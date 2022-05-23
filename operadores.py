#CALCULAR EL AREA DE UN TRAINGULO
#print("Calcula el area de un triangulo \n")
#base=float(input("Ingrese el valor de la base del triangulo: \n"))
#altura=float(input("Ingrese el valor de la altura del triangulo: \n"))
#resultado=base*altura/2
#print("El area es:" + str (resultado))

#INGRESAR DOS NUMERO Y SUMARLOS
#print("Suma de dos numeros \n")
#numero1=float(input("ingrese el primer número \n"))
#numero2=float(input("ingrese el segundo número \n"))
#resultado=numero1+numero2
#print("resultado " + str (resultado))

#INGRESAR UN NUMERO Y VISUALIZARLO ELEVADO AL CUADRADO
#print("Potencia al cuadrado de un número \n")
#numero=float(input("Ingrese el numero: \n \n"))
#resultado=numero**2 
#print("La potencia es: " + str (resultado))

#ESCIBIR UN ALGORITMO QUE CONVIARTA DE EUROS A DOLARES 
#print("Conversion de Euros a Dolares \n")
#valor=float(input("ingrese el valor a convertir: \n \n"))
#euro=1
#dolar=1.06
#conversion=valor*dolar/euro
#print("El valor convertido es: " + str (conversion))

#ESCRIBIR UN ALGORITMO QUE DE EL AREA Y PERIMETRO DE UN CUADRADO 
#print("Calcular el area y perimetro de un cuadrado \n \n")
#lado=float(input("Ingrese el valor del lado del cuadrado: \n \n"))
#area=lado*lado
#print("El area del cuadrado es: \n \n" + str (area))
#print("El perimetro del cuadrado es: \n")
#perimetro=lado+lado+lado+lado
#print(str (perimetro))

#ESCRIBIR UN ALGORITMO QUE DE EL VOLUMEN Y AREA DE UN CILINDRO 
#print ("Calcula el area y el volumen de un cilindro en centímetros \n \n")
#radio=float (input("Ingrese el valor del radio del cilindro: \n \n"))
#altura=float(input("Ingrese el valor de la altura del cilindro: \n"))
#pi=3.141592
#area=2*pi*radio*altura+2*pi*radio**2
#print("El area del cilindro en centímetros cuadrados es: \n ")
#print(str (area))
#print("El volumen del cilindro en centímetros cúbicos es: \n")
#volumen=pi*radio**2*altura
#print(str (volumen))

#ESCRIBIR UN ALGORITMO QUE MUESTRE LA LONGITUD Y AREA DE UNA CIRCUNFERENCIA 
#print("Calcula la longitud y area darea de una circunferencia en centímetros \n")
#radio=float(input("Ingrese el valor del radio de la circunferencia: \n"))
#pi=3.141592
#longitud=2*pi*radio
#print(str (longitud))
#area=pi*radio**2
#print("El area de la circunferencia es:")
#print(str (area))

#CALCULAR EL PROMEDIO DE TRES NUMEROS 
#print("Calcular el promedio de tres números \n") 
#numero1=float(input("Ingrese el primer número: \n"))
#numero2=float(input("ingrese ingrese el segundo número: \n"))
#numero3=float(input("Ingrese el tercer número: \n"))
#promedio=numero1+numero2+numero3
#resultado=promedio/3
#print("El promedio de los tres números es :")
#print (str (resultado))








#ESCRIBIR UN ALGORITMO PARA SABER SI EL NUMERO INGRESADO ES POSITIVO O NEGATIVO 
#print("¿El número es negativo o positivo? \n")
#print("Escribe el número: \n")
#numero=int(input())
#if(numero>0):
 #print("El número es positivo \n \n \n")
#elif(numero<0):
 #print("El número es negativo \n \n \n")
#else:
  #print("El número es igual a cero \n \n \n")


#ESCRIBIR UN ALGORITMO QUE RECIBA DOS NÚMEROS POR TECLADO Y DIGA CUAL ES MAYOR Y CUAL ES MENOR 
#print("¿Que número es menor y que número es mayor? \n")
#numeroUno=float(input("Escriba el primer número: \n"))
#numeroDos=float(input("Escriba el segundo número: \n"))
#if(numeroUno>numeroDos):
 #print("El número mayor es: " + str (numeroUno))
 #print("El número menor es: \n \n \n" + str (numeroDos))
#elif(numeroUno<numeroDos):
 #print("El número mayor es: " + str (numeroDos))
 #print("El número menor es: \n \n \n" + str (numeroUno))
#else:
  #print("Ambos números son iguales \n \n \n")


#ESCRIBIR TRES NUMEROS ENTEROS POSITIVOS Y CACULE E IMPRIMA EL MENOR Y EL MAYOR DE ELLOS 
#print("Calcular el mayor y menor de tres numeros enteros positivos \n")
#numeroUno=int(input("Ingrese el primer número: \n"))
#numeroDos=int(input("Ingrese el segundo número: \n"))
#numeroTres=int(input("Ingrese el tercer número: \n"))
#if(numeroUno>numeroDos) and (numeroDos>numeroTres):
  #print("El número mayor es: " + str (numeroUno))
  #print("El número menor es: " + str (numeroTres))
#elif(numeroUno<numeroDos) and (numeroDos<numeroTres):
  #print("El número mayor es: " + str (numeroTres))
  #print("El número menor es: " + str (numeroUno))
#elif(numeroUno==numeroDos) and (numeroDos<numeroTres):
  #print("El número mayor es: " + str (numeroTres))
  #print("El número menor es: " + str (numeroUno))
#elif(numeroUno==numeroDos) and (numeroDos>numeroTres):
  #print("El número mayor es: " + str (numeroDos))
  #print("El número menor es: " + str (numeroTres))
#elif(numeroUno<numeroDos) and (numeroDos==numeroTres):
  #print("El número mayor es: " + str (numeroDos))
  #print("El número menor es: " + str (numeroUno))
#elif(numeroUno>numeroDos) and (numeroDos==numeroTres):
  #print("El número mayor es: " + str (numeroUno))
  #print("El número menor es: " + str (numeroDos))
#elif(numeroUno==numeroTres) and (numeroDos<numeroTres):
  #print("El número mayor es: " + str (numeroTres))
  #print("El número menor es: " + str (numeroDos))
#elif(numeroUno==numeroTres) and (numeroDos>numeroTres):
  #print("El número mayor es: " + str (numeroDos))
  #print("El número menor es: " + str (numeroUno))
#elif(numeroUno>numeroDos) and (numeroUno>numeroTres):
  #print("El número mayor es: " + str (numeroUno))
  #print("El número menor es: " + str (numeroDos))
#elif(numeroUno<numeroDos) and (numeroDos>numeroTres):
  #print("El número mayor es: " + str (numeroDos))
  #print("El número menor es: " + str (numeroUno))
#elif(numeroTres>numeroDos) and (numeroUno>numeroDos):
  #print("El número mayor es: " + str (numeroTres))
  #print("El número menor es: " + str (numeroDos))
#else:
  #print("Todos los numeros son iguales \n \n \n")


#DADOS TRES NUMEROS CALCULAR CUAL ES EL MAYOR Y CUAL ES EL MENOR
#print("Calcula el número mayor y el número menor entre tres numeros \n")
#numeroUno=float(input("Ingrese el primer número: \n"))
#numeroDos=float(input ("Escriba el segundo número: \n"))
#numeroTres=float(input("Escriba el tercer número: \n"))
#thislist=[numeroUno, numeroDos, numeroTres]
#mayor=max(thislist)
#menor=min(thislist)
#print("El numero mayor es: " + str (mayor))
#print("El numero menor es: " + str (menor))



#DADOS DOS NUMEROS SI A ES MENOR QUE B SUMARLOS, DE LO CONTRÁRIO RESTARLOS 
#print ("Si A es menor que B se suman, de lo contrario se restan \n \n")
#numeroUno=float(input("Ingrese el primer número; A: \n"))
#numeroDos=float(input("Ingrese el segundo número; B: \n"))
#if(numeroUno<numeroDos):
 #suma=numeroUno+numeroDos
 #print("La suma es: " + str(suma))
#elif(numeroUno>numeroDos):
 #resta=numeroUno-numeroDos
 #print("La resta es: " + str(resta))
#else:
 #print("No se opera porque ambos números son iguales")


#ENCONTAR EL COCIENTE ENTRE A Y B (DIVISION POR CERO NO ES POSIBLE)
#print("Calcula el cociente entre A y B \n")
#primerNumero=float(input("Ingrese el número A: \n"))
#segundoNumero=float(input("Ingrese el número B: \n"))
#if(segundoNumero==0):
  #print("La division por cero no es posible")
#elif(primerNumero>segundoNumero):
  #division=primerNumero/segundoNumero
  #print("Resultado de la división: " +  str (division))
#elif(primerNumero<segundoNumero):
  #cociente=primerNumero/segundoNumero
  #print("El resultado de la división es : " + str (cociente))
#else:
  #(primerNumero==segundoNumero)
  #igualdad=primerNumero/segundoNumero
  #print("El resultado de la división es: " + str (igualdad))


#DADOS DOS NUMEROS A Y B SI AL MENOS UNO DE ELLOS ES NEGATIVO SUMARLOS, DE LO CONTRARIO, MULTIPLICARLOS. 
#print("Dados dos numeros, A y B. Si alguno de ellos es negativo se suman, de lo contrario se multiplican \n")
#numeroUno=float(input("Ingrese el número A: \n"))
#numeroDos=float(input("Ingrese el número B: \n"))
#if(numeroUno>=0) and (numeroDos>=0):
  #multiplication=numeroUno*numeroDos
  #print("El resultado de la multiplicacion es: \n" + str (multiplication))
#elif(numeroUno<0) and (numeroDos>=0):
  #suma=numeroUno+numeroDos
  #print("El resultado de la suma es: " + str (suma))
#elif(numeroUno>=0) and (numeroDos<0):
  #suma=numeroUno+numeroDos
  #print("El resultado de la suma es: " + str (suma))
#else:
  #(numeroUno>0) and (numeroDos<0)
  #suma=numeroUno+numeroDos
  #print("El resultado de la suma es: " + str (suma))


#DETERMINAR SI UN AÑO ES BISIESTO O NO
#print("Determinar si el año ingresado es bisiesto o no: \n")
#ear=int(input("Ingrese el año: \n"))
#division=year/4
#if(year % 4 == 0):
  #print("El año SI es bisiesto")
#elif(year % 100 ==0): 
  #print("El año SI es bisiesto \n\n")
#else:
  #print ("El año NO es bisiesto \n\n")