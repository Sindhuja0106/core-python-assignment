#Bitlabs question1 1

##E-Commerce Cart System**
names=list(map(str,input("Enter the names of the items:").split()))
values=list(map(float,input("Enter the price of each items:").split()))
d=dict(zip(names,values))
l=list(d.values())
if not d:
  print("items are not selected .please make sure items are selectes")
elif len(l)<5:
  result=sum(l)
  print("The total price without discount  is:",int(result))
else:
  s=sum(l)
  s=s*0.9
  print("The total price with 10% discount is:",int(s))