import random

N = 100

table = {
    "ua": "q",
    "iu": "q",
    "zh": "q f",
    "ei": "w",
    "un": "w",
    "ch": "w j",
    "e": "e",
    "sh": "e",
    "eng": "r",
    "uan": "t",
    "ong": "y",
    "iong": "y",
    "月": "u",
    "十": "uo",
    "丿": "u",
    "亻": "i",
    "丨": "i",
    "艹": "ii",
    "钅": "io",
    "扌": "iu",
    "丶": "o",
    "口": "o",
    "日": "oi",
    "ang": "p",
    "乛": "a",
    "氵": "a",
    "贝": "ao",
    "a": "s",
    "ia": "s",
    "ie": "d",
    "ou": "d",
    "an": "f",
    "ing": "g",
    "uai": "g",
    "ai": "h",
    "ve": "h",
    "er": "j",
    "u": "j",
    "i": "k",
    "o": "l",
    "uo": "l",
    "v": "l",
    "ao": "z",
    "iang": "x",
    "uang": "x",
    "0": "x",
    "iao": "c",
    "一": "v",
    "木": "v",
    "土": "vo",
    "in": "b",
    "ui": "b",
    "en": "n",
    "ian": "m",
    "uang": "m",
}

def main():
    correct = 0
    tot = 0
    maxc = 0

    key = random.choice(list(table))
    while correct < N:
        if correct > 0:
            key = random.choice(list(table))
        print(key)
        guess = input()
        if guess == table[key]:
            correct += 1
            maxc = max(correct, maxc)
            print('Right!', correct, end='')
        else:
            correct = 0
            print(table[key], correct, end='')

        tot += 1
        print(f'/{N} 最高连对：{maxc} 总共输入：{tot}')
        print()

    print('Congratulations!!!')
    print('你学会[星空键道]了!!!')

if __name__ == '__main__':
    main()
