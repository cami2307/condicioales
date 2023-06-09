#video numero 1 creación del primer print

print("Hola mundo ")

#video 2 creación de variables

num1 = 4 #datos numéricos
print(num1)
print(type(num1))

num2 = 6.5
print(float(num2))

#las cadenas se pueden asignar con comillas dobles o sencillas

cadena = "camila"; 'alape'
print(cadena)

#se pueden utilizar ambas comillas en una sola cadena 

cad = "estoy'estudiando'"
print(cad)

# tambien se pueden hacer bulianos

valor = True 
print(valor)

valor2 = False
print (valor2)

#se puenden asignar variables para que contengan numeros como tambien se pueden hacer cualquier tipo de operaciones tambien se pueden poner mas numeros aparte de las variables

num1 = 5
num2 = 2.6

resul= num1*num2 //10 **4

print("el resultado es: ",resul) 

# video de operadores aritmeticos se pueden hacer en dos formas directos o en variables 

resultado = 10+5
print(resultado)

nu1=7
nu2=8
res= nu1 * nu2
print(res)

resu= nu1 - nu2
print(resu)
# hay dos tipos de divisiones la entras q son con "//" y las normales q son con "/"
result= nu1 / nu2 
print (result)

resulta= nu1 // nu2
print(resulta)

# siempre se resuelve de adentro hacia fuera es decir que cumplen las mismas reglas q las matematicas

resultado1 = 3**3 * (13/5 - (2*4))
print(resultado1)

# video operadores relacionales

resultado = 10 < 20
print(resultado)

resultado = 10 > 20
print(resultado)

resultado = 10==20
print(resultado)

resultado= 10 != 20
print(resultado)

resultado = 10 <= 10 
print(resultado)          

resultando = 10>=20
print(resultado)

a = 10
b = 20
c = 30
resultado = a+b == c
print(resultado)

# video operadores logicos and(conjuncion), or(disyunción) y not (negación)

a = 10
b = 12
c = 13;

resultado = ((a>b)or(a<c))and((a==c)or(a>=b))
print(resultado)

#video operadores de asignación ayudan a ahorrar codigo y tambiem ayuda a que el codigo se vea mejor antes de hacer estas operaciones debemos crear la variable 

a = 0

a += 5 # suma en asignacion
a -= 2 # resta en asignacion
a *= 3 # multiplicación en asignación
a /= 6 # división en asignación
a **= 4 # potencia en asignación
a %= 2 # modulo en asignacion

print(a)

# video de salidas de datos por consola

nombre = "camila"
edad = 17
print(" hola soy ",nombre,'tengo',edad,"años")

#segunda forma 
print(f"hola {nombre} tengo {edad} años")
#tercera forma 
print("hola {} tengo {} años".format(nombre,edad))

# video entrada de datos deja tambien digitar con espacios 
#tipo cadena
nombre = input("digite su nombre: ")
print(f"hola {nombre}") # el input guarda solo guarda tipo cadena 

# numeros 
numero = int(input("digite un numero"))
print(f"el numero es {numero + 1}") # el int es para solo numeros enteros 

número = float(input("digite un numero"))
print(f"el numero es {numero}")#el float es para numeros decimales 

# video funciones integradas 

n = int("10")
print(n)

n = float("20")
print(n)

n = str(45)
print(n)# sirve tambien con los numeros flotantes o decimales

n = bin(4)
print(n)# bin es para valores binarios

n = hex(6)
print(n)#hex es para hexadecimal

n = int("0b1010",2)
print(n)# pasar de binario a entero

n = int(" 0xa",16)
print(n)#pasar de hexadecimal a entero

n = abs(-8)# abs es valor absoluta
print(n)

n = round(5.6)#round es para redondear
print(n)

n = len("camila")# len cuenta cuantos caracteres tiene la cadena 
print(n)

#videos capitulo 1 elementos basicos ejercicio 1

a = float(input("a--> "))
b = float(input("b--> "))
c = float(input("c--> "))

resultado = (a*3 * (b*2 - 2*a*c))/(2*b)
print(f"el resultado es: {resultado}")

#ejercicio 2

a = float(input("a --> "))
b = float(input("b --> "))
c = float(input("c --> "))
d = float(input("d --> "))
e = float(input("e --> "))

resultado = ((a+b*c)<a and ((d/a*e)+2<2) or (a>b))

print("el resultado es: {resultado}")


#ejercicio 3 intercambiar el valor de 2 variables 

a = input("a --> ")
b = input("b --> ")

a , b = b , a 

print(f"el nuevo valor de a es: {a}")
print(f"el nuevo valor de b es: {b}")

#ejercicio 4 hacer un programa para ingresar el radio de un circulo y se repirte su area y la longitud de la circunferencia

import math 

radio = float(input("radio --> "))

area = math.pi * radio**2
longitud = 2 * math.pi * radio

print(f"el area es: {area:.2f}")
print(f"la longitud de la circunferencia es: {longitud:.2f}")#.numerof es para solo controlar cuantos decimales 

#ejercicio 5 una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto debera pagar finalmente por su compra

precio = float(input("digite el precio del producto comprado: "))

descuento = precio * 0.15
precioFinal = precio - descuento 

print(f"el precio final a pagar es de €{precioFinal:.2f}")

#condicionales capitulo 1 son para comparar dos valores esa comparación da un valor ya sea verdadero o falso 

numero = int(input("digite un numero: "))

if numero >0:
    print("el numero es positivo")
elif numero == 0:
    print("el numero es cero")
else:
    print("el numero es negativo")

# condicionales combinados capitulo 2

edad = int(input("digite su edad: "))

if edad >0 and edad <100:
    print("edad correcta")
    if edad >=18:
        print("es mayor de edad")
else:
    print("edad incorrecta")

#ejercicio 2 de condicionales: pida 2 numeros y se de cuenta cual de ellos es par o si ambos lo son 

num1 = int(input("digite un numero: "))
num2 = int(input("digite otro numero: "))

if num1%2==0 and num2%2==0:
    print("ambos numeros son pares")
elif num1%2==0 and num2%2!=0:
    print(f"{num1} es par")
elif num1%2!=0 and num2%2==0:
    print(f"{num2} es par")
else:
    print("ambos numeros son impares")

#ejercicio 3: hacer un programa que pida 3 numeros y determine cual es el mayor 

num1 = int(input("digite un numero: "))
num2 = int(input("digite otro numero: "))
num3 =int(input("digite otro numero: "))

if num1>=num2 and num1>=num3:
    print(f"el numero mayor es {num1}")
elif num2>=num1 and num2>=num3:
    print(f"el numero mayor es {num2}")
elif num3>=num1 and num3>=num2:
    print("el numero mayor es {num3}")

#ejercicio 4: hacer un programa qie pida un caracter e indique si es una vocal o no

letra = input("digite un caracter: ").lower()

if letra =='a'or letra=='i'or letra=='o'or letra=='u':

    print("es una vocal")
else:
    print("no es una vocal")

#ejercicio 5: funcionamiento de calculadora

a=float(input("digite un numero: "))
b=float(input("digite otro numero: "))

operacion= input("digite la operacion: ").upper()


if operacion=='S':
    suma=a+b
    print(f"\n la suma es: {suma}")
elif operacion == 'R':
    resta=a-b         
    print(f"\n la resta es: {resta}")
elif operacion == 'M' or operacion=='P':
    mult=a*b
    print(f"\n la multiplicación es: {mult}")
elif operacion =='D':
    Div=a/b
    print(f"\n la division es: {Div:.2f}")
else:
    print("\n se equivoco de operacion")