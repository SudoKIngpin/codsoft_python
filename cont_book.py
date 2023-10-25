clist=[]

def add_contact(name,Pno,email,address):
    d={}
    d["Name"]=name
    d["Address"]=address
    d["PhoneNo"]=Pno
    d['Email']=email
    clist.append(d)
    print("Contact added sucessfully!")

def view():
    if len(clist)!=0:
        for c in range(len(clist)):
            print()
            print(c+1,'.','\tName', ': ',clist[c]["Name"])
            print('.','\tAddress', ': ',clist[c]["Address"])
            print('.','\tPhoneNo', ': ',clist[c]["PhoneNo"])
            print('.','\tEmail', ': ',clist[c]["Email"])
            print()
    else:
        print("Contact book is EMPTY!")
    
def search(name):
    if len(clist)!=0:
        for i in range(len(clist)):

            if name.lower()==clist[i]["Name"].lower():
                print("Details found !")
                print()
                print('\tName', ': ',clist[i]["Name"])
                print('.','\tAddress', ': ',clist[i]["Address"])
                print('.','\tPhoneNo', ': ',clist[i]["PhoneNo"])
                print('.','\tEmail', ': ',clist[i]["Email"])
                return i
                break
                
        else:
                print("Details not found !")
                
                
                
    
    else:
        print("Contact book is EMPTY!")

def delete(name):
    
    if len(clist)!=0:
        i=search(name)
        if i!=None:
            del clist[i]
            print("Record deleted successfully!")
                         
    else:
        print("Contact Book  Empty!")

def update(name):
        j=search(name)
        print("Enter 1 to update Name")
        print("Enter 2 to update Address")
        print("Enter 3 to update PhoneNo")
        print("Enter 4 to update Email")
        ch=int(input("Enter choice:"))
        if ch==1:
            n=input("Enter new name :")
            clist[j]["Name"]=n
            print("Name updated!")
        if ch==2:
            a=input("Enter new address :")
            clist[j]["Address"]=a
            print("Adress updated!")
        if ch==3:
            p=int(input("Enter new Phone no :"))
            clist[j]["PhoneNo"]=p
            print("Phone number updated!")
        if ch==4:
            e=input("Enter new Email :")
            clist[j]["Email"]=e
            print("Email updated!")



        
def menu():
    print("--------------------------------------")
    print("Enter 1 for adding contact")
    print("Enter 2 to view contact")
    print("Enter 3 to update contact details")
    print("Enter 4 to search contact")
    print("Enter 5 to delete contact")
    print("Enter 6 to EXIT")
    print("---------------------------------------")

    ch=int(input("Enter choice:"))

    if ch==1:
        name=input("Enter name of contact:")
        Pno=int(input("Enter phone no:"))
        email=input('Enter email id:')
        address=input("Enter address: ")
        add_contact(name,Pno,email,address)

    elif ch==2:
        view()
    elif ch==3:
        if len(clist)!=0:
            name=input("Enter name :")
            update(name)
        else:
            print("Contact Book Empty")
    elif ch==4:
            if len(clist)!=0:
                    name=input("Enter Name :")
                    search(name)
            else:
                    print("Contact Book Empty")


    elif ch==5:
                if len(clist)!=0:

                    name=input("Enter Name :")
                    delete(name)
                else:
                    print("Contact Book Empty")
    elif ch==6:
        exit()


    else:
        print("Invalid choice")



while 1:
    menu()


