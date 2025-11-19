# Segundo-Repositorio
#Este es mi segundo Repositorio voy a guardar mis archivos
#Barreras Leon Ricardo
#3°B Programacion


numero = 1
Factores = ''
Res = 0

print ('¿Que numero quieres factorizar?')
NumeroFactorial = int (input ())

for i in range ( 1 , NumeroFactorial +1):
    Res *= i

for i in range ( 1 ,numero +1 ):
    Factores += str (i) + "X"

Factores = Factores [:-3]

print (f'{NumeroFactorial} != {Factores} = {Res}')
