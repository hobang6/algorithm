# https://www.acmicpc.net/problem/15954
# 카카오 코드 페스티벌 2018 예선 B번 

from decimal import Decimal


def main():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    result = []
    acc_sum = [0 for i in range(N + 1)]   # 누적 합
    acc_square = [0 for i in range(N + 1)]    # 제곱의 누적 합

    for i in range(1, len(arr) + 1):
        acc_sum[i] = acc_sum[i - 1] + arr[i - 1]
        acc_square[i] = acc_square[i - 1] + arr[i - 1] ** 2

    for i in range(K, N + 1):
        for j in range(N - i + 1):
            mean = Decimal(acc_sum[i + j] - acc_sum[j]) / i     # 부분 합으로 평균 구하기
            square_mean = Decimal(acc_square[i + j] - acc_square[j]) / i       # 제곱의 부분 합으로 제곱의 평균 구하기
            var = Decimal(square_mean - (mean * mean))       # 분산 = 제평평제
            result.append(var)

    print(Decimal(min(result)).sqrt())


if __name__ == '__main__':
    main()
