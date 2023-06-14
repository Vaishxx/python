class Movie_tickets:
    s=['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10']
    def __init__(self,seats,price,seat_no):
        self.seats=seats  #total no. of seats
        self.price=price
        self.seat_no=seat_no
        print(self.seats,self.price,self.seat_no)
    def book(self):
        if self.seats>0:
            print("your seats have been booked.")
            self.seats=self.seats-1
        else:
            print("Sorry!The seats are full for now")
    def cancelled_seats(self,seat_no):
        print("your seats have been cancelled")
        self.seats=self.seats+1


    def remaining_seats(self):
        print("no. of seats reaming are:",self.seats)    

person1=Movie_tickets(300,200,'a1')
person2=Movie_tickets(400,150,'a10')
person1.book()
person2.book()
person2.remaining_seats()
person3=Movie_tickets(300,200,'a1')


            


        
