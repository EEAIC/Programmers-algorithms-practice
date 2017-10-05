def getDayName(a,b):
    answer = ""
    day = [ 'FRI', 'SAT' , 'SUN', 'MON', 'TUE', 'WED', 'THU']
    total_days = - 1
    date = 0
    for i in range(1,a):
        if i != a:
            if i in [1,3,5,7,8,10]:
                total_days += 31
            elif i in [4,6,9,11]:
                total_days += 30
            elif i == 2:
                total_days += 29
    total_days += b
    date = total_days % 7
    return day[date]

#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))
