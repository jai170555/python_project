stu=["jai","pummy","prem"]
def ask():
    print("choose any one option")
    print("1.show list of students")
    print("2.add name to list")
    print("3.remove name from list")
    print("4.search for name")
    print("5.exit\n")
    n=int(input("\nentry a number\n"))
    if n==1:show()
    elif n==2:add()
    elif n==3:remove()
    elif n==4:search()
    elif n==5:exit()
def show():
    for i in stu:
        print(i)
    print()
def add():
    name=input("enter name to add")
    print("name added")
    stu.append(name)
def remove():
    name=input("enter name to remove")
    if name in stu:
        stu.remove(name)
        print("name remove")
    else:
        print("name not  found")
def search():
    name=input("enter name to search")
    if name in stu:
        print("name found")
print("-"*40,"\n'''welcome to student managment system***\n","-"*40)
ask()
while(True):
    ask()
    n=input("\ndo you want to continue y/n")
    if n=="y":
        continue
    else:
        exit()
