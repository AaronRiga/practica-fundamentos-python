#como ejecutar: terminal----> python segundapractica.py
#cadena de caracteres
nombre= input("introduce tu nombre")
print(f"hola {nombre}")
print("Hola, {}!}".format(nombre))

#entero
edad=20

#flotante=decimales
altura=1.90

#convertir tipos de datos
edadString=str(edad)

print(edad+edad)
print(edadString+edadString)

#Verificar de que tipo es mi variable
print(type(edadString))

#booleano
boolleanos=False

tuedad=input("introduce tu edad")
tuedad=int(tuedad)

#Estructuras de control
if tuedad>=18 and tuedad<100:
    print("Eres mayor de edad")
elif tuedad>=200:
    print("Eres inmortal")
elif tuedad<0:
    print("no existes")
else:
    print("eres menor de edad")

for i in range(0,10):
    print(i)

dia=input("introduce un día")
dia=int(dia)

with switch(dia) as s:
    if s.case(15):
        print("Es quincena")