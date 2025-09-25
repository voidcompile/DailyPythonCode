# bio-kmer-counter
A tiny, fast k‑mer counter for FASTA files (DNA/RNA). No external deps by default.


## Features
- Stream FASTA (supports `.gz`)
- Canonical mode (merge reverse complements)
- CSV export, optional bar plot (matplotlib only if you pass `--plot`)
- GC%, N-rate, length summary


## Usage
```bash
python kmer_counter.py path/to/sequences.fa -k 3 --canonical --top 20 --csv kmers.csv --plot top20.png
```

Multiple inputs are allowed:
```
python kmer_counter.py a.fa b.fa.gz -k 5 --canonical --top 30
```

## Options

-k, --k: k‑mer length (1..12 recommended)

--canonical: count each k‑mer with its reverse complement as one

--normalize: show relative frequencies (0..1)

--top N: print top‑N table to stdout (default 20)

--csv FILE: write full counts to CSV

--plot FILE: save a bar plot for the printed top‑N

--alphabet {DNA,RNA}: map T↔U as needed (default DNA)

## Example FASTA
>seq1
ACGTACGTNNACGT
>seq2
TTGACGTTGACA
Notes

Non‑[ACGTU] letters break k‑mers at those positions (skipped).

For large k or long genomes, memory use scales with number of unique k‑mers; consider smaller --top and CSV for full data.

License

MIT © VoidCompile
