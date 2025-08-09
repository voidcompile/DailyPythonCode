#!/usr/bin/env python3
"""
explain_package.py
A small utility that explains a Python package:
- if package is installed: show docstring, version, top-level attrs
- if not installed: query PyPI to get summary and project links
"""

import sys
import importlib
import inspect
from textwrap import fill, indent

# import importlib.metadata with fallback for older Pythons
try:
    from importlib import metadata as importlib_metadata
except Exception:
    import importlib_metadata  # requires 'importlib-metadata' backport on Python <3.8

# optional dependency (standard widely-available lib). If not present, requests will be used.
try:
    import requests
except ImportError:
    requests = None

PYPI_JSON_URL = "https://pypi.org/pypi/{name}/json"

def pretty_print(title, text, width=80):
    print(f"\n=== {title} ===")
    if not text:
        print("(no information)")
        return
    for line in fill(text, width=width).splitlines():
        print(line)

def explain_installed_package(name):
    """Try to import the package and show docstring, version, and sample attributes."""
    try:
        module = importlib.import_module(name)
    except Exception as e:
        return False, f"Failed to import package '{name}': {e}"

    # docstring (first part)
    doc = inspect.getdoc(module) or ""
    first_para = doc.split("\n\n")[0] if doc else ""

    # version (try metadata then attribute)
    version = None
    try:
        # try to get distribution name from importlib.metadata
        try:
            version = importlib_metadata.version(name)
        except Exception:
            # sometimes distribution name differs from import name; try module attribute
            version = getattr(module, "__version__", None)
    except Exception:
        version = getattr(module, "__version__", None)

    # list some top-level attributes (functions/classes) as sample
    attrs = []
    try:
        candidates = [a for a in dir(module) if not a.startswith("_")]
        # pick a few representative names
        for a in candidates[:12]:
            try:
                obj = getattr(module, a)
                kind = "func" if inspect.isfunction(obj) else ("class" if inspect.isclass(obj) else type(obj).__name__)
                attrs.append(f"{a} ({kind})")
            except Exception:
                attrs.append(a)
    except Exception:
        attrs = []

    info = {
        "name": name,
        "version": version,
        "summary": first_para,
        "attributes": attrs,
        "location": getattr(module, "__file__", "built-in / dynamic"),
    }
    return True, info

def explain_from_pypi(name):
    """Query PyPI JSON API for package summary and project URLs."""
    if not requests:
        return False, "requests library is not installed; cannot query PyPI. Install with: pip install requests"

    url = PYPI_JSON_URL.format(name=name)
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            info = data.get("info", {})
            summary = info.get("summary") or info.get("description") or ""
            home_page = info.get("home_page")
            project_urls = info.get("project_urls") or {}
            version = info.get("version")
            return True, {
                "name": name,
                "version": version,
                "summary": summary,
                "home_page": home_page,
                "project_urls": project_urls
            }
        elif resp.status_code == 404:
            return False, f"Package '{name}' not found on PyPI."
        else:
            return False, f"PyPI returned status {resp.status_code} for package '{name}'."
    except Exception as e:
        return False, f"Failed to query PyPI: {e}"

def main():
    if len(sys.argv) >= 2:
        package_name = sys.argv[1]
    else:
        package_name = input("Enter the package name (e.g. numpy, requests, flask): ").strip()

    if not package_name:
        print("Package name is empty. Exiting.")
        return

    print(f"\nExplaining package: {package_name}")

    ok, result = explain_installed_package(package_name)
    if ok:
        info = result
        pretty_print("Package (installed) Summary", f"{info.get('summary') or 'No docstring summary available.'}")
        print(f"\nVersion: {info.get('version')}")
        print(f"Location: {info.get('location')}")
        pretty_print("Top-level attributes (sample)", ", ".join(info.get("attributes") or []))
        return

    # if not installed or import failed, show import error and try PyPI
    print(f"\nNote: Import failed or package not installed locally: {result}")
    print("Trying to fetch metadata from PyPI...")

    ok2, result2 = explain_from_pypi(package_name)
    if ok2:
        info = result2
        pretty_print("PyPI Summary", info.get("summary"))
        print(f"\nLatest version on PyPI: {info.get('version')}")
        if info.get("home_page"):
            print(f"Home page: {info.get('home_page')}")
        if info.get("project_urls"):
            print("\nProject URLs:")
            for k, v in info.get("project_urls").items():
                print(f"- {k}: {v}")
    else:
        print(f"Could not fetch PyPI info: {result2}")

if __name__ == "__main__":
    main()
