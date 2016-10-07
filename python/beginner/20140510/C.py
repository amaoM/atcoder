import copy
import math

if __name__ == '__main__':
  N = int(input())
  c_list = [int(input()) for _ in range(N)]

  def pattern(l, r, s, c):
    for n in range(len(l)):
      tmp_l = copy.deepcopy(l)
      tmp_r = copy.deepcopy(r)
      tmp_s = copy.deepcopy(s)
      tmp_r.append(tmp_l[n])
      del tmp_l[n]
      if len(tmp_l) == 0:

        for i in range(len(tmp_r) - 1):
          for ii in range(i + 1, len(tmp_r)):
            if tmp_r[ii] % tmp_r[i] == 0:
              tmp_s[ii] = abs(tmp_s[ii] - 1)

        return c + sum(tmp_s)
      else:
        c = pattern(tmp_l, tmp_r, tmp_s, c)
    return c
  print(pattern(c_list, [], [1 for _ in range(N)], 0) / math.factorial(N))
