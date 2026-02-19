wantLine = int(input())

blank = " "
star = "*"
# 줄 수
for i in range(wantLine, 0, -1):

    # 공백, 별 수
    for j in range(1, (2 * wantLine) + 1, 2):

        if i > 0:
            i = i - 1
            print(i * blank, j * star, sep="")

    print(end="")
    break