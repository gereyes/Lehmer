#Numeros pseudoAleatorios por el metodo lehmer
#Genesis Jesus Reyes Osnaya

contador = 1
xo = int(input("Ingresa la semilla: ")) #Ingresamos la semilla
c = int(input("Ingresa el numero c: ")) #Ingresamos el numero C
numero = int(input("Ingresa la cantidad de numeros: ")) #Ingresamos la cantidad
xoj = xo

if(xo>c):
    print("")
    print("Resta: " , xo)
    while(contador < numero):
        
        multiStr = str(xo * c) #Se hace la multiplicacion

        ope = len(multiStr) - len(str(xoj)) #Sacamos los tamanos

        derecha = int(multiStr[ope:])
        izquierda = int(multiStr[:ope])
        resultado = derecha - izquierda #Restamos el numero mayor con el menor


        xo = resultado
        print("Resta: " , xo)
        contador = contador + 1

else:
    print("")
    print("La semilla debe ser mas grande que el numero")
    kgh
