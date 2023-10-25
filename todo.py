# Coded by Harsh Vishwakarma 
# CUI Based Todo app
# Task 1. Codsoft Internship 

task_list=[] # List for storing & manipulating records 

def create(task):
    task_list.append(task)
    print("Task added successfully !")
    ch=input("wanna add more tasks: Y/N: ").upper()

    if ch=='Y':
                task=input("Enter your task :")
                create(task)
    
 

def delete():
    if len(task_list)!=0:
        display()
    
        ch=int(input("Enter task no: "))
        del task_list[ch-1]
        print("Task deleted !")
    else:
        print("No  task exist !")
    

def update():
    if len(task_list)!=0:
        display()
    
        ch=int(input("Enter task no: "))
        del task_list[ch-1]
        
        n_t=input("Enter updated task:")
        task_list.insert(ch-1,n_t)
        print("Task updated Successfully!")
    else:
        print("No  task exist !")
    

def display():
    if len(task_list)!=0:
        for i in range(len(task_list)):
        
            print('\n',i+1,'. ',task_list[i])
        print()
    else:
        print("No tasks to display!")


def menu():
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Update Tasks")
    print("4. Delete Task")
    print("5. Exit")

    ch=int(input("Enter choice: "))

    if ch==1:
        task=input("Enter your task :")
        create(task)
    
    elif ch==2:
        display()

    elif ch==3:
        update()

    elif ch==4:
        delete()

    
    elif ch==5:
        exit()
    else:
        print("Invalid Choice!")





print("****************TODO-APP********************")
while 1:
    menu()