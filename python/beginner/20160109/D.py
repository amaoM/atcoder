# coding: utf-8

def main():
    N, W = map(int, input().split())

    l = [0 for _ in range(W+1)]

    pv = 0
    pw = 0

    for n in range(N):
        v, w = map(int, input().split())

        if v > l[w]:
            l[w] = v

        if W >= pw + w and pv + v > l[pw+w]:
            l[pw+w] = pv + v

        pv = v
        pw = w
    print(max(l))

if __name__ == '__main__':
    main()
