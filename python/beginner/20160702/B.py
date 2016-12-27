# coding: utf-8;

def main():
    a, b, c = map(int, input().split())
    print(a * b * c % (10 ** 9 + 7))
    
if __name__ == '__main__':
    main()
