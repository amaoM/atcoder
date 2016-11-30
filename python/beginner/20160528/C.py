# coding: utf-8

def main():
    n = int(input())
    al = list(map(int, input().split()))
    c = 1
    tc = 1

    for i in range(1, n):
        if al[i] > al[i - 1]:
            tc += 1
        else:
            tc = 1
        c += tc

    print(c)

if __name__ == '__main__':
    main()
