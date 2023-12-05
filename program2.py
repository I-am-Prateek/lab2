#Code by Pratik Shrestha(23026137)
#Monitoring the calory data of a user
daily_cal_intake=float(input("Enter the starting daily calory intake:"))
if(daily_cal_intake<0):
    print("Enter the positive value")
else:
    print()

#asking the user to enter the input as no of days and percentage user want to decrease
decrease_percentage=float(input("Enter the calories decrease in percentage:"))

no_of_days=int(input("Enter the number of day you want to calculate:"))

#calculating the average percentage
avg_daily_percentage_dec=decrease_percentage/100

all_calories=daily_cal_intake
for i in range(1,no_of_days+1):
        calories*=(1-avg_daily_percentage_dec/100)
        if(all_calories<1200):
            print("You need to stabilize the diet")
        else:
            print("The decrease in calories per day is:",all_calories)

            