def main():
    N = int(input())
    S = input()
    ec = S.count('E')
    wc = 0
    min = ec
    for k in S:
        if k == 'E':
            ec -= 1
            if min > ec + wc: min = ec + wc
        else:
            wc += 1
    print(min)

if __name__ == '__main__':
    main()