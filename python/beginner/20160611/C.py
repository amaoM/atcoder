# coding: utf-8;

def main():
    s = input()
    k = 'WBWBWWBWBWBW' * 3
    m = ["Do","Do","Re","Re","Mi","Fa","Fa","So","So","La","La","Si"]
    print(m[k.find(s)])

if __name__ == '__main__':
    main()
