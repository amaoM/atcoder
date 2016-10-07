# coding: utf-8
import math
import copy

if __name__ == '__main__':
  [A, B, C] = [int(i) for i in input().split()]
  mx = 10000
  mn = 0
  t = 5000

  def f(t):
    return A * t + B * math.sin(C * t * math.pi)

  while True:
    ft = int(f(t))
    if ft == 100:
      break
    elif ft > 100:
      mx = copy.deepcopy(t)
      t = (mx + mn) / 2
      f(t)
    elif ft < 100:
      mn = copy.deepcopy(t)
      t = (mx + mn) / 2
      f(t)
  print(t)
