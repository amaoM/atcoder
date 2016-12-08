# coding: utf-8;

def main():
    n, x = map(int, input().split())
    print(min(n - x, x - 1))

if __name__ == '__main__':
    main()
