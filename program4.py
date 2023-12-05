#Code by Pratik Shrestha(23026137)
#simple python code to demonstrate the list, function and sort element 
#declaring list

given_number=[4,6,9,12,17,44,27,33,22]
print(given_number)
for j in range (0,8):
    for i in range (0,8):
        if(given_number[i+1]>given_number[i]):
            z=given_number[i+1]
            given_number[i+1]=given_number[i]
            given_number[i]=z

print(given_number)      



