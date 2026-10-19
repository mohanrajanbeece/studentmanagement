
while True:
    print("1.Add")
    print("2.View")
    print("3.search")
    print("4.Delete")
    print("5.Exit")

    choice = input("enter your choice(1,2,3,4,5): ")
    if choice =='1':
        name=input("Enter the name: ")
        with open("student.md","a") as file:
            file.write(name +"\n")
        
    elif choice=='2':
        print("student details:")
        with open ("student.md","r+") as file:
            print(file.read())
    elif choice=='3':
        name=input("Enter the name:")
        with open ("student.md","r+") as file:
            line=file.read()
            
            if name in line:
                    print("name is available")
            else:
                    print("record not found")         
    #
    elif choice=='4':
        name=input("enter the student name:")
        with open("student.md","r") as file:
            line=file.readlines()
        with open("student.md","w") as file:
            file.writelines(n for n in line if n.strip() != name)
        print("name removed" if any(n.strip() == name for n in line) else "name not found")
            
  
    elif choice =='5':
        "Exit"
        break
    