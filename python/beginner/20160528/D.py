# coding: utf-8

def dp(i, boxs, cm):
    if cm[i] > 0: return cm[i]
    th, tw = boxs[i][0], boxs[i][1]
    tc = 1
    for j, box in enumerate(boxs):
        h, w = box[0], box[1]
        if th > h and tw > w:
            tc = max(tc, dp(j, boxs, cm) + 1)

    cm[i] = tc
    return tc

def main():
    n = int(input())
    boxs = []
    cm = [0 for _ in range(n)]

    for _ in range(n):
        h, w = map(int, input().split())
        boxs.append((h, w))

    res = 0
    for i in range(n):
        res = max(res, dp(i, boxs, cm))

    print(res)

if __name__ == '__main__':
    main()
