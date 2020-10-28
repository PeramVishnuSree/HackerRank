year = int(input())
leap_year = 0
# julian calender
if year<1918 :
    if year%4 == 0:
        leap_year += year 

#Gregorian calender
elif year>1918:
    if year%4 ==0 and year%100!= 0:
        leap_year += year
    elif year%400 == 0:
        leap_year += year

if year == leap_year:
    print("12.09." + str(leap_year))
#year of transition
elif year == 1918:
    print("26.09.1918")
else:
    print("13.09." + str(year))   
             
