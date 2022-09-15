month = input("Enter the month(The first letter should be capital): ")
day = int(input("Enter the date "))

if month in ('January', 'February', 'March'):
	season = 'winter'
elif month in ('April', 'May', 'June'):
	season = 'Summer'
elif month in ('July', 'August', 'September'):
	season = 'Spring'
else:
    season='Fall'

if (month == 'March') and (day > 19):
	season = 'Summer'
elif (month == 'June') and (day > 20):
	season = 'Spring'
elif (month == 'September') and (day > 21):
	season = 'Fall'
elif (month == 'December') and (day > 20):
	season = 'winter'

print("Season is",season)
