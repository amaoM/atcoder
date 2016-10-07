#coding: utf-8

if __name__ == '__main__':
  [l_1, l_2, l_3] = [int(l) for l in input().split()]
  if l_1 == l_2:
    print(l_3)
  elif l_1 == l_3:
    print(l_2)
  else:
    print(l_1)
