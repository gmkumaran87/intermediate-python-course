if __name__ == '__main__':
    n = int(input())

    # Listify the given values [['1'],['2'],['3']]
    #arr = list(map(list, input().rstrip().split()))
    arr = list(map(str, input().rstrip().split()))
    print(arr)
    rev_arr = ' '.join(arr[::-1])
    print(rev_arr)

