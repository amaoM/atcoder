# coding: utf-8

if __name__ == '__main__':
  [N, M] = [int(i) for i in input().split()]
  res = [0 for _ in range(M + 1)]
  for i in input().split():
    res[int(i)] += 1
  max_count = max(res)
  if N / max_count >= 2:
    print('?')
  else:
    print(res.index(max_count))
