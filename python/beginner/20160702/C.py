# coding: utf-8;

def main():
    n = int(input())
    al = list(map(int, input().split()))
    for _, i in sorted([(a, i) for i, a in enumerate(al)], key=lambda x:x[0], reverse=True): print(i + 1)

if __name__ == '__main__':
    main()
