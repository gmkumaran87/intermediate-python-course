
def hourglass(arr):
    rows = len(arr) - 2
    cols = len(arr[0]) - 2

    for i in range(rows):
        for j in range(cols):
            yield (arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] +arr[i+2][j] + arr[i+2][j + 1] + arr[i+2][j + 2])

def maxhourglass(arr):
    return max(hourglass(arr))

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(arr)
    print(f'Maximum sum of Hourglass - {maxhourglass(arr)}')


