# coding: utf-8;

def main():
    n = int(input())
    zip_dict = {}
    a_list = [int(input()) for _ in range(n)]
    u_list = sorted(list(set(a_list)))
    for i, a in enumerate(u_list):
        zip_dict[a] = i
    for a in a_list:
        print(zip_dict[a])

if __name__ == '__main__':
    main()
