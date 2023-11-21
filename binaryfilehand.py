import csv
f=open("c.csv","w")
w=csv.writer(f) # returns csv writer object
w.writerow(["ENO","ESAL"]) 
n=int(input("Enter Number of Employees:"))
for i in range(n):
    eno=input("Enter Employee No:")
   # ename=input("Enter Employee Name:") 
    esal=input("Enter Employee Salary:")
    #eaddr=input("Enter Employee Address:")
    w.writerow([eno,esal]) 
print("Total Employees data written to csv file successfully") 