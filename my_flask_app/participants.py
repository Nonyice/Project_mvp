#!/user/bin/env/python3

class Participants:
	
    def __init__(self,first_name,last_name,age,sex):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.sex=sex
    @property
    def first_name(self):
        return self.__first_name
  
    @first_name.setter
    def first_name(self, value):
        self.__first_name=value
   
    @property
    def last_name(self):
        return self.__last_name
  
    @last_name.setter
    def last_name(self, value):
        self.__last_name=value
   
    @property
    def age(self):
        return self.__age
  
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError ("Age must be a number in integer")
        elif value <=0:
            raise ValueError ("Does look like you tyoed in an invalid age")
        self.__age=value
	
    @property
    def sex(self):
        return self.__sex
  
    @sex.setter
    def sex(self, value):
        self.__sex=value
	
    def welcome(self):
        print("Welcome " + (self.__first_name +" " + self.__last_name) + " " + "You are one of the participants and we appreciate your coming " + " " + "\n....................... kindly wait while we find your group\n")

fn=input("Please enter your first name: ")
ln=input("please enter your last names: " )
ag=int(input("How old are you, please:?: "))
sx=input("Are you male or female? ")

pat1=Participants(fn,ln,ag,sx)
pat1.welcome()
