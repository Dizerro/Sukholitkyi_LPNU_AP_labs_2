def rabin_karp_search_from_file(file_path, needle):
    d = 256
    q = 101

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            haystack = f.read()
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []

    m = len(needle)
    n = len(haystack)

    if m > n:
        return []

    h = pow(d, m - 1) % q
    p = 0
    t = 0

    for i in range(m):
        p = (d * p + ord(needle[i])) % q
        t = (d * t + ord(haystack[i])) % q

    result = []

    for i in range(n - m + 1):
        if p == t:
            if haystack[i:i + m] == needle:
                result.append(i)
        if i < n - m:
            t = (d * (t - ord(haystack[i]) * h) + ord(haystack[i + m])) % q
            if t < 0:
                t += q

    return result

if __name__ == "__main__":
    file_path = "text.txt"
    needle = input("Введіть рядок для пошуку: ")

    positions = rabin_karp_search_from_file(file_path, needle)

    if positions:
        print(f"Знайдено '{needle}' на позиціях:", positions)
    else:
        print(f"Рядок '{needle}' не знайдено у файлі.")