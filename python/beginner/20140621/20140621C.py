# coding: utf-8

def caluc(N, NG_list):

    def __caluc(n, NG_list):
        if n in NG_list:
            return False
        else:
            return n

    yield __caluc(N - 1, NG_list)
    yield __caluc(N - 2, NG_list)
    yield __caluc(N - 3, NG_list)

def judge(N, NG_list):
    N_list = [N]

    if N in NG_list:
        return 'NO'

    for i in range(100):
        
        if len(N_list) == 0:
            return 'NO'

        N = N_list.pop()

        for n in caluc(N, NG_list):

            if n is False:
                continue

            if n == 0:
                return 'YES'

            N_list.append(n)

    return 'NO'


if __name__ == '__main__':
    args = []

    for i in range(4):
        args.append(int(input()))

    print(judge(args[0], [args[1], args[2], args[3]]))
