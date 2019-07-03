#2) VERIFICAR EDAD
Age = int(input("Ingrese su edad: "))#Pedimos la edad del usuario
#Comparamos la edas, si es igual o mayor a 18 realizara...
if Age >= 18:
    print('Eres mayor de edad, puedes ir por putas')
#Si el usuario se equivoca imprime un mensaje de error
elif Age <= 0:
    print('Que pedo')
#Si no es mayor a 18 realiza...
else:
    print('¿Eres virgen?')    
input('Presione Intro para finalizar')#La pausax2
