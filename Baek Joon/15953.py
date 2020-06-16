def main():
    reward_2017 = [500, 300, 300, 200, 200, 200, 50, 50, 50, 50, 30, 30, 30, 30, 30, 10, 10, 10, 10, 10, 10]
    reward_2018 = [512, 256, 256, 128, 128, 128, 128]
    for i in range(8):
        reward_2018.append(64)
    for i in range(16):
        reward_2018.append(32)

    count = int(input())

    for i in range(count):
        num1, num2 = map(int, input().split())
        reward = reward_2017[num1 - 1] * 10000 if 0 < num1 <= 21 else 0
        reward += reward_2018[num2 - 1] * 10000 if 0 < num2 <= 31 else 0
        print(reward)


if __name__ == '__main__':
    main()
