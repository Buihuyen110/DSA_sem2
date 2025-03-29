from Lab4.utils import read, write

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'


def poly_hash(s, base=257, mod=10 ** 9 + 7):
    """Вычисление полиномиального хеша строки."""
    hash_value = 0
    for i, c in enumerate(s):
        hash_value = (hash_value * base + ord(c)) % mod
    return hash_value


def get_hashes(s, length, base=257, mod=10 ** 9 + 7):
    """Вычисление хешей всех подстрок строки s длины length."""
    n = len(s)
    hashes = {}
    base_power = 1  # base^length % mod
    for i in range(length):
        base_power = (base_power * base) % mod

    # Вычисляем хеш для первой подстроки
    current_hash = 0
    for i in range(length):
        current_hash = (current_hash * base + ord(s[i])) % mod

    hashes[current_hash] = [0]  # хеш и его индекс начала

    # Прокачиваем хеши для других подстрок
    for i in range(1, n - length + 1):
        current_hash = (current_hash * base - ord(s[i - 1]) * base_power + ord(s[i + length - 1])) % mod
        if current_hash not in hashes:
            hashes[current_hash] = []
        hashes[current_hash].append(i)

    return hashes


def common_substring(s, t):
    # Двоичный поиск по длине
    left, right = 0, min(len(s), len(t))
    best_length = 0
    best_indices = []

    while left <= right:
        mid = (left + right) // 2
        # Хеши подстрок длины mid для обеих строк
        s_hashes = get_hashes(s, mid)
        t_hashes = get_hashes(t, mid)

        found = False

        # Ищем общие хеши
        for t_hash, t_indices in t_hashes.items():
            if t_hash in s_hashes:
                # Если хеши совпадают, проверяем сами подстроки
                for i in s_hashes[t_hash]:
                    for j in t_indices:
                        if s[i:i + mid] == t[j:j + mid]:
                            if mid > best_length:
                                best_length = mid
                                best_indices = [(i, j)]
                            elif mid == best_length:
                                best_indices.append((i, j))
                            found = True
                            break
                    if found:
                        break
            if found:
                break

        if found:
            left = mid + 1  # Пытаемся найти подстроку большей длины
        else:
            right = mid - 1  # Ищем меньшую длину

    return best_indices, best_length

def main():
    lines = read(PATH_INPUT, 7)
    results = []
    for line in lines:
        s, t = line.split()
        best_indices, best_length = common_substring(s, t)

        if best_length == 0:
            results.append(f"0 1 0")
        else:
            for i, j in best_indices:
                results.append(f"{i} {j} {best_length}")

    write(PATH_OUTPUT, results, 7)

if __name__ == "__main__":
    main()
