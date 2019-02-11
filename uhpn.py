import random

N = 50

ans = { idx: False for idx in range(N) }

def rights(ans):
    tot = 0
    for k, v in ans.items():
        if v:
            tot += 1
    return tot

table = {
    'iu': 'q',
    'ia': 'w',
    'ua': 'w',
    'uan': 'r',
    'ue': 't',
    've': 't',
    'ing': 'y',
    'uai': 'y',
    'sh': 'u',
    'ch': 'i',
    'uo': 'o',
    'un': 'p',
    'iong': 's',
    'ong': 's',
    'iang': 'd',
    'uang': 'd',
    'en': 'f',
    'eng': 'g',
    'ang': 'h',
    'an': 'j',
    'ao': 'k',
    'ai': 'l',
    'ei': 'z',
    'ie': 'x',
    'iao': 'c',
    'zh': 'v',
    'ui': 'v',
    'ou': 'b',
    'in': 'n',
    'ian': 'm',
}

def main():
    idx = 0

    while rights(ans) < N:
        key = random.choice(list(table))
        print(key)
        guess = input()
        if guess == table[key]:
            ans[idx] = True
            print('Right!', rights(ans), end='')
        else:
            ans[idx] = False
            print(table[key], rights(ans), end='')
        idx = (idx + 1) % N

        print('/%s' % N)
        print()

    print('Congratulations!!!')
    print('你学会双拼了!!!')

if __name__ == '__main__':
    main()
