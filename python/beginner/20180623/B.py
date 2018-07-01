def main():
    N = input()
    Sn = 0
    for n in N: Sn += int(n)
    print('Yes' if int(N) % Sn == 0 else 'No')
    
if __name__ == '__main__':
    main()