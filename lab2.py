#Code by Pratik Shrestha(23026137)
#code to calculate the monthly and yearly average of temperature
#taking the input as no of year from the user
no_of_years=int(input("Enter the number of years:"))
i=0
j=0
total_month=no_of_years*12
avg_1=0
high=0
while(j<=no_of_years):
    i=0
    while(i<=12):         #applying the while loop to ask the user average monthly high temperature 
        no_of_month=int(input("Enter the average monthly high temperature:"))
        i=i+1

        total_temp=avg_1+no_of_month
        Avg_temp=total_temp/12

        if(no_of_month>high):
            high=no_of_month
    print("The highest temperature of the period is:",high)
    print("The average high temperature of", no_of_years,"year is:",Avg_temp,"deg C")
    j=j+1
        

    


