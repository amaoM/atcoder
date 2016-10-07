#coding: utf-8
class Node:
  def __init__(self, i):
    self.left = None
    self.right = None
    self.x = i

  def fight(self, tern):
    if tern == 'T':
      if self.left.x <= N:
        self.left.fight('A')
      else:
        print('A')
    else:
      if self.right.x <= N:
        self.right.fight('T')
      else:
        print('T')

def loop(node):
  if node.x > N:
    return node
  node.left = loop(Node(2 * node.x))
  node.right = loop(Node(2 * node.x + 1))
  return node

if __name__ == '__main__':
  N = int(input())
  x = 1
  deep = 0

  while N > 0:
    N /= 2
    deep += 1

  print(deep)

  # node = loop(Node(x))
  # node.fight('T')
