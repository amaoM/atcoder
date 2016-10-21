# coding: utf-8

def main():
    N = int(input())
    a, b = map(int, input().split())
    K = int(input())
    PL = list(map(int, input().split()))

    for i, p in enumerate(PL):
        if p == a or p == b: return False
        if p in PL[i + 1:]: return False

    return True

if __name__ == '__main__':
    if main():
        print('YES')
    else:
        print('NO')
