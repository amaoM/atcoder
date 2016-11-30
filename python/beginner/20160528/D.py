# coding: utf-8

def dp(th, tw, boxs, c, cl):
    for box in boxs:
        h, w = box[0], box[1]
        if th > h and tw > w:
            cl.append(c + 1)
            cl = dp(h, w, boxs, c + 1, cl)
    return cl

def main():
    n = int(input())
    boxs = []

    for _ in range(n):
        h, w = map(int, input().split())
        boxs.append((h, w))

    cl = dp(10 ** 5, 10 ** 5, boxs, 0, [])

    print(max(cl))

if __name__ == '__main__':
    main()
