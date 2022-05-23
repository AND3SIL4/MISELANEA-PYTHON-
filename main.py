print("MISELANEA EJERCICIOS PROGRAMACION PYTHON \n")
print("Menú: \n")
print("1) Operadores")
print("2) Condicionales")
print("3) Ciclos \n")
print("Ingrese la opcion que desee:")
numero = int(input())
print("---------------------------------------------------------------- \n")
if (numero == 1):
    print("Bienvenido a operadores \n")
    print("Menu \n")
    print("1) Calcular el area de un triangulo.")
    print("2) Suma de dos numeros.")
    print("3) Número elevado al cuadrado.")
    print("4) Convierta euros a dolares.")
    print("5) Valor del area y perimetro de un cuadrado")
    print("6) Area y volumen de un cilindro.")
    print("7) Longitud y area de un circulo.")
    print("8) Promedio de tres numeros.")
    print("99) Regresar. \n")
    numeroO = int(input("Ingrese la opcion que quiera: "))
    print("---------------------------------------------------------------\n")
    if (numeroO == 1):
        print("Calcular el area de un triangulo.")
        base = float(input("Ingrese el valor de la base del triangulo: \n"))
        altura = float(
            input("Ingrese el valor de la altura del triangulo: \n"))
        resultado = base * altura / 2
        print("El area es:" + str(resultado))
    elif (numeroO == 2):
        print("Suma de dos numeros \n")
        numero1 = float(input("ingrese el primer número \n"))
        numero2 = float(input("ingrese el segundo número \n"))
        resultado = numero1 + numero2
        print("resultado: " + str(resultado))
    elif (numeroO == 3):
        print("Número elevado al cuadrado.")
        numero = float(input("Ingrese el numero: \n \n"))
        resultado = numero**2
        print("La potencia es: " + str(resultado))
    elif (numeroO == 4):
        print("Conversion de Euros a Dolares \n")
        valor = float(input("ingrese el valor a convertir: \n \n"))
        euro = 1
        dolar = 1.06
        conversion = valor * dolar / euro
        print("El valor convertido es: " + str(conversion))
    elif (numeroO == 5):
        print("Calcular el area y perimetro de un cuadrado \n \n")
        lado = float(input("Ingrese el valor del lado del cuadrado: \n"))
        area = lado * lado
        print("El area del cuadrado es: " + str(area))
        perimetro = lado + lado + lado + lado
        print("El perimetro del cuadrado es: " + str(perimetro))
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
    elif (numeroO == 7):
        print(
            "Calcula la longitud y area darea de una circunferencia en centímetros \n"
        )
        radio = float(
            input("Ingrese el valor del radio de la circunferencia: \n"))
        pi = 3.141592
        longitud = 2 * pi * radio
        area = pi * radio**2
        print("La longitud de la circunferencia es: " + str(longitud))
        print("El area de la circunferencia es: " + str(area))
    elif (numeroO == 8):
        print("Calcular el promedio de tres números")
        numero1 = float(input("Ingrese el primer número: \n"))
        numero2 = float(input("ingrese ingrese el segundo número: \n"))
        numero3 = float(input("Ingrese el tercer número: \n"))
        promedio = numero1 + numero2 + numero3
        resultado = promedio / 3
        print("El promedio de los tres números es: " + str(resultado))
    else:
        (numeroO == 99)
if (numero == 2):
    print("Bienvenido a condicionales")
    print("Menu")
    print("1) Saber si el número ingresado es positivo o negativo")
    print("2) Cual número es mayor y cual es menor")
    print("3) Numeros mayor y menor entre tres numeros dados")
    print("4) Si A es menor que B se suman, de lo contrario se restan")
    print("5) Cociente entre A y B")
    print(
        "6) Sumar dos numeros A y B si alguno de ellos son negativos, de lo contrario se multiplican"
    )
    print("7) Determinar si un año es bisiesto")
    print("99) Devolverse")
    number = int(input("Elija la opcion que quiere: "))
    print("---------------------------------------------------------------\n")
    if (number == 1):
        print("¿El número es negativo o positivo? \n Escribe el número:")
        numero = int(input())
        if (numero > 0):
            print("El número es positivo ")
        elif (numero < 0):
            print("El número es negativo ")
        else:
            print("El número es igual a cero ")
    elif (number == 2):
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
    elif (number == 3):
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
    elif (number == 4):
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
    elif (number == 5):
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
    elif (number == 6):
        print(
            "Dados dos numeros, A y B. Si alguno de ellos es negativo se suman, de lo contrario se multiplican \n"
        )
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
    elif (number == 7):
        print("Determinar si el año ingresado es bisiesto o no: \n")
        year = int(input("Ingrese el año: \n"))
        division = year / 4
        if (year % 4 == 0):
            print("El año SI es bisiesto")
        elif (year % 100 == 0):
            print("El año SI es bisiesto \n\n")
        else:
            print("El año NO es bisiesto \n\n")
    else:
        (number == 99)

if (numero == 3):
    print("Bienvenido a ciclos")
    print("Menu")
    print("1) Multiplos de 3 entre 1 - 100")
    print("2) Numeros impares entre 0 - 100")
    print("3) Numeros pares del 1 - 100")
    print("4) Mostrar en pantalla los cuadrados de los numeros del 1 - 30")
    print(
        "5) Sumar los cuadrados de los 100 primeros numeros naturales y mostrar el resultado en pantalla"
    )
    print(
        "6) Dados dos numeros naturales, el primero menor que el segundo, mostar todos los numeros comprendidos entre ellos en secuencia acendente"
    )
    print(
        "7) Sumar todos los numeros que se digitan por teclado mientras que no sea cero"
    )
    print("99) Volver")
    ciclo = int(input("Elija la opcion que quiere: "))
    print("----------------------------------------------------------------\n")
    if (ciclo == 1):
        print("Multiplos del número 3, entre 1 - 100")
        def multiplo(valor, multiplo):
          return True if valor % multiplo == 0 else False
        multipla = []
        for x in range(1, 101):
          if multiplo(x, 3):
            multipla.append(x)
        print("Los multiplos de 3 son:", multipla)
    if (ciclo == 2):
        print("Numeros impares entre 0 - 100")
        numeros = []
        numero = 0
        while numero < 100:
          numero += 1
          if numero % 2 != 0:
            numeros.append(numero)
        print("Los numeros impares son: " + str(numeros))
    if (ciclo == 3):
        print("Numeros pares del 1 - 100 son: ")
        print([i for i in range(1,101) if i%2==0])
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
    elif (ciclo == 5):
        print("Sumar los cuadrados de los 100 primeros numeros naturales y mostrar el resultado en pantalla. \nLos cuadrados son: \n")
        suma = 0
        for i in range(100):
            cuadrado = (i + 1) * (i + 1)
            suma = suma + cuadrado
            print(f"El cuadrado de {i+1} = {cuadrado}")
            print("La suma es: ", suma)
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
    elif (ciclo == 7):
        print(
            "Sumar todos los numeros que se digitan por teclado mientras que no sea cero"
        )
        condicion = True
        suma = 0
        while condicion:
            f = float(input("Digite un número: "))
            suma = suma + f
            print("La suma es: ", suma)
            if f == 0:
                print("No se puede sumar el número cero (0)")
                condicion = False
            else:
              print("99) Volver")
