#Bitlabs Question 2
### Restaurant Menu Management 2

def add1(item):
  menu.append(item)
def remove1(item):
  if item in menu:
    menu.remove(item)
  else:
    print("The item ",item,"to be removed is not present")
def check1(item):
  if item in menu:
    print(item,"is available")
  else:
    print(item,"is not avilable")
menu=eval(input("initial_menu = "))
add_item=input("add_item = ")
add1(add_item)
remove_item=input("remove_item = ")

remove1(remove_item)

check_item=input("check_item = ")
print("Updated menu:",menu)
check1(check_item)