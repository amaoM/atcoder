# coding: utf-8;

def main():
    s = input()
    ans = ''

    for i, c in enumerate(s):
        if c == '1' or c == '0':
            ans += c
        elif i > 0:
            ans = ans[:-1]

    print(ans)

if __name__ == '__main__':
    main()
