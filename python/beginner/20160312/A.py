# coding: utf-8

def main():
    x, y = map(int, input().split())
    if x > y:
        print('Worse')
    else:
        print('Better')

if __name__ == '__main__':
    main()
