# coding: utf-8;

def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    n, l = map(int, input().split())
    s = [input() for _ in range(n)]
    s.sort()
    print(''.join(s))

if __name__ == '__main__':
    main()
