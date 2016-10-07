# conding: utf-8

if __name__ == '__main__':
  A, B, C, D, E = [int(i) for i in input().split()]
  print(max([A + D + E, B + C + E]))
