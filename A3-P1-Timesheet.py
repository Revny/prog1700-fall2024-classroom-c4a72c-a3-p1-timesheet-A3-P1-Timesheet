#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #:     
#Student Name:Lucas  


    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    
workday =[1,2,3,4,5] #the lists that the program uses
hoursworked = []
hours =[]


for i in range(len(workday)):
        hours=int(input(f"enter in the hours you worked #{i+1}:")) #i will increse by one untill it hits 5
        hoursworked.append(hours)
        

totalhours =sum (hoursworked) #totalhours and averagehours
average = totalhours/5

print(f"the total hours within in the week is {totalhours}")
(print(f"the average hours are {average}"))

minworkhours= min(hoursworked) #min hours
print(f"your min work hours are {minworkhours}")


           


   # YOUR CODE ENDS HERE

def main():
    
    main()