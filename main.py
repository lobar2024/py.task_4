def is_palindrome_num(n):
    s = str(abs(n))
    return s == s[::-1]

def largest_palindrome_product(digits):
    """N xonali ikki sonning ko'paytmasidan eng katta palindrom."""
    lo = 10**(digits-1)
    hi = 10**digits - 1
    best = 0
    for i in range(hi, lo-1, -1):
        if i*i < best: break
        for j in range(i, lo-1, -1):
            p = i*j
            if p < best: break
            s = str(p)
            if s == s[::-1]: best = p
    return best

def palindrome_pairs(words):
    """Juftlashganda palindrom hosil qiladigan juftlar."""
    word_set = {w: i for i, w in enumerate(words)}
    result   = []
    for i, word in enumerate(words):
        for k in range(len(word)+1):
            prefix = word[:k]; suffix = word[k:]
            r_prefix = prefix[::-1]; r_suffix = suffix[::-1]
            if r_suffix in word_set and word_set[r_suffix] != i:
                s = suffix
                if s == s[::-1]: result.append([word_set[r_suffix], i])
            if k and r_prefix in word_set and word_set[r_prefix] != i:
                s = prefix
                if s == s[::-1]: result.append([i, word_set[r_prefix]])
    return result

if __name__ == "__main__":
    for n in [121, -121, 12321, 12345]:
        print(f"{n:>6} → {is_palindrome_num(n)}")

    print("\nEng katta 2 xonali palindrom:", largest_palindrome_product(2))
    print("Eng katta 3 xonali palindrom:", largest_palindrome_product(3))
