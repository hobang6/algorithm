# https://www.acmicpc.net/problem/4344

# 평균은 넘겠지

def main():
    num = int(input())

    for i in range(num):
        data = list(map(int, input().split()))
        student_num = data[0]
        data.remove(data[0])
        mean = sum(data) / student_num
        count = 0
        for j in data:
            if j > mean:
                count += 1
        print('%.3f' % ((count / student_num) * 100) + '%')


if __name__ == '__main__':
    main()
