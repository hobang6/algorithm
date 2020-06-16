# https://www.acmicpc.net/problem/8958

# OX퀴즈

def main():
    num = int(input())

    for i in range(num):
        quiz_result = input()
        count, result = 0, 0
        for c in quiz_result:
            if c == 'O':
                count += 1
            else:
                count = 0
            result += count
        print(result)


if __name__ == '__main__':
    main()
