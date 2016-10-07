#coding: utf-8

if __name__ == '__main__':
  N = int(input())
  A = [int(i) for i in input().split()]
  if sum(A) % N != 0:
    print(-1)
  else:
    b = 0
    s = 0
    avg = sum(A) / N
    for i in range(N - 1):
      s += A[i]
      if s != avg * (i + 1):
        b += 1
    print(b)
