##Movie Ticket Booking System 4
def booking(book_seat):
  if book_seat not in booked_seats:
    l.remove(book_seat)
    booked_seats.append(book_seat)
  else:
    print("The seat is already booked")
def cancellation(cancel_seat):
  if cancel_seat in booked_seats:
    booked_seats.remove(cancel_seat)
    ###l.append(cancel_seat)

###This is main method###
total_seats=int(input("total_seats = "))
l=list(range(1,11))
booked_seats=eval(input("booked_seats = "))
for i in booked_seats:
  l.remove(i)
book_seat=int(input("book_seat = "))
cancel_seat=int(input("cancel_seat = "))
booking(book_seat)
cancellation(cancel_seat)
print(l)

