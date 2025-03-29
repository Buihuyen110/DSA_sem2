from Lab4.utils import read, write

PATH_INPUT = '../txtf/input.txt'
PATH_OUTPUT = '../txtf/output.txt'

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    for i in range(1, len(pattern)):
        while length > 0 and pattern[i] != pattern[length]:
            length = lps[length - 1]
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
    return lps

def kmp_search(text, pattern):
    if not pattern:
        return []
    lps = compute_lps(pattern)
    i = j = 0
    occurrences = []
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                occurrences.append(i - j + 1)
                j = lps[j - 1]
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    return occurrences

def main():
    p, t = read(PATH_INPUT, 1)
    results = kmp_search(t, p)
    write(PATH_OUTPUT, results, 1)

if __name__ == "__main__":
    main()
