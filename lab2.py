#Code by Pratik Shrestha(23026137)
#code to calculate the monthly and yearly average of temperature
#taking the input as no of year from the user
no_of_years=int(input("Enter the number of years:"))
i=0
total_month=no_of_years*12
avg_1=0
while(i<=total_month):         #applying the while loop to ask the user average monthly high temperature 
    no_of_month=float(input("Enter the average monthly high temperature:"))
    i=i+1
    total_temp=avg_1+no_of_month
    Avg_temp=total_temp/total_month
print("The average high temperature of", no_of_years,"year is:",Avg_temp,"deg C")
high=35
if(no_of_month>high):
    print("The highest temperature of the period is:",)
    


