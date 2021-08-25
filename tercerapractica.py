#uso de la libreria random para generar datos aleatorios
import random
print(random.randint(1,20))

#Generar una campana de datos
import matplotlib.pyplot as plt


#Introducir un rango de valores
import random
print(random.randrange(10,100,2))

#Reacomodar una lista al azar
lista=[1,2,3,4,5,6,7,8,9,10]
print('Lista original' , lista)

random.shuffle(' Lista mixeada', lista)

campana=[random.gauss(1-0.5)for  in range(1000)]
plt.hist(campana, bins=15)
plt.show()

#pegar esto para crear un archivo READ ME de Github----> echo "# practica-fundamentos-python" >> README.md 
#git init 
#git add README.md 
#git commit -m "first commit" 
#git branch -M main 
#git remote add origin https://github.com/AaronRiga/practica- fundamentos-python.git
 #git push -u origin main