#pgm_to_check_the_season

#function_that_return_the_season...
def season(month, date):
    if((month >= 11 and date >=21) or (month <=3 and date <=19)):
        return 'winter'
    if((month >= 3 and date >=20) or (month <=6 and date <=20)):
        return 'summer'
    if((month >= 6 and date >=21) or (month <=9 and date <=21)):
        return 'spring'
    if((month >= 9 and date >=22) or (month <=11 and date <=20)):
        return 'fall'
 

 #------main_function-------
month = input('Which month is this :')

date = int(input('Who told the date :'))

if(month == 'january'):
    m=1
elif(month == 'february'):
    m=2
elif(month == 'march'):
    m= 3
elif(month == 'april'):
    m = 4
elif(month == 'may'):
    m=5
elif(month == 'june'):
    m=6
elif(month == 'july'):
    m=7
elif(month == 'august'):
    m=8
elif(month == 'september'):
    m=9
elif(month == 'october'):
    m=10
elif(month == 'november'):
    m=11
elif(month == 'december'):
    m=12
print('It\'s  ',season(m,date))
