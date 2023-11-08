import csv
global user
#Insert
def insert(user):
    l=open("details.csv","a+")
    lr=csv.reader(l)
    lw=csv.writer(l)
    #Name,Age,Branch,Salary
    Name=user
    for i in lr:
        if i[0]==Name:
            print("Record for Staff already exists, cannot add more")
        else:
            pass
    Age=int(input("Enter Age: "))
    Branch=input("Enter Branch: ")
    Salary=float(input("Enter Salary: "))
    det=[Name,Age,Branch,Salary]
    lw.writerow(det)
    l.close()
#View
def View(user):
    v=open("details.csv","r")
    vr=csv.reader(v)
    for i in vr:
        if i[0]==user:
            print(i)
        else:
            if user not in vr:
                print("Record not Found")
    v.close()
#Edit
def Edit(user):
    e=open("details.csv","r")
    er=csv.reader(e)
    e.close()
    e=open("details.csv","w")
    ew=csv.writer(e)
    ch=int(input("Enter Value to be Edited:\n(1)Age\n(2)Branch\n(3)Salary\nEnter Choice: "))
    if ch==1:
        new=int(input("Enter New Age: "))
        for  i in er:
            if i[0]==user:
                i[ch]==new
            else:
                pass
    elif ch==2:
        new=input("Enter new Value: ")
        for i in er:
            if i[0]==user:
                i[ch]==new
    elif ch==3:
        new=float(input("Enter new Value: "))
        for i in er:
            if i[0]==user:
                i[ch]==new
    ew.writerows(er)
    print("File Updated")
    e.close()
#Bonus Calc
def Bonus(user):
    b=open("details.csv","r")
    br=csv.reader(b)
    for i in br:
        if i[0]==user:
            print("Bonus=",i[3]*0.25)
            print("Total Salary=",i[3]+(i[3]*0.25))
        else:
            pass
    b.close()
#Main
def main():
    user=input("Enter Username: ")
    ans="y"
    while ans.lower()=="y":
        ch=int(input("**MAIN MENU**\n(1)Insert\n(2)View\n(3)Edit\n(4)Calculate Bonus\nEnter Choice: "))
        if ch==1:
            insert(user)
        elif ch==2:
            View(user)
        elif ch==3:
            Edit(user)
        elif ch==4:
            Bonus(user)
        else:
            print("Invalid Choice.")
            ans=input("Do you want to continue operation(Y): ")
        ans=input("Do you want to continue operation(Y): ")
    print("Terminating Software")

main()
