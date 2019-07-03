
#3) CALIFICACIÓN
Cal = int(input("Ingrese su calificación: "))#Pido al usuario una calificación entera
#Comparo su calificacion, dependiendo que valor me de sera el mensaje que me dara
if Cal < 0:
    print('Error. Estas bien pendejo e idiota, metiste un numero negativo.')
elif Cal < 5:
    print('suspenso. si no sabes que significa es que estas bien pendejo y reprobaste, echale ganas')
elif Cal == 5:
    print('Suficiente. Reprobaste cagada, echale ganas, apoco quieres recursar')
elif Cal == 6:
    print('Aprovado. Por la minima cabron, siguete esforzando, no quieres ver el mensaje si repruebas')
elif Cal == 7:
    print('Notable. Pues sigues valiendo madres, puedes mejorar, pero si te vale madres la materia Congratulations')
elif Cal >= 8:
    print('Sobresaliente. Felicidades campeón, aunque todos sabemos que pasaste por barbero con el profesor')
input('Presione Intro para finalizar')#La pausax3
