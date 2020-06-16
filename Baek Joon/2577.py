# https://www.acmicpc.net/problem/2577

# 숫자의 개수

def main():
    a = int(input())
    b = int(input())
    c = int(input())

    arr = list(str(a * b * c))

    for i in range(10):
        count = 0
        while True:
            if str(i) in arr:
                arr.remove(str(i))
                count += 1
            else:
                break
        print(count)


if __name__ == '__main__':
    main()
