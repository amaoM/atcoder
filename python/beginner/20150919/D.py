# coding: utf-8
import copy

if __name__ == '__main__':
  N = int(input())
  res = N // 10
  if N % 10 > 0:
    res += 1

  for i in range(1, len(str(N))):
    if N // (10 ** (i + 1)) * 10 ** i == 0:
      if N // (10 ** i) > 1:
        res += 10 ** i
      else:
        res += N % (10 ** i) + 1
    else:
      res += (N // (10 ** (i + 1)) + 1) * 10 ** i

  print(res)
