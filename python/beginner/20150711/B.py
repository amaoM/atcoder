# coding: utf-8
import math

if __name__ == '__main__':
  N = int(input())
  circle_area = []

  for _ in range(N):
    circle_area.append(int(input()) ** 2 * math.pi)

  circle_area.sort(reverse=True)

  red_area = 0

  for n in range(N):
    red_area += pow(-1, n) * circle_area[n]

  print(red_area)
