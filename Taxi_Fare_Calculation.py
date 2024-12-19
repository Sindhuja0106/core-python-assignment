###Taxi Fare Calculation 7

def calculate(trips):
  j=1
  total=0
  for i in trips:
    fare=0
    fare=50+(i*10)
    print(f"Trip {j}: ${fare}") 
    j=j+1
    total=total+fare
  print(f"Total Fare: ${total}") 
trips=eval(input("trips = "))
calculate(trips)    