# coding: utf-8
class Queue:

    def __init__(self):
        self.tree_list = []

    def enqueue(self, tree):
        self.tree_list.append(tree)

    def dequeue(self):
        return self.tree_list.pop(0)

    def is_empty(self):
        pass


if __name__ == '__main__':
    tree_list = []    
    queue = Queue()

    n = int(input())

    for i in range(1, n):
        f, s = map(int, input().split())
        queue.enqueue([f, s])

    c = 0
    while True:
        tree = queue.dequeue()
        next_tree = queue.dequeue()

        if tree[0] in next_tree:
            k = next_tree.index(tree[0])
            queue.enqueue(sorted(next_tree[k-1:], reverse=True) + tree)
            # if k != 0 and k != len(tree) and queue.tree_list not in tree:
            #     queue.enqueue(tree)
            print(queue.tree_list)
            continue

        if tree[1] in next_tree:
            k = next_tree.index(tree[1])
            queue.enqueue(sorted(tree, reverse=True) + next_tree[:k])
            # if k != 0 and k != len(tree) and queue.tree_list not in tree:
            #     queue.enqueue(tree)
            print(queue.tree_list)
            continue

        queue.enqueue(tree)
        queue.enqueue(next_tree)

        if c > 10:
            exit()

        c += 1

    



    

