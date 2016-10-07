# conding: utf-8

if __name__ == '__main__':
  # S = list(input())
  # chars = ['A', 'B', 'C', 'D', 'E', 'F']
  # res = [0 for _ in range(6)]
  # for s in S:
  #   res[chars.index(s)] += 1
  # print(' '.join(str(r) for r in res))

  S = input()
  print(*[S.count(c) for c in 'ABCDEF'])
