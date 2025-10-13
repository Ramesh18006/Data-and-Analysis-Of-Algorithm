import time
# Naive String Search
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    comparisons = 0

    start_time = time.time()
    for i in range(n - m + 1):
        for j in range(m):
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
        else:
            print(f"Naive Match found at index {i}")
    end_time = time.time()

    return comparisons, end_time - start_time
# KMP Algorithm
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    comparisons = 0

    i = j = 0
    start_time = time.time()
    while i < n:
        comparisons += 1
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            print(f"KMP Match found at index {i - j}")
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    end_time = time.time()

    return comparisons, end_time - start_time
# Input
text = "AbAbABa"
pattern = "AbA"

naive_ops, naive_time = naive_search(text, pattern)
kmp_ops, kmp_time = kmp_search(text, pattern)

print("\n--- Comparison Summary ---")
print(f"Naive Search: {naive_ops} comparisons, {naive_time:.6f} seconds")
print(f"KMP Search:   {kmp_ops} comparisons, {kmp_time:.6f} seconds")

