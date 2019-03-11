import json


_CHAR = '0123456789abcdefghijklmnopqrstuvwxyz'


def count2(data, base):
    left = (_CHAR.index(data[0]), _CHAR.index(data[1]))
    next = sorted([left[0], (left[0] + 1) % base])
    if len(data) == 2:
        return [v <= left[1] for v in next].count(True), left[1] in next
    if left[1] > next[1]:
        return 2 ** (len(data) - 1), False
    elif left[1] == next[1]:
        result, include = count2(data[1:], base)
        return result + 2 ** (len(data) - 2), include
    elif left[1] > next[0]:
        return 2 ** (len(data) - 2), False
    elif left[1] == next[0]:
        return count2(data[1:], base)
    else:
        return 0, False


def count(data, base):
    left_dig = _CHAR.index(data[0])
    len_guru = len(data) - 1
    if len(data) == 1:
        return left_dig, True
    # calc boundary
    result, include = count2(data, base)
    # total of shorter len(data)
    result += (base - 1) * (2 ** len_guru - 1)
    if left_dig > 1:
        result += (left_dig - 1) * 2 ** len_guru
    return result, include


def solve(data):
    b, start, end = data.split(',')
    b = int(b)
    upper, _ = count(end, b)
    lower, include = count(start, b)
    result = upper - lower
    if include:
        result += 1
    return f'{result}'


if __name__ == '__main__':
    data = json.load(open('data.json'))
    for case in data['test_data']:
        actual = solve(case["src"])
        ok = actual == case["expected"]
        print(("ok" if ok else "**NG**"), case["src"], actual, case["expected"])
