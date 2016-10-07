# conding: utf-8

if __name__ == '__main__':
    R, C, K = map(int, input().split())
    N = int(input())

    get_position = {}

    for _ in range(N):
        r, c = map(int, input().split())
        for rr in range(1, R + 1):
            if r == rr:
                if (rr, cc) not in get_position:
                    get_position[(rr, cc)] = 1
                else:
                    get_position[(rr, cc)] += 1;

            for cc in range(1, C + 1):
                if c == cc: 
                    if (rr, cc) not in get_position:
                        get_position[(rr, cc)] = 1
                    else:
                        get_position[(rr, cc)] += 1;

    print(get_position)