#Intro programa

print("Hola mi nombre es Marvin y estoy aqui para ayudarte")
nombre = input("Cual es tu Nombre? ")
print("Un gusto en conocerte " + nombre)
eleccion = int(
    input(
        "Que puedo hacer hoy por ti: \n 1 Sacar el área de un circulo \n 2 Sacar el área de un cuadrado \n 3 Sacar el área de un tringulo \n 4 Sacar el promedio \n 5 Formar una oración \n"
    ))

#1 Área del circulo

if eleccion == 1:
    print("De acuerdo, quieres sacar el área de un círculo")
    pi = 3.14

    r = int(input("Cuanto mide el radio: "))
    area = (pi * r)**2

    print("El área es ", area)

#2 Área de un cuadrado
if eleccion == 2:
    print("De acuerdo, quieres sacar el área de un cuadrado")

    lado = int(input("Cuanto mide un lado: "))
    area = (lado * lado)

    print("El área es ", area)

#3 Área de un triangulo

if eleccion == 3:
    print("De acuerdo, quieres sacar el área de un tringulo")

    base = int(input("Cuanto mide la base: "))
    altura = int(input("Cuanto mide la altura: "))
    area = (base * altura) / 2

    print("El área es ", area)

#4 Promedio de 3 calificaciones

if eleccion == 4:
    print("De acuerdo, quieres sacar el primedio de 3 calificaciones")

    cal1 = int(input("Cual es la primera calificación: "))
    cal2 = int(input("Cual es la segunda calificación: "))
    cal3 = int(input("Cual es la tercera calificación: "))
    promedio = (cal1 + cal2 + cal3) / 3

    print("El promedio es: ", promedio)

# Concatenar palabras

if eleccion == 5:
    print("De acuerdo, quieres que forme una oración")

    pal1 = str(input("Cual es la primera palabra: "))
    pal2 = str(input("Cual es la segunda palabra: "))
    pal3 = str(input("Cual es la tercera palabra: "))
    pal4 = str(input("Cual es la cuarta palabra: "))
    pal5 = str(input("Cual es la quinta palabra: "))

    frase = (pal1 + pal2 + pal3 + pal4 + pal5)

    print("La frase que forman tus palabras es: ", frase)
