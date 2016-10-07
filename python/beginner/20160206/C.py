# coding: utf-8

def main():
    print(len([True for p in input().split('+') if '0' not in p]))

if __name__ == '__main__':
    main()
