# coding: utf-8

if __name__ == '__main__':
  N, K = [int(i) for i in input().split()]
  print(((N - K) * (K - 1) * 6 + 1 + (N - 1) * 3) / N ** 3)
