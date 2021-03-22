def compare():
    rows = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    flag = 0
    for row in rows:
        if row < 9:
            # print("this number is {}".format(row))
            flag += 1
    return flag


if __name__ == "__main__":
    aaa = compare()
    print(aaa)

