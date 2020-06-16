# https://www.acmicpc.net/problem/1110

# 더하기 사이클

def main():
    num = '{0:02d}'.format(int(input()))
    result = num
    cnt = 0

    while True:
        result = result[1] + str(int(result[0]) + int(result[1]))[-1:]
        cnt += 1
        if result == num:
            print(cnt)
            break


if __name__ == '__main__':
    main()
