# coding: utf-8;

import math

def main():
    h, w, a, b = map(int, input().split())
    ans = math.factorial(h - a - 1 + w - b - 1) / (math.factorial(h - a - 1) * math.factorial(w - b - 1))
    for i in range(b, w):
        ans = ans + math.factorial(h - a - 1 + w - i - 1) / (math.factorial(h - a - 1) * math.factorial(w - i - 1))
    print(ans)




if __name__ == '__main__':
    main()
