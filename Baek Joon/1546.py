# https://www.acmicpc.net/problem/1546

# 평균

def main():
    num = int(input())
    arr = list(map(int, input().split()))
    max_num = max(arr)

    for i in range(num):
        arr[i] = (arr[i] / max_num) * 100
    print(sum(arr) / num)


if __name__ == '__main__':
    main()
