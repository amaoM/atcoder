# coding: utf-8 
 
if __name__ == '__main__':
    more_or_less = []
 
    c = int(input())
 
    for i in range(c):
        s, e = map(int, input().split())
 
        if e + 2 > len(more_or_less):
            more_or_less += [0 for i in range(len(more_or_less), e + 2)]

        more_or_less[s] += 1
        more_or_less[e + 1] -= 1

    v = 0
    ans = 0

    for i in more_or_less:
        v += i
        ans = max(ans, v)

    print(ans)
