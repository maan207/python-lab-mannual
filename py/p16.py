
#Python Program to demonstrate the use of class
print("Program :- MSc CS & CL Semester-1")
print("Name : Mansi Rathod")
print("Enrollment : 92600565012")
print("Practical-16")
class MyNewClass:
    """This class demonstrates the creation of objects"""
#instance attribute
    num=100
    #instance method
    def hello(self):
        print("\n Hello World !")
#creating object of MyNewClass
obj = MyNewClass()
print(obj.num)
obj.hello()
print(MyNewClass.__doc__)

