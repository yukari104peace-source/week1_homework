def create_kuku_table():
    # 9行9列の九九表を2次元リストで返す
    table = []

    for i in range(1, 10):
        row = []

        for j in range(1, 10):
            row.append(i * j)

        table.append(row)

    return table


def main():
    table = create_kuku_table()

    # 1行ずつ、スペース区切りで表示する
    for row in table:
        for product in row:
            print(f"{product} ", end="")

        print()


if __name__ == "__main__":
    main()
