#coding: utf-8
if __name__ == '__main__':
  N = int(input())
  vote = {}
  for _ in range(N):
    S = input()
    if S in vote:
      vote[S] += 1
    else:
      vote[S] = 1

  print(max([(v, k) for(k, v) in vote.items()])[1])
