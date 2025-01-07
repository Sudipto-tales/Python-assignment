#My Details

class My_Details:
    def __init__(self,name,age,education, institute):
        self.name = name
        self.age = age
        self.education = education
        self.institute = institute
 
class Display(My_Details):
    def display(self):
        print(f"Hello!! I am {self.name}, {self.age} old pursuing {self.education} from {self.institute}.")
        
name = input("Enter your name: ")
age = int(input("Enter your age: "))
education = input("Enetr your Course: ")
institute = input("Enter your Institute name: ")

myself = Display(name, age, education, institute)
myself.display()