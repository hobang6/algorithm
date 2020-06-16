# https://www.acmicpc.net/problem/2525

# 오븐 시계

def main():
    hour, minute = map(int, input().split())
    duration = int(input())

    total_time = (hour * 60) + minute + duration

    if total_time >= 60 * 24:
        total_time -= 60 * 24

    print('%d %d' % (total_time // 60, total_time % 60))


if __name__ == '__main__':
    main()
