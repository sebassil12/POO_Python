class Student():
    def __init__(self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def studying(self):
        print("Studying...") 

nombre = input("What's your name: ")
age = int(input("What's your age: "))
grade = int(input("What's your grade: "))

estudiante = Student(nombre, age, grade)

print(f"""
      DATOS DEL ESTUDIANTE \n\n
      Nombre: {estudiante.name} \n
      Edad: {estudiante.age} \n
      Grado: {estudiante.grade} \n
      """
)

while True:
    estudiar = input()
    if(estudiar.lower() == "estudiar"):
        estudiante.studying()