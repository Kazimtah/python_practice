class Student():

    class_year = 2024 #The variable is a class variable not a method varibale.
    num_student = 0 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student +=1


student1 = Student("Mohamad Kazim", 31)
#print(student1.name, student1.age, student1.class_year)
student2 = Student("Patrick", 35, )
#print(student2.name, student2.age, student2.class_year)

student3 = Student("Alyas", 32)
#print(student3.name, student3.age)
student4 = Student("Zaman", 24)


#print("***********************")
#print(Student.num_student)

print(f"My graduated student of {Student.class_year} has number of {Student.num_student}")

print(student1.name, student4.age)
print(student2.name, student4.age)
print(student3.name, student4.age)
print(student4.name, student4.age)