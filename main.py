import os
import random
def miselanea ():
  print("MISELANEA EJERCICIOS PROGRAMACION PYTHON \n  Menú: \n   1) Operadores \n   2) Condicionales \n   3) Ciclos \n   4) Arreglos \n   00) Terminar programa")
  print("Ingrese la opcion que desee:")
  numero = int(input())
  os.system("clear")
  def operadores ():
    while True:
        print("Bienvenido a operadores \n Menu \n  1) Calcular el area de un triangulo.\n  2) Suma de dos numeros.\n  3) Número elevado al cuadrado.\n  4) Convierta euros a dolares.\n  5) Valor del area y perimetro de un cuadrado\n  6) Area y volumen de un cilindro.\n  7) Longitud y area de un circulo.\n  8) Promedio de tres numeros.\n  99) Regresar. \n")
        numeroO = int(input("Ingrese la opcion que quiera: "))
        os.system("clear")
        if (numeroO==99):
          return miselanea ()
          break 
        elif (numeroO == 1):
            print("Calcular el area de un triangulo.")
            base = float(input("Ingrese el valor de la base del triangulo: \n"))
            altura = float(
                input("Ingrese el valor de la altura del triangulo: \n"))
            resultado = base * altura / 2
            print("El area es:" + str(resultado))
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return operadores ()
        elif (numeroO == 2):
            print("Suma de dos numeros \n")
            numero1 = float(input("ingrese el primer número \n"))
            numero2 = float(input("ingrese el segundo número \n"))
            resultado = numero1 + numero2
            print("resultado: " + str(resultado))
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return operadores ()
        elif (numeroO == 3):
            print("Número elevado al cuadrado.")
            numero = float(input("Ingrese el numero: \n \n"))
            resultado = numero**2
            print("La potencia es: " + str(resultado))
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return operadores ()
        elif (numeroO == 4):
            print("Conversion de Euros a Dolares \n")
            valor = float(input("ingrese el valor a convertir: \n \n"))
            euro = 1
            dolar = 1.06
            conversion = valor * dolar / euro
            print("El valor convertido es: " + str(conversion))
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return operadores ()
        elif (numeroO == 5):
            print("Calcular el area y perimetro de un cuadrado \n \n")
            lado = float(input("Ingrese el valor del lado del cuadrado: \n"))
            area = lado * lado
            print("El area del cuadrado es: " + str(area))
            perimetro = lado + lado + lado + lado
            print("El perimetro del cuadrado es: " + str(perimetro))
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return operadores ()
        elif (numeroO == 6):
            print(
                "Calcula el area y el volumen de un cilindro en centímetros \n \n")
            radio = float(input("Ingrese el valor del radio del cilindro: \n"))
            altura = float(input("Ingrese el valor de la altura del cilindro: \n"))
            pi = 3.141592
            area = 2 * pi * radio * altura + 2 * pi * radio**2
            volumen = pi * radio**2 * altura
            print("El area del cilindro en centímetros cuadrados es: " + str(area))
            print("El volumen del cilindro en centímetros cúbicos es: " +
                  str(volumen))
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return operadores ()
        elif (numeroO == 7):
            print("Calcula la longitud y area darea de una circunferencia en centímetros \n")
            radio = float(
                input("Ingrese el valor del radio de la circunferencia: \n"))
            pi = 3.141592
            longitud = 2 * pi * radio
            area = pi * radio**2
            print("La longitud de la circunferencia es: " + str(longitud))
            print("El area de la circunferencia es: " + str(area))
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return operadores ()
        elif (numeroO == 8):
            print("Calcular el promedio de tres números")
            numero1 = float(input("Ingrese el primer número: \n"))
            numero2 = float(input("ingrese ingrese el segundo número: \n"))
            numero3 = float(input("Ingrese el tercer número: \n"))
            promedio = numero1 + numero2 + numero3
            resultado = promedio / 3
            print("El promedio de los tres números es: " + str(resultado)) 
            print
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return operadores ()
    operadores ()
  def condicionales ():
    while True:
      print("Bienvenido a condicionales \n Menu \n  1) Saber si el número ingresado es positivo o negativo \n  2) Cual número es mayor y cual es menor \n  3) Numeros mayor y menor entre tres numeros dados \n  4) Si A es menor que B se suman, de lo contrario se restan \n  5) Cociente entre A y B \n  6) Sumar dos numeros A y B si alguno de ellos son negativos, de lo contrario se multiplican \n  7) Determinar si un año es bisiesto\n  99) Volver \n")
      number2 = int(input("Elija la opcion que quiere: "))
      os.system("clear")
      if (number2==99):
          return miselanea ()
          break
      elif (number2 == 1):
            print("¿El número es negativo o positivo? \n\nEscribe el número:")
            numero = int(input())
            if (numero > 0):
                print("El número es positivo ")
            elif (numero < 0):
                print("El número es negativo ")
            else:
                print("El número es igual a cero ")
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return condicionales ()
      elif (number2 == 2):
            print("¿Que número es menor y que número es mayor? \n")
            numeroUno = float(input("Escriba el primer número: \n"))
            numeroDos = float(input("Escriba el segundo número: \n"))
            if (numeroUno > numeroDos):
                print("El número mayor es: " + str(numeroUno))
                print("El número menor es: " + str(numeroDos))
            elif (numeroUno < numeroDos):
                print("El número mayor es: " + str(numeroDos))
                print("El número menor es: " + str(numeroUno))
            else:
                print("Ambos números son iguales ")
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return condicionales ()
      elif (number2 == 3):
            print(
                "Calcula el número mayor y el número menor entre tres numeros \n")
            numeroUno = float(input("Ingrese el primer número: \n"))
            numeroDos = float(input("Escriba el segundo número: \n"))
            numeroTres = float(input("Escriba el tercer número: \n"))
            thislist = [numeroUno, numeroDos, numeroTres]
            mayor = max(thislist)
            menor = min(thislist)
            print("El numero mayor es: " + str(mayor))
            print("El numero menor es: " + str(menor))
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return condicionales ()
      elif (number2 == 4):
            print("Si A es menor que B se suman, de lo contrario se restan \n \n")
            numeroUno = float(input("Ingrese el primer número; A: \n"))
            numeroDos = float(input("Ingrese el segundo número; B: \n"))
            if (numeroUno < numeroDos):
                suma = numeroUno + numeroDos
                print("La suma es: " + str(suma))
            elif (numeroUno > numeroDos):
                resta = numeroUno - numeroDos
                print("La resta es: " + str(resta))
            else:
                print("No se opera porque ambos números son iguales")
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return condicionales ()
      elif (number2 == 5):
            print("Calcula el cociente entre A y B \n")
            primerNumero = float(input("Ingrese el número A: \n"))
            segundoNumero = float(input("Ingrese el número B: \n"))
            if (segundoNumero == 0):
                print("La division por cero no es posible")
            elif (primerNumero > segundoNumero):
                division = primerNumero / segundoNumero
                print("Resultado de la división: " + str(division))
            elif (primerNumero < segundoNumero):
                cociente = primerNumero / segundoNumero
                print("El resultado de la división es : " + str(cociente))
            else:
                (primerNumero == segundoNumero)
                igualdad = primerNumero / segundoNumero
                print("El resultado de la división es: " + str(igualdad))
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return condicionales ()
      elif (number2 == 6):
            print("Dados dos numeros, A y B. Si alguno de ellos es negativo se suman, de lo contrario se multiplican \n")
            numeroUno = float(input("Ingrese el número A: \n"))
            numeroDos = float(input("Ingrese el número B: \n"))
            if (numeroUno >= 0) and (numeroDos >= 0):
                multiplication = numeroUno * numeroDos
                print("El resultado de la multiplicacion es: \n" +
                      str(multiplication))
            elif (numeroUno < 0) and (numeroDos >= 0):
                suma = numeroUno + numeroDos
                print("El resultado de la suma es: " + str(suma))
            elif (numeroUno >= 0) and (numeroDos < 0):
                suma = numeroUno + numeroDos
                print("El resultado de la suma es: " + str(suma))
            else:
                (numeroUno > 0) and (numeroDos < 0)
                suma = numeroUno + numeroDos
                print("El resultado de la suma es: " + str(suma))
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return condicionales ()
      elif (number2 == 7):
            print("Determinar si el año ingresado es bisiesto o no: \n")
            year = int(input("Ingrese el año: \n"))
            division = year / 4
            if (year % 4 == 0):
                print("El año SI es bisiesto")
            elif (year % 100 == 0):
                print("El año SI es bisiesto \n\n")
            else:
                print("El año NO es bisiesto \n\n")
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return condicionales ()
    condicionales ()
  def ciclos():
    while True:
        print("Bienvenido a ciclos \n Menu \n  1) Multiplos de 3 entre 1 - 100 \n  2) Numeros impares entre 0 - 100 \n  3) Numeros pares del 1 - 100 \n  4) Mostrar en pantalla los cuadrados de los numeros del 1 - 30 \n  5) Sumar los cuadrados de los 100 primeros numeros naturales y mostrar el resultado en pantalla \n  6) Dados dos numeros naturales, el primero menor que el segundo, mostar todos los numeros comprendidos entre ellos en secuencia acendente \n  7) Sumar todos los numeros que se digitan por teclado mientras que no sea cero \n  99) Volver \n")
        ciclo = int(input("Elija la opcion que quiere: ")) 
        os.system("clear")
        if (ciclo == 99):
          os.system("clear")
          return miselanea ()
          break 
        elif (ciclo == 1):
            print("Multiplos del número 3, entre 1 - 100")
            def multiplo(valor, multiplo):
              return True if valor % multiplo == 0 else False
            multipla = []
            for x in range(1, 101):
              if multiplo(x, 3):
                multipla.append(x)
            print("Los multiplos de 3 son:", multipla)
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return ciclos ()
        if (ciclo == 2):
            print("Numeros impares entre 0 - 100")
            numeros = []
            numero = 0
            while numero < 100:
              numero += 1
              if numero % 2 != 0:
                numeros.append(numero)
            print("Los numeros impares son: " + str(numeros))
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return ciclos ()
        if (ciclo == 3):
            print("Numeros pares del 1 - 100 son: ")
            print([i for i in range(1,101) if i%2==0])
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return ciclos ()
        elif (ciclo == 4):
            print("Cuadrados de los numeros del 1 - 30")
            def generarCuadrados(n):
              if 2 * n <= 30:
                cuadrados = [c**2 for c in range(1, 31)]
                return cuadrados[:n] + cuadrados[-n:]
              else:
                raise ValueError("n, no debe ser mayor a 2*n")
            resultado = generarCuadrados(15)
            print("Los cuadrados son:", resultado)
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return ciclos ()
        elif (ciclo == 5):
            print("Sumar los cuadrados de los 100 primeros numeros naturales y mostrar el resultado en pantalla. \nLos cuadrados son: \n")
            suma = 0
            for i in range(100):
                cuadrado = (i + 1) * (i + 1)
                suma = suma + cuadrado
                print(f"El cuadrado de {i+1} = {cuadrado}")
                print("La suma es: ", suma)
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return ciclos ()
        elif (ciclo == 6):
            print("Dados dos numeros naturales, el primero menor que el segundo, mostar todos los numeros comprendidos entre ellos en secuencia acendente")
            n1=int(input("Ingrese el primer numero: "))
            n2=int(input("Ingrese el segundo numero (mayor que el primero): "))
            if (n1==n2):
              print("ERROR... ambos numeros son iguales")
            elif n1<=n2:
              x = range(n1, n2)
              for numeros in x:
                print(numeros)
            else:
              (n1>=n2)
              print("ERROR... el segundo numero tiene que ser mayor que el primero")
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return ciclos ()
        elif (ciclo == 7):
            print("Sumar todos los numeros que se digitan por teclado mientras que no sea cero")
            condicion = True
            suma = 0
            while condicion:
                f = float(input("Digite un número: "))
                suma = suma + f
                print("La suma es: ", suma)
                if f == 0:
                    print("No se puede sumar el número cero (0)")
                    condicion = False
            d = input ("\n\n >> Presione cualquier tecla para voler <<")
            os.system("clear")
            return ciclos ()
    ciclos()
  def arreglos ():
    while True:
      print ("Bienvenido a arreglos \n Menu \n  1) Generar numeros aleatorios y ordenarlos con el metodo burbuja \n  2) Introducir 20 numeros enteros y ordenarlos al inverso \n  3) 10 Valores enteros ordenados en tres formas distintas \n  4) Encontrar el numero mayor y menor y su posicion original \n  5) Histograma de numeros \n  6) Introducir un numero y mostrar cuantas veces se repite en un arreglo \n  7) Mostrar 1 para los numeros primos y  0 para los que no son primos entre 8 numeros diferentes \n 99) Volver")
      arreglo=int(input("Ingrese una opcion: "))
      os.system("clear")
      if arreglo == 99:
        os.system("clear")
        return miselanea ()
        break 
      elif arreglo == 1:
        print ("Generar un rango de numeros aleatorios y organizarlos con el metodo burbuja")
        lista = []
        numeros = int (input("Ingrese el rango: "))
        for i in range (numeros):
          enteros = int(random.randint(-100, 100))
          lista.append(enteros)
        def metodoBurbuja(lista):
          listaEnteros = len(lista)
          for i in range (listaEnteros - 1):
            for n in range (0, listaEnteros - i -1):
              if lista [n] > lista [n + 1]:
                lista [n], lista [n + 1] = lista [n + 1], lista [n]
          return lista 
        print (metodoBurbuja(lista))
        h = input ("\nPresione cualquier tecla para voler")
        os.system("clear")
        return arreglos()
      elif arreglo == 2:
        print ("Elabore una aplicación que permita introducir 20 elementos de tipo entero en un arreglo, el programa mostrara impreso el arreglo en orden inverso.")
        lista = []
        print("Digite 20 numeros")
        valores = 20
        valorUno = 0 
        while valorUno < valores:
          print ("Ha digitado", (valorUno), "Elementos")
          enteros = int(input())
          lista.append (enteros)
          valorUno += 1
        lista.sort(reverse = True)
        print ('El orden de los elementos esta de mayor a menor', (lista))
        h = input ("\nPresione cualquier tecla para voler")
        os.system("clear")
        return arreglos()
      elif arreglo == 3:
        print ("Hacer un programa que lea diez valores enteros en un array y los muestre en pantalla. Después que los ordene de menor a mayor y los vuelva a mostrar. y finalmente que los ordene de mayor a menor y los muestre por tercera vez.")
        lista = []
        lista1 = []
        lista3 = []
        print ("Digite 10 numeros")
        valores = 10
        valor1 = 0
        while valor1 < valores:
          print ("Usted ha digitado", (valor1 + 1, "numeros"))
          enteros = int(input())
          lista.append(enteros)
          lista1.append(enteros)
          lista3.append(enteros)
          valor1 += 1
        lista.sort(reverse=True)
        lista1.sort()
        print(("Los numero que digito son"), str (lista3))
        str (lista3)
        print (("El orden de los numeros esta de menor a mayor"), str (lista1))
        print (("El orden de los numeros de mayor a menos es"), str (lista))
        h = input ("\nPresione cualquier tecla para voler")
        os.system("clear")
        return arreglos()
      elif arreglo == 4:
        print ("Elabore un programa que encuentre al número mayor y menor de un arreglo y luego muestre en qué posición se encontraban estos números originalmente.")
        arreglo = [12, 7, 82, 92, 62 , 1, 82, 0, 73, 73, 64, 45, 56,23,]
        for posicion in arreglo:
          maximo = max(arreglo)
          posicionmax = arreglo.index(maximo)
          menor = min(arreglo)
          posicionmin = arreglo.index(menor)
        print (f"El arreglo es: {arreglo}")
        print ("El valor maximo del arreglo es: ", str (maximo), "y la ubicacion dentro del arreglo es: ", str(posicionmax))
        print ("El valor minimo del arreglo es: ", str (menor), "y la ubicacion dentro del arreglo es: ", str (posicionmin))
        h = input ("\nPresione cualquier tecla para voler")
        os.system("clear")
        return arreglos()
      elif arreglo == 5:
        print ("5. elabore un programa que permita introducir un arreglo de 10 elementos, el programa mostrara un histograma de esos datos (el histograma se interpretara con la salida de n asteriscos donde n es el valor de cada elemento del arreglo) ej.: el arreglo es 2,3,4 el histograma será 2->** 3->*** 4->****")
        lista = []
        print ("Digite 10 numeros: ")
        valores = 10
        valor1 = 0
        while valor1 < valores:
          print ("Llevas digitando", (valor1 + 1), "numeros")
          enteros = int(input())
          lista.append (enteros)
          valor1 += 1
        caracter1 = []
        for i in lista:
          caracter = "*"
          a = (caracter * i)
          caracter1.append(a)
        for n,c in zip(lista, caracter1):
          print (str(n) + ":" + (c))
        h = input ("\nPresione cualquier tecla para voler")
        os.system("clear")
        return arreglos()
      elif arreglo == 6:
        print ("Elabore un programa que permita introducir un arreglo de 25 elementos de tipo entero. Luego pedir al usuario que introduzca un número. el programa mostrara el número de veces que se repite dicho valor en el arreglo")
        lista = []
        print ("Digite 25 numeros")
        valores = 25
        valor1 = 0 
        while valor1 <  valores:
          print ("llevas digitando ", str (valor1 + 1), "numeros")
          enteros = int(input())
          lista.append (enteros)
          valor1 += 1 
        print ("El arreglo que se digito fue: ", (lista))
        repetido = int (input("Digite un numero para saber cunatas veces se encuentra en el arreglo "))
        cantidad = lista.count(repetido)
        print ("La veces que el numero esta repetido son: ", (cantidad))
        h = input ("\nPresione cualquier tecla para voler")
        os.system("clear")
        return arreglos()
      elif arreglo == 7:
        print ("Elabore un programa que permita introducir un arreglo de 8 elementos de tipo entero. El programa mostrara un arreglo en donde muestre un 1 para los primos y un 0 para los no primos.")
        print ("Digite 8 numeros")
        valores = 8
        valor1 = 0
        impar = []
        par = []
        lista = []
        while valor1 < valores:
          print ("Lleva digitando", (valor1 + 1), "numeros")
          enteros = int(input())
          lista.append (enteros)
          valor1 += 1 
        for i in range (valores):
          if lista [i] % 2 == 0:
            par.append (lista[i])
          else:
            impar.append (lista[i])
        impar.sort ()
        par.sort ()
        print ("EL arreglo fue: " + str (lista), "Los numeros impares son: " + str (impar), "Los numeros pares son: " + str (par))
        h = input ("\nPresione cualquier tecla para voler")
        os.system("clear")
        return arreglos()
    arreglos ()
  if numero == 1:
    return operadores ()
  elif numero == 2:
    return condicionales ()
  elif numero == 3:
    return ciclos ()
  elif numero == 4:
    return arreglos ()
  elif numero == 00:
    os.system("clear")
    print ("*** PROGRAMA TERMINADO, BYEE! ***")
miselanea ()
    