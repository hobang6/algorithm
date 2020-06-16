# https://www.acmicpc.net/problem/4673

# 셀프 넘버

def main():
    n_set = set(range(1, 10001))
    g_set = set()

    for i in range(1, 10001):
        for j in str(i):
            i += int(j)
        g_set.add(i)

    for i in sorted(n_set - g_set):
        print(i)


if __name__ == '__main__':
    main()
