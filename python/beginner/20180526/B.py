def main():
    N = int(input())
    S = input()
    max = 0;
    for i in range(1, N):
        l = S[:i]
        r = S[i:]
        used = []
        for k in l:
            if k in r and k not in used:
                used.append(k)
        if len(used) > max: max = len(used)
    print(max)

if __name__ == '__main__':
  main()