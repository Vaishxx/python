class RailwayForm():
    formtype="ReservationForm"
    def printdata(self):
        print("Name is",self.name)
        print("Age is",self.age)
        print("Train is",self.train)
    

ApplicationForm=RailwayForm()
ApplicationForm.name="Vaishnavi"
ApplicationForm.age="20"
ApplicationForm.train="Shatabdi Express"
ApplicationForm.printdata()

