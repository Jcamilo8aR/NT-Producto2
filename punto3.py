# Calcular la nota final de una materia, teniendo en cuenta las notas de los cuatro peridos y luego decir si gana o pierde esta.

materia = input("Materia: ")

print("Primer Periodo")
p1Nota1 = float(input("Nota 1: "))
p1Nota2 = float(input("Nota 2: "))
p1Nota3= float(input("Nota 3: "))

print("Segundo Periodo")
p2Nota1 = float(input("Nota 1: "))
p2Nota2 = float(input("Nota 2: "))
p2Nota3= float(input("Nota 3: "))

print("Tercer Periodo")
p3Nota1 = float(input("Nota 1: "))
p3Nota2 = float(input("Nota 2: "))
p3Nota3= float(input("Nota 3: "))

print("Cuarto Periodo")
p4Nota1 = float(input("Nota 1: "))
p4Nota2 = float(input("Nota 2: "))
p4Nota3= float(input("Nota 3: "))

calcularPeriodo = lambda nota1,nota2,nota3: (nota1 + nota2 +nota3)/3

totalP1=calcularPeriodo(p1Nota1,p1Nota2,p1Nota3)
totalP2=calcularPeriodo(p2Nota1,p2Nota2,p2Nota3)
totalP3=calcularPeriodo(p3Nota1,p3Nota2,p3Nota3)
totalP4=calcularPeriodo(p4Nota1,p4Nota2,p4Nota3)

calcularTotal =  lambda nota1,nota2,nota3,nota4: (nota1 + nota2 +nota3+nota4)/4
notaFinal= calcularTotal(totalP1,totalP2,totalP3,totalP4)

calcularResultado = lambda total: "Pierde la materia"  if total < 3 else "Gana la materia"
anotacion = calcularResultado(notaFinal)


print (f'\n3Materia: {materia} \nPerido 1: {totalP1} \nPeriodo 2: {totalP2} \nPeriodo3: {totalP3} \nPeriodo 4: {totalP4} \nNota Final: {notaFinal} \n{anotacion}')
