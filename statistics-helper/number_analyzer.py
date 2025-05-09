import math
import statistics
from collections import Counter
import matplotlib.pyplot as plt

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    """Return the prime factors of a number."""
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

def analyze_single_number(num):
    """Perform basic analysis on a single number."""
    print(f"\n🔍 Analysis for number: {num}")
    print("Even" if num % 2 == 0 else "Odd")
    print("Prime" if is_prime(num) else "Composite")
    
    if math.isqrt(num) ** 2 == num:
        print("Perfect square ✅")
    
    print(f"Prime factors: {prime_factors(num)}")

def analyze_number_list(numbers):
    """Perform statistical analysis on a list of numbers."""
    print("\n📊 Statistical Analysis")
    print(f"Count: {len(numbers)}")
    print(f"Minimum: {min(numbers)}")
    print(f"Maximum: {max(numbers)}")
    print(f"Mean: {statistics.mean(numbers):.2f}")
    
    if len(numbers) >= 2:
        print(f"Median: {statistics.median(numbers)}")
        print(f"Variance: {statistics.variance(numbers):.2f}")
        print(f"Standard Deviation: {statistics.stdev(numbers):.2f}")
    else:
        print("More numbers needed for median, variance, and std deviation.")
    
    print(f"Sum: {sum(numbers)}")
    print(f"Range: {max(numbers) - min(numbers)}")
    
    # Frequency distribution
    counts = Counter(numbers)
    plt.bar(counts.keys(), counts.values(), color='lightgreen')
    plt.title("Histogram of Number Frequencies")
    plt.xlabel("Number")
    plt.ylabel("Frequency")
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.show()

def main():
    user_input = input("Enter a number or a comma-separated list of numbers: ").strip()
    
    try:
        if ',' in user_input:
            numbers = [int(x) for x in user_input.split(',')]
            analyze_number_list(numbers)
        else:
            num = int(user_input)
            analyze_single_number(num)
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()
