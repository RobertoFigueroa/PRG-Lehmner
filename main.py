'''
Universidad Del Valle de Guatemala
LCG - Lehmner Random Number Generator 
Cifrado de información
Roberto Figueroa, Gustavo Mendez, Luis Urbina, Michele Benvenuto, Randy Venegas
Grupo 2
'''


import matplotlib.pyplot as plt

m = int(input('Choose M: '))
a = int(input('Choose A: '))
x = int(input('Choose X: '))
c = int(input('Choose C: '))
count = int(input('How many numbers print on display: '))

#Configuring plot
xAxis = []
yAxis = []
plt.title('Period of random numbers')
plt.xlabel('iteration')
plt.ylabel('random numbers')

if a >= m or c >= m or x >= m :
    print("Los valores dados no son compatibles, a, c y x deben ser menor al modulo")
else:
    x1 = (a * x + c) % m
    yAxis.append(x1)
    file = open("numbers.txt", 'w')
    for i in range(m):
        x = (a * x + c) % m
        yAxis.append(x)
        if i < count:
            print(x)
        file.write(str(x) + ', ')
        if i > 0 and x == x1: #en este caso se volvió al inicio, de esta forma se determina el módulo
            print("Period: {0}".format(i + 1))
            file.write("Period: {0}".format(i + 1))
            break
        xAxis.append(i)

#normalizing lists
xSize = len(yAxis)
ySize = len(xAxis)

if xSize > ySize:
    nextStep = xAxis[ySize-1]
    for i in range(xSize-ySize):
        nextStep += 1
        xAxis.append(nextStep)

plt.plot(xAxis, yAxis)
plt.show()

print("End.")
