import random

N = 50

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
    tot = 0

    while tot < N:
        key = random.choice(list(table))
        print(key)
        guess = input()
        if guess == table[key]:
            tot += 1
            print('Right!', tot, end='')
        else:
            tot = 0
            print(table[key], tot, end='')

        print('/%s' % N)
        print()

    print('Congratulations!!!')
    print('你学会[自然]双拼了!!!')

if __name__ == '__main__':
    main()
