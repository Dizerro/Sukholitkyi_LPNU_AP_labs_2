def is_ukrainian_upper_letter(char):
    return char in 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'

def is_valid_passport(candidate):
    if len(candidate) != 8:
        return False
    return (
        is_ukrainian_upper_letter(candidate[0]) and
        is_ukrainian_upper_letter(candidate[1]) and
        all(c.isdigit() for c in candidate[2:])
    )

def rabin_karp_passport_search(file_path):
    d = 256
    q = 101
    m = 8
    passports = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []

    n = len(text)
    h = pow(d, m - 1) % q
    t = 0

    for i in range(m):
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if is_valid_passport(text[i:i + m]):
            passports.append(text[i:i + m])
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q

    return passports

def filter_passports_by_series(passports, series):
    return [p for p in passports if p.startswith(series)]

if __name__ == "__main__":
    file_path = "generated_text.txt"
    passports = rabin_karp_passport_search(file_path)

    if not passports:
        print("Паспортів не знайдено.")
    else:
        print("Знайдені паспорти:")
        for p in passports:
            print(p)

        while True:
            series = input("Введіть серію для фільтрації (або 'вихід' для завершення): ").upper()
            if series == "ВИХІД":
                break
            if len(series) != 2 or not all(is_ukrainian_upper_letter(c) for c in series):
                print("Серія має складатися з 2 великих українських літер.")
                continue
            filtered = filter_passports_by_series(passports, series)
            if filtered:
                print(f"Паспорти з серією {series}:")
                for p in filtered:
                    print(p)
            else:
                print(f"Паспортів з серією {series} не знайдено.")
