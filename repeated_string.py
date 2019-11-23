"""
 The occurrences of a letter in a substring.
 Substring is gotten by the first n characters of the finite string given
"""


def get_occurrence(s, l):
    occurrence = 0
    for letter in s:
        if letter == l:
            occurrence += 1
    return occurrence


""" Approach One: Loop through and get the substring """


def repeated_string(s, n, l):
    for i in range(n - 1):
        if len(s) < n - 1:
            s += s

    if len(s) > n:
        s = s[0: n]

    print(s)
    return get_occurrence(s, l)


def repeated_string_two(s, n, l):
    r = n // len(s)  # get the number of times the string can be printed
    s = s * r

    if len(s) < n:
        s += s

    if len(s) > n:
        s = s[0: n]

    print(s)
    return get_occurrence(s, l)


def main():
    print(repeated_string_two("mua", 10, "a"))


if __name__ == "__main__":
    main()
