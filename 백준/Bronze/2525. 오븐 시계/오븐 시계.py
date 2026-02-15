nowHour, nowMinute = input().split()
plus = int(input())


resultMinute = int(nowMinute) + plus
resultHour = int(nowHour) + (resultMinute // 60)


# 분의 합이 60분보다 적을 때
if int(nowMinute) + plus < 60:
    print(nowHour, resultMinute, sep=" ")

# 분의 합이 60분보다 많고 24시간이 안넘을 때
elif resultHour < 24:
    highResultMinute = resultMinute % 60
    print(resultHour, highResultMinute, sep=" ")
# 분의 합이 60분보다 많고 24시간이 넘을 때
else:
    highResultHour = resultHour % 24
    highResultMinute = resultMinute % 60
    print(highResultHour, highResultMinute, sep=" ")
