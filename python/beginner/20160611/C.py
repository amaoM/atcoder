# coding: utf-8;

def main():
    l = ['Do', 'Re', 'Mi', 'Fa', 'So', 'Ra', 'Si']
    s = input()
    k = 'WW'
    i = s.find(k)
    j = s.find(k, i + 1)
    if j - i == 7:
        print(l[4 - i])
    else:
        print(l[4 + i])

if __name__ == '__main__':
    main()
