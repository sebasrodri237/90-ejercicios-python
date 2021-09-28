# /////////////////////////////////////////////////////// LA GRANJA ///////////////////////////////////////////////////////////////////////
#1- Litros de leche que se producen en la granja
def litrosLeche(n,Numlitros):

    return n*Numlitros

largo = int(input("Digite el largo del corral: "))
litros = float(input("Digite el numero de litros de leche que produce una vaca: "))

print("La cantidad de litros de leche que se producen en la granja es de:",litrosLeche(largo,ancho,litros))

#2- Cantidad de huevos de gallina al mes en la granja
def numeroHuevos(NumAves):

    DIAS = 30

    return ((NumAves/3)/2)*((DIAS/3) + (DIAS/5))

aves = int(input("Digite el numero de aves en la granja: "))

print("La cantidad de huevos que producen las gallinas al mes en la granja es de:",numeroHuevos(aves))

#3- Cantidad en kilos de escorpiones que se pueden vender sin que decrezca la población
def numEscorpionesVenta(pequeños,medianos,grandes):

    tercioP = int((pequeños+medianos+grandes)/3)
    totalk = 0

    while(tercioP>0):
        if grandes > 0:
            tercioP = tercioP - 1
            grandes = grandes - 1
            totalk = totalk + 50
        elif(grandes == 0 and medianos>0):
            tercioP = tercioP - 1
            medianos = medianos - 1
            totalk = totalk + 30
        elif(grandes == 0 and medianos == 0 and pequeños>0):
            tercioP = tercioP - 1
            pequeños = pequeños - 1
            totalk = totalk + 20
    return int(totalk/1000)

escorPeq = int(input("Digite el numero de escorpiones pequeños en la granja: "))
escorMed = int(input("Digite el numero de escorpiones medianos en la granja: "))
escorGran = int(input("Digite el numero de escorpiones grandes en la granja: "))

print("Los kilos de escorpiones que se pueden vender sin reducir son:",numEscorpionesVenta(escorPeq,escorMed,escorGran),"kg")

#4- Material para cerramiento del corral más económico(con tablas, varilla o alambre)
def cerramientoEco(n,m,p,q,s):

    totalM = n*p*4*2 + m*p*4*2
    totalV = n*q*8*2 + m*q*8*2
    totalA = n*s*5*2 + m*s*5*2
    
    if(totalM) < (totalV) and (totalM) < (totalA):
        return "tablas de madera"
    elif(totalV) < (totalM) and (totalV) < (totalA):
        return "varilla"
    elif(totalA) < (totalM) and (totalA) < (totalV):
        return "alambre"

largo = int(input("Digite el largo del corral: "))
ancho = int(input("Digite el ancho del corral: "))  
metroTablas = int(input("Digite el precio por metro de tablas de madera: "))
metroVarillas = int(input("Digite el precio por metro de varillas: "))  
metroAlambre = int(input("Digite el precio por metro de alambre: "))

print("El cerramiento mas económico es con: ",cerramientoEco(largo,ancho,metroTablas,metroVarillas,metroAlambre))
# /////////////////////////////////////////////////////// LA GRANJA ///////////////////////////////////////////////////////////////////////

# /////////////////////////////////////////////////////// Numéricos ///////////////////////////////////////////////////////////////////////

#5- Función potencia de un entero elevado a un entero.
def potencia(base,exponente):

    return base**(exponente)

base = int(input("Digite la base: "))
exp = int(input("Digite el exponente: "))

print("El resultado de la función potencia es:", potencia(base,exp))

#6- Función que determina si un número es divisible por otro.
def divisible(dividendo,divisor):

    if dividendo % divisor == 0:
        return True
    else:     
        return False
divid = int(input("Digite el dividendo: "))
divis = int(input("Digite el divisor: "))

print("El numero es divisible por otro:",divisible(divid,divis))

#7- Determinar si un número es primo.
def primo(numero):

    if numero == 1:
        return False
    elif numero == 2:
        return True
    else:
        n = 2
        flag = True
        while(n <= numero-1 and flag):
            if numero % n == 0:
                flag = False
                return False
            else:
                n = n+1
        return True
    
num = int(input("Digite un número natural: "))

print("El numero es primo:",primo(num))

#8- Dados dos naturales, determinar si son primos relativos.
def primoRelativo(numero1,numero2):

    n = 2
    flag = True
    while((n <= numero1 or n <= numero2) and flag):
        if numero1 % n == 0 and numero2 % n == 0:
            flag = False
            return False
        else:
            n = n+1
    return True
    
num1 = int(input("Digite el primer número natural: "))
num2 = int(input("Digite el segundo número natural: "))

print("Los numeros son primos relativos:",primoRelativo(num1,num2))

#9- Determinar si un número es múltiplo de la suma de otros dos números.
def multiplo(numero1,numero2,numeroMultiplo):

    if numeroMultiplo %  (numero1+numero2) == 0:
        return True
    else:
        return False

num1 = float(input("Digite el primer numero a sumar: "))
num2 = float(input("Digite el segundo numero a sumar: "))
numMul = float(input("Digite el numero a verificar si es multiplo de la suma anterior: "))

print("El numero es multiplo de la suma de los numeros:",multiplo(num1,num2,numMul))

#10- Dados los coeficientes de un polinomio de grado dos, evaluar el polinomio en un valor dado.
def polGrado2(coefCuadratico,coefLineal,termInd,k):

    return (coefCuadratico*(k*k) + coefLineal*k + termInd)

a2= float(input("Digite el valor del coeficiente cuadratico (distinto de 0): "))
a1 = float(input("Digite el valor del coeficiente lineal: "))
a0 = float(input("Digite el valor del termino independiente: "))
k = float(input("Digite el valor x para evaluar el polinomio: "))

print("El resultado de evaluar el polinomio",a2,"*x^2 +",a1,"*x +",a0,"en x=",k,"es:",polGrado2(a2,a1,a0,k))

#11- Dados los coeficientes de un polinomio de grado dos, calcular coeficiente lineal de la derivada.
def coeflin(coefCuadratico,coefLineal,termInd):

    return (2*coefCuadratico)

a2= float(input("Digite el valor del coeficiente cuadratico (distinto de 0): "))
a1 = float(input("Digite el valor del coeficiente lineal: "))
a0 = float(input("Digite el valor del termino independiente: "))

print("El coeficiente lineal de la derivada del polinomio",a2,"*x^2 +",a1,"*x +",a0,"es:",coeflin(a2,a1,a0))

#12- Dados los coeficientes de un polinomio de grado dos y un número real, evaluar la derivada del polinomio en ese número.
def deriPolGrado2(coefCuadratico,coefLineal,termInd,k):

    return ((2*coefCuadratico)*k + coefLineal)

a2= float(input("Digite el valor del coeficiente cuadratico (distinto de 0): "))
a1 = float(input("Digite el valor del coeficiente lineal: "))
a0 = float(input("Digite el valor del termino independiente: "))
k = float(input("Digite el valor x para evaluar el polinomio: "))

print("El resultado de evaluar la derivada del polinomio",a2,"*x^2 +",a1,"*x +",a0,"en x=",k,"es:",deriPolGrado2(a2,a1,a0,k))

#13- Dado un natural, determinar si es un número de Fibonacci o no.
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def numFibonacci(num):
    
    i = 0
    flag = True
    
    while (i<num and flag):
        print(fibonacci(i))
        if num == fibonacci(i+1):
            flag: False
            return True
        
        else:
            i = i+1
    return False           

num = int(input("Digite un número natural: "))

print("El número es de Fibonacci:",numFibonacci(num))

# /////////////////////////////////////////////////////// Fin Numéricos ///////////////////////////////////////////////////////////////////////

# /////////////////////////////////////////////////////// Geométricos ///////////////////////////////////////////////////////////////////////

# 14- Dadas la pendiente y el punto de corte de dos rectas, determinar si son paralelas, perpendiculares o ninguna de las anteriores.
def relacionRectas(m1,m2,pcUno,pcDos):

    if(m1 == m2 and pcUno != pcDos):
        return "son paralelas"
    
    elif m1*m2 == -1:
        return "son perpendiculares"
    
    else:
        return "no son paralelas ni perpendiculares"    

m1 = float(input("Ingrese la pendiente de la recta 1: "))
m2 = float(input("Ingrese la pendiente de la recta 2: "))
pcUno = float(input("Ingrese la coordenada del punto de corte con respecto al eje y de la recta 1 : "))
pcDos = float(input("Ingrese la coordenada del punto de corte con respecto al eje y de la recta 2 : "))

print("Las rectas",relacionRectas(m1,m2,pcUno,pcDos))

# 15- Dadas la pendiente y el punto de corte de dos rectas, determinar los puntos de intersección al origen (ordenada y abscisa).
def interseccionOrigen(m,puntoC):

    return "0,"+str(puntoC),str((-puntoC)/m)+",0"    

m1 = float(input("Ingrese la pendiente de la recta 1: "))
m2 = float(input("Ingrese la pendiente de la recta 2: "))
pcUno = float(input("Ingrese la coordenada del punto de corte con respecto al eje y de la recta 1 : "))
pcDos = float(input("Ingrese la coordenada del punto de corte con respecto al eje y de la recta 2 : "))

print("De la recta 1, la ordenada y abscisa son respectivamente :",interseccionOrigen(m1,pcUno),"y de la recta 2, la ordenada y abscisa son respectivamente :",interseccionOrigen(m2,pcDos))

#16- Dado el radio de un círculo, calcular el área del triángulo que circunscribe el circulo (triángulo afuera).
def areaTri(radio,perim):

    return (1/2)*radio*perim

radio = float(input("Ingrese el radio de la circunferencia inscrita en el triángulo: "))
perimetro=float(input("Ingrese el perimetro del triángulo que circunscribe la circunferencia: "))

print("El área del triangulo que circunscribe a la circunferencia de radio",radio,"es:",areaTri(radio,perimetro))

#17- Dado el radio de un círculo, calcular el  ́area y perímetro del cuadrado, pentágono 
#y hexágono adentro (inscrito en un círculo) y afuera (inscribiendo al círculo).
def areaYPerimInscrito(radio,figura):
   
    CONSTCUADRADO = 2**(1/2)
    CONSTPENTAGONO = (10+2*(5**(1/2)))**(1/2)
    CONSTHEXAGONO = 3**(1/3)

    if figura == "cuadrado":

       return ((2*radio)/(CONSTCUADRADO))**2,((2*radio)/(CONSTCUADRADO))*4
    if figura == "pentagono":

       return (5*(radio**2)*CONSTPENTAGONO)/8,(5*radio*CONSTPENTAGONO)/2
    if figura == "hexagono":

       return (6*radio),(3*(radio**2)*CONSTHEXAGONO)/2

def areaYPerimInscribiendo(radio,figura):

    CONSTPENTAGONOAREA = 1.72048
    CONSTPENTAGONO = (1+(2/(5**(1/2))))**(1/2)
    CONSTHEXAGONO = 3**(1/2)

    if figura == "cuadrado":

       return (2*radio)**2,(2*radio)*4
    if figura == "pentagono":

       return CONSTPENTAGONOAREA*((2*radio)/CONSTPENTAGONO)**2,(2*radio*5)/CONSTPENTAGONO
    if figura == "hexagono":

       return (6*2*radio*CONSTHEXAGONO)/3,2*(radio**2)*CONSTHEXAGONO

radio = float(input("Ingrese el radio de la circunferencia: "))
figura = input("Digite el nombre de la figura inscrita o que inscribe a la circunferenia sin tildes(cuadrado, pentagono o hexagono): ")

print("El área y perímetro del",figura,"inscrito en la circunferencia son respectivamente: ",areaYPerimInscrito(radio,figura))
print("El área y perímetro del",figura,"que circunscribe a la circunferencia son respectivamente: ",areaYPerimInscribiendo(radio,figura))

#18 - Cantidad de telaraña que requiere la araña para su telaraña de pi*r^2.
def cantidadTelaraña(r):

    if r == 0:
        return 0
    
    elif r == 1:
        return 6
    
    else:
        return 6*r + cantidadTelaraña(r-1)

radio = int(input("Ingrese el valor del radio de la telaraña de pi*r^2: "))
print("La telaraña total que requiere la araña para su telaraña es de",cantidadTelaraña(radio))
# /////////////////////////////////////////////////////// Fin Geométricos ///////////////////////////////////////////////////////////////////////

# /////////////////////////////////////////////////////// Varios ///////////////////////////////////////////////////////////////////////
#19- Arboles a podar para obtener T hojas.
def podarArboles(t,p,k):

    return (t/p)/k

hojas = int(input("Digite la cantidad de hojas a podar: "))
hojasRama = int(input("Digite cuantas hojas tiene una rama: "))
ramas = int(input("Digite la cantidad de ramas podadas: "))

print("Se deben podar",podarArboles(hojas,hojasRama,ramas),"arboles")

#20- Pago dinero con interes simple y compuesto.
def pagoIntSim(k,i):

    DIAS = 7
    return k*(1+((DIAS/360)*(i/100)))

def pagoIntComp(k,i):

    DIAS = 7
    return k*(1+(i/100))**DIAS

dineroPres = int(input("Digite la cantidad de dinero prestada: "))
interesDia = int(input("Digite el interes diario: "))

print("El dinero a pagar luego de una semana (7 días) con interes simple es de",pagoIntSim(dineroPres,interesDia),"y con interes compuesto es de",pagoIntComp(dineroPres,interesDia))

#21.1- Formas distintas de ubicar fichas rojas(1x1), azules(1x2) de lego sobre base de 1xn.
def numUbicaciones(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return numUbicaciones(n-1) + numUbicaciones(n-2)

nDeBase = int(input("Digite la dimensión n de la base: "))

print("Existen aproximadamente",numUbicaciones(nDeBase),",formas de ubicar las fichas rojas y azules")

#21.2- Formas distintas de ubicar fichas rojas(1x1), azules(1x2) y amarillas(1x3) de lego sobre base de 1xn. Se debe correr el codigo junto a las
#funciones factorial y combinatoria.
def numUbicacionesDos(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return numUbicacionesDos(n-1) + numUbicacionesDos(n-2) + numUbicacionesDos(n-3)

nDeBase = int(input("Digite la dimensión n de la base: "))

print("Existen aproximadamente",numUbicacionesDos(nDeBase),",formas de ubicar las fichas rojas, azules y amarillas")
# /////////////////////////////////////////////////////// Fin Varios ///////////////////////////////////////////////////////////////////////

# /////////////////////////////////////////////////////// Arreglos ///////////////////////////////////////////////////////////////////////
#22-Implementar la criba de Eratostenes para calcular los números primos en el rango 1 a n, donde n es un número natural dado por el usuario.
def cribaErastones(n):

    listaCriba = [False,False]
    for x in range(2,n+1):
        listaCriba.append(True)

    for x in range(2,n+1):
        if x^2 < n:
            for y in range(2,n+1):
                if y%x == 0 and y!=x:
                    listaCriba[y] = False

    return listaCriba

num = int(input("Digite un número natural n, para calcular los números primos desde 1 a n (criba de Erastones): "))
print("La criba de Eratostenes es",cribaErastones(num))

#23- Desarrollar un algoritmo que calcule la suma de los elementos de un arreglo de números reales/naturales.
#Función para calcular la suma de los elementos de un arreglo
def sumTotal(arreglo):
    
    sumtotal = 0
    for i in arreglo:
        sumtotal = sumtotal + i
    return sumtotal

#/////Arreglo de prueba///
v = [2,5.3,3,8.8,5]

print("La suma de los elementos del arreglo es",sumTotal(v))

#24- Desarrollar un algoritmo que calcule el promedio de un arreglo de números reales/naturales.
#Función para calcular el promedio de un arreglo
def promedio(arreglo):
    
    sumtotal = 0
    cont = 0
    for i in arreglo:
        sumtotal = sumtotal + i
        cont = cont +1
    return float(sumtotal/cont) #promedio

#Promedio Naturales
def promedioN(arreglo):
    
    sumtotal = 0
    cont = 0
    for i in arreglo:
        sumtotal = sumtotal + i
        cont = cont +1
    return int(sumtotal/cont) #promedio
#/////Arreglo de prueba///
v = [2,5.3,3,8.8,5]

print("El promedio de los elementos del arreglo es",promedio(v))

#25- Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números reales/naturales de igual tamaño.
def productoPunto(v,w):

    result = 0
    for i in range(0,len(v)):
        result = result + (v[i]*w[i])
    return result
#Ejemplo de arreglos de números reales
v = [2,5.3,3,8.8,5]
w = [2.3,-6,8.9,1.1,2]

print(productoPunto(v,w))

#26- Desarrollar un algoritmo que calcule el mínimo de un arreglo de números reales/naturales.
def minimo(arreglo):

    print(arreglo)
    minimo = arreglo[0]
    for i in range(0,len(arreglo)-1):
        if minimo > arreglo[i+1]:
            minimo = arreglo[i+1]    
    return minimo

#/////Arreglo de prueba///
v = [2,5.3,3,8.8,5]
print("El mínimo del arreglo es",minimo(v))

#27- Desarrollar un algoritmo que calcule el máximo de un arreglo de números reales/naturales.
def maximo(arreglo):

    maximo = arreglo[0]
    for i in range(0,len(arreglo)-1):
        if maximo < arreglo[i+1]:
            maximo = arreglo[i+1]
    return maximo

#/////Arreglo de prueba///
v = [2,5.3,3,8.8,5]
print("El maximo del arreglo es",maximo(v))

#28- Desarrollar un algoritmo que calcule el producto directo de dos arreglos de números reales/naturales de igual tamaño.
def productoDirecto(v,w):

    productoD = []
    for i in range(0,len(v)):
        productoD.append(v[i]*w[i])
    return productoD
#Ejemplo de arreglos de números reales
v = [2,5.3,3,8.8,5]
w = [2.3,-6,8.9,1.1,2]

print(productoDirecto(v,w))

#29- Desarrollar un algoritmo que determine la mediana de un arreglo de números reales/naturales. La mediana es el número que queda 
#en la mitad del arreglo después de ser ordenado.
def mediana(arreglo):

    arreglo = sorted(arreglo)

    if len(arreglo)%2 == 0:
        
        return (arreglo[int(len(arreglo)/2)-1] + arreglo[int(len(arreglo)/2)])/2
    else:
        return arreglo[int((len(arreglo)-1)/2)]
v = [5,3,-1,2.4,8,9.6,4.2,7,1.1]

# Mediana Naturales

def medianaN(arreglo):

    arreglo = sorted(arreglo)

    if len(arreglo)%2 == 0:
        
        return int((arreglo[int(len(arreglo)/2)-1] + arreglo[int(len(arreglo)/2)])/2)
    else:
        return arreglo[int((len(arreglo)-1)/2)]

print(mediana(v))

#30- Hacer un algoritmo que deje al final de un arreglo de números reales/naturales, todos los ceros que aparezcan en dicho arreglo.
def corrimientoIzq(pos,arreglo):
    for j in range(pos,len(arreglo)-1):
        arreglo[j] = arreglo[j+1]
def reemplazarPorCeros(num,arreglo): 
    for k in range(len(arreglo)-num,len(arreglo)):
        arreglo[k] = 0

    return arreglo
def cerosUltimo(arreglo):

    cont = 0
    for i in range(0,len(arreglo)):
        if arreglo[i] == 0:
            cont = cont + 1
            corrimientoIzq(i,arreglo)

    return reemplazarPorCeros(cont,arreglo)

v = [5,0,6,0,3.1,-1,0,80,1]
print(cerosUltimo(v))

#31- Hacer un algoritmo que calcule los números en decimal que representa dicho arreglo de unos y ceros.
def binarioADecimal(arreglo):

  decimal = 0
  for i in range(0,len(arreglo)):
    if arreglo[i] == 1:
      decimal = decimal + 2**(i)
  return decimal

v = [1,0,0,1,0,1,1,1,1]

print(binarioADecimal(v))

#32- Hacer un algoritmo que dado un número entero no negativo, cree un arreglo de unos y ceros que representa 
#el número en binario al revés.
def decimalABinario(decimal):

  binario = []

  while(decimal // 2 != 0):
    binario.append(decimal % 2)
    decimal = decimal // 2
  
  binario.append(decimal)  

  return binario

print(decimalABinario(106))

#33- Hacer un algoritmo que calcule el Máximo Común Divisor (MCD) para un arreglo de enteros positivos.
def mcd(x,y):
  if y == 0: 
    return x
  return mcd(y, x%y)
def calcularmcd(array):

  mcdValor = 0
  for i in range(0,len(array)):
    if i == 0:
      mcdValor = mcd(array[i],array[i+1])
    elif i >=2:
      mcdValor = mcd(mcdValor,array[i])

  return mcdValor

w = [12,20,14,124,72,2458]

print(calcularmcd(w))

#34- Hacer un algoritmo que calcule el Mínimo Común Múltiplo (MCM) para un arreglo de entero positivos.
def mcd(x,y):
  if y == 0: 
    return x
  return mcd(y, x%y)

def calcularmcm(array):

  mcmValor = 0
  multiplicar = 0
  total = 0
  for i in range(0,len(array)):
    if i == 0:
      mcmValor = mcd(array[i],array[i+1])
      multiplicar = array[i]*array[i+1]
      total = multiplicar/mcmValor
    elif i >=2:
      mcmValor = mcd(total,array[i])
      multiplicar = total*array[i]
      total = multiplicar/mcmValor

  return total

v = [12,20,30,15]

print(calcularmcm(v))
# /////////////////////////////////////////////////////// Fin Arreglos ///////////////////////////////////////////////////////////////////////

# /////////////////////////////////////////////////////// CONJUNTOS COMO ARREGLOS ///////////////////////////////////////////////////////////////////////
def llenarArreglo(largoArr):

  v = [0]*largoArr
  for i in range(0,largoArr):
    v[i] = float(input("Ingrese un elemento del arreglo:"))
  return v

def imprimirMenu():
    print("//////////////////////////////////////////////")
    print("///////////////Menú Principal////////////////////")
    print("1. Unión")
    print("2. Intersección")
    print("3. Diferencia")
    print("4. Diferencia Simetrica")
    print("5. Pertenece")
    print("6. Contenido")
    print("7. Salir")

print("//////////////////////////////////////////////")
print("///////////////Menú Principal////////////////////")
print("1. Unión")
print("2. Intersección")
print("3. Diferencia")
print("4. Diferencia Simetrica")
print("5. Pertenece")
print("6. Contenido")
print("7. Salir")

nA1 = int(input("Ingrese el tamaño del arreglo 1: "))
v = llenarArreglo(nA1)
nA2 = int(input("Ingrese el tamaño del arreglo 2: "))
w = llenarArreglo(nA2)

# y = [9,2,5,7,1,8,22]
# z = [7,1,9,2,0]

opcion = int(input("Ingrese una opción: "))
while opcion > 0 and opcion <= 6:
    if opcion == 1:
        #35- Calcula en un arreglo la unión de los conjuntos y la imprime.
        def quitarRep(conjunto):

            conjuntoSinRep = []

            for i in range(0,len(conjunto)-1):
                if conjunto[i] != conjunto[i+1]:
                    conjuntoSinRep.append(conjunto[i])

            return conjuntoSinRep
        
        def union(conjuntoUno,conjuntoDos):

            return quitarRep(conjuntoUno+conjuntoDos)


        print(union(v,w))
        imprimirMenu()
        opcion = int(input("Ingrese una opción: "))
    if opcion == 2:
        #36- Calcula en un arreglo la intersección de los conjuntos y la imprime.
        def interseccion(conjuntoUno,conjuntoDos):

            conjuntoInter = []
            for i in range(0,len(conjuntoUno)):
                for j in range(0,len(conjuntoDos)):
                    if conjuntoUno[i] == conjuntoDos[j]:
                        conjuntoInter.append(conjuntoUno[i])

            return conjuntoInter

        print(interseccion(v,w))
        imprimirMenu()
        opcion = int(input("Ingrese una opción: "))
    if opcion == 3:
        #37- Calcula en un arreglo la diferencia del primero con el segundo y la imprime.
        def diferencia(conjuntoUno,conjuntoDos):

            conjuntoDif = []
            flag = False
            for i in range(0,len(conjuntoUno)):
                for j in range(0,len(conjuntoDos)):
                    if conjuntoUno[i] == conjuntoDos[j]:
                        flag = True

                if flag == False:
                    conjuntoDif.append(conjuntoUno[i])
                else:
                    flag = False

            return conjuntoDif

        print(diferencia(v,w))
        imprimirMenu()
        opcion = int(input("Ingrese una opción: "))
    if opcion == 4:
        #38- Calcula en un arreglo la diferencia simetrica de los conjuntos y la imprime.
        def diferencia(conjuntoUno,conjuntoDos):

            conjuntoDif = []
            flag = False
            for i in range(0,len(conjuntoUno)):
                for j in range(0,len(conjuntoDos)):
                    if conjuntoUno[i] == conjuntoDos[j]:
                        flag = True

                if flag == False:
                    conjuntoDif.append(conjuntoUno[i])
                else:
                    flag = False

            return conjuntoDif

        def diferenciaSim(conjuntoUno,conjuntoDos):

            conjuntoDifSim = diferencia(conjuntoUno,conjuntoDos) + diferencia(conjuntoDos,conjuntoUno)

            return conjuntoDifSim

        print(diferenciaSim(v,w))
        imprimirMenu()
        opcion = int(input("Ingrese una opción: "))
    if opcion == 5:
        #39- Lee un entero y determina si el elemento pertenece o no a cada uno de los conjuntos y lo imprime.
        def pertenece(conjuntoUno,conjuntoDos,numeroEnt):

            flagUno = False
            flagDos = False
            for i in range(0,len(conjuntoUno)):
                if conjuntoUno[i] == numeroEnt:
                    flagUno = True
            for j in range(0,len(conjuntoDos)):
                if conjuntoDos[j] == numeroEnt:
                    flagDos = True

            if flagUno and flagDos:
                return True
            else:
                return False

        numero = int(input("Ingrese un número entero: "))

        print("El número entero pertenece a cada uno de los conjuntos:",pertenece(v,w,numero))
        imprimirMenu()
        opcion = int(input("Ingrese una opción: "))
    if opcion == 6:
        #40- Determina sí el primer conjunto esta contenido en el segundo y lo imprime.
        def contenido(conjuntoUno,conjuntoDos):

            cont = 0
            for i in range(0,len(conjuntoUno)):
                for j in range(0,len(conjuntoDos)):
                    if conjuntoUno[i] == conjuntoDos[j]:
                        cont = cont + 1
            
            if cont == len(conjuntoUno):
                return True
            else:
                return False

        print("El primer conjunto esta contenido en el segundo conjunto:",contenido(w,v))

        imprimirMenu()
        opcion = int(input("Ingrese una opción: "))
#42- Desarrollar el programa anterior usando la representación modificada con las operaciones entre
#conjuntos optimizadas. 
def imprimirMenu():
    print("//////////////////////////////////////////////")
    print("///////////////Menú Principal////////////////////")
    print("1. Unión")
    print("2. Intersección")
    print("3. Diferencia")
    print("4. Diferencia Simetrica")
    print("5. Pertenece")
    print("6. Contenido")
    print("7. Salir")

print("//////////////////////////////////////////////")
print("///////////////Menú Principal////////////////////")
print("1. Unión")
print("2. Intersección")
print("3. Diferencia")
print("4. Diferencia Simetrica")
print("5. Pertenece")
print("6. Contenido")
print("7. Salir")
opcion = int(input("Ingrese una opción: "))
while opcion > 0 and opcion <= 6:
    if opcion == 1:
        #35.2- Calcula en un arreglo la unión de los conjuntos y la imprime.
        def ordenarConjunto(conjunto):

        aux = 0
        for i in range(0,len(conjunto)-1):
            for j in range(i+1,len(conjunto)):
            if conjunto[j]<conjunto[i]:
                aux = conjunto[i]
                conjunto[i] = conjunto[j]
                conjunto[j] = aux

        return conjunto

        def quitarRep(conjunto):

        conjuntoSinRep = []

        for i in range(0,len(conjunto)-1):
            if conjunto[i] != conjunto[i+1]:
            conjuntoSinRep.append(conjunto[i])

        return conjuntoSinRep
        
        def union(conjuntoUno,conjuntoDos):

        return quitarRep(ordenarConjunto(conjuntoUno+conjuntoDos))

        v = [1,2,5,7,9]
        w = [0,3,4,5,8]

        print(union(v,w))
        imprimirMenu()
        opcion = int(input("Ingrese una opción: "))
    if opcion == 2:
        #36.2- Calcula en un arreglo la intersección de los conjuntos y la imprime.
        def ordenarConjunto(conjunto):

        aux = 0
        for i in range(0,len(conjunto)-1):
            for j in range(i+1,len(conjunto)):
            if conjunto[j]<conjunto[i]:
                aux = conjunto[i]
                conjunto[i] = conjunto[j]
                conjunto[j] = aux

        return conjunto
        
        def interseccion(conjuntoUno,conjuntoDos):

        conjuntoInter = []
        for i in range(0,len(conjuntoUno)):
            for j in range(0,len(conjuntoDos)):
            if conjuntoUno[i] == conjuntoDos[j]:
                conjuntoInter.append(conjuntoUno[i])

        return ordenarConjunto(conjuntoInter)
        
        y = [9,2,5,7,1]
        z = [7,1,9,2]

        print(interseccion(y,z))
        imprimirMenu()
        opcion = int(input("Ingrese una opción: "))
    if opcion == 3:
        #37.2- Calcula en un arreglo la diferencia del primero con el segundo y la imprime.
        def ordenarConjunto(conjunto):

        aux = 0
        for i in range(0,len(conjunto)-1):
            for j in range(i+1,len(conjunto)):
            if conjunto[j]<conjunto[i]:
                aux = conjunto[i]
                conjunto[i] = conjunto[j]
                conjunto[j] = aux

        return conjunto
        
        def diferencia(conjuntoUno,conjuntoDos):

        conjuntoDif = []
        flag = False
        for i in range(0,len(conjuntoUno)):
            for j in range(0,len(conjuntoDos)):
            if conjuntoUno[i] == conjuntoDos[j]:
                flag = True

            if flag == False:
            conjuntoDif.append(conjuntoUno[i])
            else:
            flag = False

        return ordenarConjunto(conjuntoDif)
        
        y = [9,2,5,7,1,8,22]
        z = [7,1,9,2]

        print(diferencia(y,z))
        imprimirMenu()
        opcion = int(input("Ingrese una opción: "))
    if opcion == 4:
        #38.2- Calcula en un arreglo la diferencia simetrica de los conjuntos y la imprime.
        def ordenarConjunto(conjunto):

        aux = 0
        for i in range(0,len(conjunto)-1):
            for j in range(i+1,len(conjunto)):
            if conjunto[j]<conjunto[i]:
                aux = conjunto[i]
                conjunto[i] = conjunto[j]
                conjunto[j] = aux

        return conjunto
        
        def diferencia(conjuntoUno,conjuntoDos):

        conjuntoDif = []
        flag = False
        for i in range(0,len(conjuntoUno)):
            for j in range(0,len(conjuntoDos)):
            if conjuntoUno[i] == conjuntoDos[j]:
                flag = True

            if flag == False:
            conjuntoDif.append(conjuntoUno[i])
            else:
            flag = False

        return ordenarConjunto(conjuntoDif)

        def diferenciaSim(conjuntoUno,conjuntoDos):

        conjuntoDifSim = diferencia(conjuntoUno,conjuntoDos) + diferencia(conjuntoDos,conjuntoUno)

        return ordenarConjunto(conjuntoDifSim)

        y = [9,2,5,7,1,8,22]
        z = [7,1,9,2,0]

        print(diferenciaSim(y,z))
        imprimirMenu()
        opcion = int(input("Ingrese una opción: "))
    if opcion == 5:
        #39.2- Lee un entero y determina si el elemento pertenece o no a cada uno de los conjuntos y lo imprime.
        def pertenece(conjuntoUno,conjuntoDos,numeroEnt):

            flagUno = False
            flagDos = False
            for i in range(0,len(conjuntoUno)):
                if conjuntoUno[i] == numeroEnt:
                    flagUno = True
            for j in range(0,len(conjuntoDos)):
                if conjuntoDos[j] == numeroEnt:
                    flagDos = True

            if flagUno and flagDos:
                return True
            else:
                return False

        y = [9,2,5,7,1,8,22]
        z = [7,1,9,2,0]

        numero = int(input("Ingrese un número entero: "))

        print("El número entero pertenece a cada uno de los conjuntos:",pertenece(y,z,numero))
        imprimirMenu()
        opcion = int(input("Ingrese una opción: "))
    if opcion == 6:
        #40.2- Determina sí el primer conjunto esta contenido en el segundo y lo imprime.
        def contenido(conjuntoUno,conjuntoDos):

            cont = 0
            for i in range(0,len(conjuntoUno)):
                for j in range(0,len(conjuntoDos)):
                    if conjuntoUno[i] == conjuntoDos[j]:
                        cont = cont + 1
            
            if cont == len(conjuntoUno):
                return True
            else:
                return False

        y = [9,2,5,7,1,8,22]
        z = [7,1,9,2]

        print("El primer conjunto esta contenido en el segundo conjunto:",contenido(z,y))

        imprimirMenu()
        opcion = int(input("Ingrese una opción: "))
# /////////////////////////////////////////////////////// Fin Conjuntos como arreglos ///////////////////////////////////////////////////////////////////////

# /////////////////////////////////////////////////////// POLINOMIOS COMO ARREGLOS ///////////////////////////////////////////////////////////////////////
def imprimirMenu():
    print("//////////////////////////////////////////////")
    print("///////////////Menú Principal////////////////////")
    print("1. Evaluar")
    print("2. Sumar")
    print("3. Resta")
    print("4. Multiplicar")
    print("5. Dividir")
    print("6. Residuo")
    print("7. Salir")

print("//////////////////////////////////////////////")
print("///////////////Menú Principal////////////////////")
print("1. Evaluar")
print("2. Sumar")
print("3. Resta")
print("4. Multiplicar")
print("5. Dividir")
print("6. Residuo")
print("7. Salir")
opcion = int(input("Ingrese una opción: "))
while opcion > 0 and opcion <= 6:
    if opcion == 1:
        #43- Lee un real e imprime la evaluación de los dos polinomios en dicho dato.
        def evaluar(polinomioUno,polinomioDos,num):

            resultUno = 0
            resultDos = 0

            for i in range(0,len(polinomioUno)):
                resultUno = resultUno + (polinomioUno[i]*num**i)
            
            for j in range(0,len(polinomioDos)):
                resultDos = resultDos + (polinomioDos[j]*num**j)

            return resultUno,resultDos

        polUno = [5,2,-4,2]
        polDos = [15,-1,4,3]
        numero = float(input("Digite el número real para evaluar en los polinomios: "))

        print("Los polinomios evaluados en el número",numero,"dan como resultado respectivamente",evaluar(polUno,polDos,numero))        
        imprimirMenu()
        opcion = int(input("Ingrese una opción: "))
    if opcion == 2:
        #44- Calcula el polinomio suma y lo imprime.
        def sumar(polinomioUno,polinomioDos):

            polSumar = []

            if len(polinomioUno)>len(polinomioDos):
                for i in range(0,len(polinomioUno)):
                    if i <= len(polinomioDos)-1:
                        polSumar.append(polinomioUno[i]+polinomioDos[i])
                    else:
                        polSumar.append(polinomioUno[i])
            else:
                for i in range(0,len(polinomioDos)):
                    if i <= len(polinomioUno)-1:
                        polSumar.append(polinomioUno[i]+polinomioDos[i])
                    else:
                        polSumar.append(polinomioDos[i])

            return polSumar

        polUno = [5,2,-4,2]
        polDos = [15,-1,4,3]


        print("El arreglo de la suma de los polinomios es respectivamente",sumar(polUno,polDos))        
        imprimirMenu()
        opcion = int(input("Ingrese una opción: "))
    if opcion == 3:
        #45- Calcula el polinomio resta y lo imprime.
        def restar(polinomioUno,polinomioDos):

            polRestar = []

            if len(polinomioUno)>len(polinomioDos):
                for i in range(0,len(polinomioUno)):
                    if i <= len(polinomioDos)-1:
                        polRestar.append(polinomioUno[i]-polinomioDos[i])
                    else:
                        polRestar.append(polinomioUno[i])
            else:
                for i in range(0,len(polinomioDos)):
                    if i <= len(polinomioUno)-1:
                        polRestar.append(polinomioUno[i]-polinomioDos[i])
                    else:
                        polRestar.append(polinomioDos[i])

            return polRestar

        polUno = [5,2,-4,2]
        polDos = [15,-1,4,3]


        print("El arreglo de la resta de los polinomios es respectivamente",restar(polUno,polDos))    
        imprimirMenu()
        opcion = int(input("Ingrese una opción: "))
    if opcion == 4:
        #46- Calcula el polinomio multiplicación y lo imprime.
        def multiplicar(polinomioUno,polinomioDos):

            polMultiplicar = []
            for k in range(0,len(polinomioUno)+len(polinomioDos)-1):
                polMultiplicar.append(0)

            if len(polinomioUno)>=len(polinomioDos):
                for i in range(0,len(polinomioUno)):
                    for j in range(0,len(polinomioDos)):
                        polMultiplicar[j+i] = polMultiplicar[j+i] + polinomioUno[i]*polinomioDos[j]
            else:
                for i in range(0,len(polinomioDos)):
                    for j in range(0,len(polinomioUno)):
                        polMultiplicar[i+j] = polMultiplicar[i+j] + polinomioDos[i]*polinomioUno[j]

            return polMultiplicar

        polUno = [5,2,-4,2]
        polDos = [15,-1,4,3,5]

        print("El arreglo de la resta de los polinomios es respectivamente",multiplicar(polUno,polDos))       
        imprimirMenu()
        opcion = int(input("Ingrese una opción: "))
    if opcion == 5:
        #47- Calcula el polinomio divisi ́on del primer polinomio por el segundo y lo imprime.

        imprimirMenu()
        opcion = int(input("Ingrese una opción: "))
    if opcion == 6:
        #48- Calcula el polinomio residuo de la divisi ́on del primero por el segundo y lo imprime.
       
        imprimirMenu()
        opcion = int(input("Ingrese una opción: "))
# /////////////////////////////////////////////////////// Fin Polinomios como arreglos ///////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////// MATRICES ///////////////////////////////////////////////////////////////////////
#50- Desarrollar un algoritmo que permita sumar dos matrices de números reales (enteros).
def crearMat(x,y):
  matriz = []
  fila = []
  for i in range(0,x):
    fila = [0]*y
    matriz.append(fila)
  return matriz
print(crearMat(3,3))
def sumarMatrices(matrizUno,matrizDos):

  matSuma = crearMat(len(matrizUno),len(matrizUno))
  for i in range(0,len(matSuma)):
    for j in range(0,len(matSuma[i])):
      matSuma[i][j] = matrizUno[i][j]+matrizDos[i][j]

  return matSuma

matUno = [[1,2,3],
         [4,5,6],
         [7,8,9]]
matDos = [[7,8,9],
         [4,5,6],
         [1,2,3]]

print(sumarMatrices(matUno,matDos))

#51- Desarrollar un algoritmo que permita multiplicar dos matrices de números reales (enteros).
def crearMat(x,y):
  matriz=[]
  for i in range(x):
    fil =[0]*y
    matriz.append(fil)
  return matriz

def sumarMatrices(matrizUno,matrizDos):

  matSuma = crearMat(len(matrizUno),len(matrizUno))
  for i in range(0,len(matSuma)):
    for j in range(0,len(matSuma[i])):
      matSuma[i][j] = matrizUno[i][j]*matrizDos[i][j]

  return matSuma

matUno = [[1,2,3],
         [4,5,6],
         [7,8,9]]
matDos = [[7,8,9],
         [4,5,6],
         [1,2,3]]

print(sumarMatrices(matUno,matDos))

#52- Desarrollar un programa que sume los elementos de una columna dada de una matriz.
def sumarEnColumna(matriz,col):

  sumCol = 0
  for i in range(0,len(matriz)):
    sumCol = sumCol + matriz[i][col]
  return sumCol

matUno = [[1,2,3],
         [4,5,6],
         [7,8,9]]
columna = int(input("Digite el número de columna a sumar sus elementos: "))
print(sumarEnColumna(matUno,columna))

#53- Desarrollar un programa que sume los elementos de una fila dada de una matriz.
def sumarEnFila(matriz,fila):

  sumFila = 0
  for i in range(0,len(matriz)):
      sumFila = sumFila + matriz[fila][i]
  return sumFila

matUno = [[1,2,3],
         [4,5,6],
         [7,8,9]]
fila = int(input("Digite el número de fila a sumar sus elementos: "))
print(sumarEnFila(matUno,fila))

#54- Desarrollar un algoritmo que determine si una matriz es mágica.
def sumarEnColumna(matriz,col):

  sumCol = 0
  for i in range(0,len(matriz)):
    sumCol = sumCol + matriz[i][col]
  return sumCol

def sumarEnFila(matriz,fila):

  sumFila = 0
  for i in range(0,len(matriz)):
    sumFila = sumFila + matriz[fila][i]
  return sumFila

def sumarDiagonal(matriz):
  sumDiag = 0
  for i in range(0,len(matriz)):
    sumDiag = sumDiag + matriz[i][i]
  return sumDiag

def sumarDiagonal2(matriz):
  sumDiag2 = 0
  for i in range(0,len(matriz)):
    for j in range(0,len(matriz[i])):
      if  i == len(matriz)-j-1 and j == len(matriz)-i-1:
        sumDiag2 = sumDiag2 + matriz[i][j]
  return sumDiag2

def matrizMagica(matriz):

  for i in range(0,len(matriz)-1):
    if sumarEnFila(matriz,i) == sumarEnFila(matriz,i+1):
      if sumarEnColumna(matriz,i) == sumarEnColumna(matriz,i+1):
        if sumarDiagonal(matriz) == sumarDiagonal2(matriz):
          return True
    else:
      return False

mat = [[8,1,6],
       [3,5,7],
       [4,9,2]]

print("La matriz es mágica:",matrizMagica(mat))

#55- Desarrollar un algoritmo que dado un entero, reemplace en una matriz todos los números
#mayores a un número dado por un uno y todos los menores o iguales por un cero.
def remplazarUnosyCeros(matriz,num):

  for i in range(0,len(matriz)):
    for j in range(0,len(matriz[i])):
      if  matriz[i][j] > num:
        matriz[i][j] = 1
      else:
        matriz[i][j] = 0

  return matriz

matUno = [[8,1,6],
         [3,5,7],
         [4,9,2]]
numero = int(input("Digite un número entero: "))

print(remplazarUnosyCeros(matUno,numero))

#56- Desarrollar un programa que calcule el determinante de una matriz cuadrada.
def borrarFila(matriz,fila):

  matNueva = []

  for i in range(0,len(matriz)):
    if i != fila:
      matNueva.append(matriz[i])
  
  return matNueva

def borrarCol(matriz,col):

  matNueva = []
  a = []
  for i in range(0,len(matriz)):
    for j in range(0,len(matriz[i])):
      if j != col:
        a.append(matriz[i][j])
    matNueva.append(a)
    a = []
  return matNueva

def detDosXDos(matriz):

  return matriz[0][0]*matriz[1][1] - matriz[1][0]*matriz[0][1] 

def detTresXTres(matriz):

  det = 0

  for j in range(0,len(matriz)):
      det = det + (matriz[0][j]*((-1)**(j))*detDosXDos(borrarCol(borrarFila(matriz,0),j)))

  return det

def determinante(matriz):

  det = 0

  if len(matriz) == 2:
    det = detDosXDos(matriz)
  if len(matriz) == 3:
    det = detTresXTres(matriz)
  if len(matriz) == 4:
    for j in range(0,len(matriz)):
      det = det + (matriz[0][j]*((-1)**(j))*detTresXTres(borrarCol(borrarFila(matriz,0),j)))
    
  return det

matUno = [[8,1,6],
         [3,5,7],
         [4,9,2]]


mat = [[1,2,1,2],
       [1,2,3,4],
       [-1,3,3,-1],
       [2,2,1,1]]

print(determinante(mat))

#57- Desarrollar un programa que dadas una matriz cuadrada A y un arreglo de n ́umeros reales
#del mismo tamaño B, calcule una solución x para el sistema de ecuaciones lineales Ax = B.
def borrarFila(matriz,fila):

  matNueva = []

  for i in range(0,len(matriz)):
    if i != fila:
      matNueva.append(matriz[i])
  
  return matNueva

def borrarCol(matriz,col):

  matNueva = []
  a = []
  for i in range(0,len(matriz)):
    for j in range(0,len(matriz[i])):
      if j != col:
        a.append(matriz[i][j])
    matNueva.append(a)
    a = []
  return matNueva

def detDosXDos(matriz):

  return matriz[0][0]*matriz[1][1] - matriz[1][0]*matriz[0][1] 

def detTresXTres(matriz):

  det = 0

  for i in range(0,len(matriz)):
      for j in range(0,len(matriz[i])):
        if i == 0:
          det = det + (matriz[i][j]*((-1)**(i+j))*detDosXDos(borrarCol(borrarFila(matriz,i),j)))

  return det

def matInversa(matriz):

  matInv = []
  escalar = 0
  if len(matriz) == 2:
    escalar = 1/detDosXDos(matriz)
    matInv = [[matriz[1][1]*escalar,-matriz[0][1]*escalar],[-matriz[1][0]*escalar,matriz[0][0]*escalar]]
  if len(matriz) == 3:
    escalar = 1/detTresXTres(matriz)
    matInv = [[escalar*(matriz[1][1]*matriz[2][2]-matriz[1][2]*matriz[2][1]),
              escalar*(matriz[0][2]*matriz[2][1]-matriz[0][1]*matriz[2][2]),
              escalar*(matriz[0][1]*matriz[1][2]-matriz[0][2]*matriz[1][1])],
              [escalar*(matriz[1][2]*matriz[2][0]-matriz[1][0]*matriz[2][2]),
              escalar*(matriz[0][0]*matriz[2][2]-matriz[0][2]*matriz[2][0]),
              escalar*(matriz[0][2]*matriz[1][0]-matriz[0][0]*matriz[1][2])],
              [escalar*(matriz[1][0]*matriz[2][1]-matriz[1][1]*matriz[2][0]),
              escalar*(matriz[0][1]*matriz[2][0]-matriz[0][0]*matriz[2][1]),
              escalar*(matriz[0][0]*matriz[1][1]-matriz[0][1]*matriz[1][0])]]
  elif len(matriz)>3:
    print("No se puede calcular la matriz inversa de una matriz mayor a 3X3.")
  return matInv

def vectorSolucion(matriz,vector):

  vecSol = []
  sum = 0
  for i in range(0,len(matriz)):
    for j in range(0,len(matriz[i])):
      sum = sum + matriz[i][j]*vector[j]
    vecSol.append(sum)
    sum = 0
  
  return vecSol

matrizA = [[1,2],[4,4]]
vectorB = [0,2]

matA = [[8,1,6],
         [3,5,7],
         [4,9,2]]
vecB = [1,3,5]

print(matInversa(matA))
print(vectorSolucion(matInversa(matA),vecB))

#58- Desarrollar un programa que calcule la inversa de una matriz cuadrada.
def borrarFila(matriz,fila):

  matNueva = []

  for i in range(0,len(matriz)):
    if i != fila:
      matNueva.append(matriz[i])
  
  return matNueva

def borrarCol(matriz,col):

  matNueva = []
  a = []
  for i in range(0,len(matriz)):
    for j in range(0,len(matriz[i])):
      if j != col:
        a.append(matriz[i][j])
    matNueva.append(a)
    a = []
  return matNueva

def detDosXDos(matriz):

  return matriz[0][0]*matriz[1][1] - matriz[1][0]*matriz[0][1] 

def detTresXTres(matriz):

  det = 0

  for i in range(0,len(matriz)):
      for j in range(0,len(matriz[i])):
        if i == 0:
          det = det + (matriz[i][j]*((-1)**(i+j))*detDosXDos(borrarCol(borrarFila(matriz,i),j)))

  return det

def matInversa(matriz):

  matInv = []
  escalar = 0
  if len(matriz) == 2:
    escalar = 1/detDosXDos(matriz)
    matInv = [[matriz[1][1]*escalar,-matriz[0][1]*escalar],[-matriz[1][0]*escalar,matriz[0][0]*escalar]]
  if len(matriz) == 3:
    escalar = 1/detTresXTres(matriz)
    matInv = [[escalar*(matriz[1][1]*matriz[2][2]-matriz[1][2]*matriz[2][1]),
              escalar*(matriz[0][2]*matriz[2][1]-matriz[0][1]*matriz[2][2]),
              escalar*(matriz[0][1]*matriz[1][2]-matriz[0][2]*matriz[1][1])],
              [escalar*(matriz[1][2]*matriz[2][0]-matriz[1][0]*matriz[2][2]),
              escalar*(matriz[0][0]*matriz[2][2]-matriz[0][2]*matriz[2][0]),
              escalar*(matriz[0][2]*matriz[1][0]-matriz[0][0]*matriz[1][2])],
              [escalar*(matriz[1][0]*matriz[2][1]-matriz[1][1]*matriz[2][0]),
              escalar*(matriz[0][1]*matriz[2][0]-matriz[0][0]*matriz[2][1]),
              escalar*(matriz[0][0]*matriz[1][1]-matriz[0][1]*matriz[1][0])]]
  elif len(matriz)>3:
    print("No se puede calcular la matriz inversa de una matriz mayor a 3X3.")
  return matInv

matriz = [[1,2],[4,4]]

matUno = [[8,1,6],
         [3,5,7],
         [4,9,2]]

print(matInversa(matriz))

#59- Desarrollar un programa que tome un arreglo de tamaño n^2 y llene en espiral hacia adentro una matriz cuadrada de tamaño n.
def crearMat(x,y):
  matriz=[]
  for i in range(x):
    fil =[0]*y
    matriz.append(fil)
  return matriz

def matrizEnEspiral(arreglo):

  matrizEsp = crearMat(int(len(arreglo)**(1/2)),int(len(arreglo)**(1/2)))

  cont = 0

  for i in range(0,len(matrizEsp)):

    if cont == 0 and cont <=2:
      for j in range(0,len(matrizEsp)):
        matrizEsp[i][j] = arreglo[cont]
        cont = cont + 1
    
    if cont >=2 and cont <= 4:
      for j in range(1,len(matrizEsp)):
        matrizEsp[j][len(matrizEsp)-1] = arreglo[cont]
        cont = cont + 1
    
    if cont >=4 and cont <= 6:
      for j in range(len(matrizEsp)-2,-1,-1):
        matrizEsp[len(matrizEsp)-1][j] = arreglo[cont]
        cont = cont + 1
    
    if cont >=6 and cont <= 7:
      for j in range(len(matrizEsp)-2,0,-1):
        matrizEsp[j][0] = arreglo[cont]
        cont = cont + 1
    
    if cont == 8:
      for j in range(1,len(matrizEsp)-1):
        matrizEsp[len(matrizEsp)-2][j] = arreglo[cont]
        cont = cont + 1

  return matrizEsp

arreglo = [1,2,3,4,5,6,7,8,9]

print(matrizEnEspiral(arreglo))
# /////////////////////////////////////////////////////// Fin Matrices ///////////////////////////////////////////////////
# /////////////////////////////////////////////////////// CADENAS ///////////////////////////////////////////////////////////////////////
#71- Desarrollar un algoritmo que reciba como entrada un caracter y de como salida el numero de
#ocurrencias de dicho caracter en una cadena de caracteres.
def ocurrencias(caracter):

    ocurrencias = 0

    for i in range(0,len(cadena)):
        if cadena[i] == caracter:
            ocurrencias = ocurrencias + 1

    return ocurrencias

caracterUsuario = input("Digite el caracter, al que se le quiere contar sus ocurrencias en una cadena: ")

cadena = "cadena de prueba para el algoritmo"

print("El caracter",caracterUsuario,"aparece",ocurrencias(caracterUsuario),"veces en la cadena.")

#72- Desarrollar un algoritmo que reciba como entrada dos cadenas y determine si la primera es subcadena de la segunda.
def subcadena(cadenaUno,cadenaDos):

    for i in range(0,len(cadenaDos)):
        if  cadenaDos[i:i+len(cadenaUno)] == cadenaUno[0:len(cadenaUno)]:
            print(cadenaDos[i:i+len(cadenaUno)])
            return True

    return False
            
cadenaUno = input("Digite la primer cadena de texto: ")
cadenaDos = input("Digite la segunda cadena de texto: ")

print("La primera cadena de texto si subcadena de la cadena de la segunda cadena de texto:",subcadena(cadenaUno,cadenaDos))

#73- Desarrollar un algoritmo que reciba dos cadenas de caracteres y determine si la primera esta incluida en la segunda,
#todos los caracteres (con repeticiones) de la cadena uno estan presentes en la cadena dos, sin importar el orden.
def incluida(cadenaUno,cadenaDos):

    cont = 0

    for i in range(0,len(cadenaUno)):
        flag = False
        for j in range(0,len(cadenaDos)):
            if cadenaUno[i] == cadenaDos[j] and not flag:
                cont = cont + 1
                flag = True
            
    if cont == len(cadenaUno):
        return True
    else:
        return False

cadenaUno = input("Digite la primer cadena de texto: ")
cadenaDos = input("Digite la segunda cadena de texto: ")

print("La primera cadena si esta incluida en la segunda cadena de texto",incluida(cadenaUno,cadenaDos))

#74- Desarrollar un algoritmo que invierta una cadena de caracteres.
def invertir(cadena):

    cadenaInvertida = ""

    for i in range(len(cadena)-1,-1,-1):
        cadenaInvertida = cadenaInvertida + cadena[i]

    return cadenaInvertida

cadena = input("Digite una cadena de texto: ")

print("La cadena",cadena,"invertida es",invertir(cadena))

#75- Desarrollar un algoritmo que determine si una cadena de caracteres es palíndrome. Una cadena se dice palíndrome si al invertirla es igual a ella misma.
def invertir(cadena):

    cadenaInvertida = ""

    for i in range(len(cadena)-1,-1,-1):
        cadenaInvertida = cadenaInvertida + cadena[i]

    return cadenaInvertida
def palindrome(cadena):

    if (cadena) == invertir(cadena):
        return True
    else:
        return False

cadena = input("Digite una cadena de texto: ")

print("La cadena",cadena," es palíndrome:",palindrome(cadena)) 

#76- Desarrollar un algoritmo que determina si una cadena de caracteres es frase palíndrome. Una cadena se dice frase palíndrome 
#si la cadena al eliminarle los espacios es palíndrome.

def invertir(cadena):

    cadenaInvertida = ""

    for i in range(len(cadena)-1,-1,-1):
        cadenaInvertida = cadenaInvertida + cadena[i]

    return cadenaInvertida
def borrarEspacios(cadena):

    aux = ""

    for i in range(0,len(cadena)):
        if cadena[i] != " ":
            aux = aux + cadena[i]

    return aux
def frasePalindrome(cadena):

    aux = borrarEspacios(cadena)
    
    if (aux) == invertir(aux):
        return True
    else:
        return False

cadena = input("Digite una cadena de texto: ")

print("La cadena",cadena,"es una frase palíndrome:",frasePalindrome(cadena))

#77- Desarrollar un algoritmo que realice el corrimiento circular a izquierda de una cadena de
#caracteres. El corrimiento circular a izquierda es pasar el primer carácter de una cadena como
#ultimo carácter de la misma.
def corriCircularIzq(cadena):

    cadenaCorriIzq = ""

    for i in range(len(cadena)-1,-1,-1):
        if i != 0:
            cadenaCorriIzq = cadena[i] + cadenaCorriIzq
        else:
            cadenaCorriIzq = cadenaCorriIzq + cadena[i]
            
    return cadenaCorriIzq

cadena = input("Digite una cadena de texto: ")
print("El corrimiento circular de la cadena",cadena,"es",corriCircularIzq(cadena))

#78- Desarrollar un algoritmo que realice el corrimiento circular a derecha de una cadena de caracteres. 
#El corrimiento circular a derecha de una cadena es poner el  ́ultimo carácter de la
#cadena como primer carácter de la misma.
def corriCircularDer(cadena):

    cadenaCorriDer = ""

    for i in range(0,len(cadena)):
        if i != len(cadena)-1:
            cadenaCorriDer =  cadenaCorriDer + cadena[i]
        else:
            cadenaCorriDer = cadena[i] + cadenaCorriDer
            
    return cadenaCorriDer

cadena = input("Digite una cadena de texto: ")
print("El corrimiento circular de la cadena",cadena,"es",corriCircularDer(cadena))

#79- Desarrollar un algoritmo que codifique una cadena de caracteres mediante una cadena de
#correspondencias de caracteres dada. La cadena de correspondencias tiene como el primer
#carácter el carácter equivalente para el carácter ‘a’, el segundo carácter para 
#la ‘b’y así sucesivamente hasta la ‘z’. No se tiene traducción para las mayúsculas ni para la ‘ñ’.
def cadenaANumero(letra):

  abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]  

  for j in range(0,len(abecedario)):
    if letra == abecedario[j]:
      return j

  return -1
    
def codifique(cadena,cadenaCorrespondencia):

  cadenaCodificada = ""

  for i in range(0,len(cadena)):
    if cadena[i] == " ":
      cadenaCodificada = cadenaCodificada + " "
    elif cadenaANumero(cadena[i]) == -1:
        cadenaCodificada = cadenaCodificada + cadena[i] 
    else:
        cadenaCodificada = cadenaCodificada + cadenaCorrespondencia[cadenaANumero(cadena[i])]

  return cadenaCodificada

print(codifique("al sur de Colombia","qwertyuiopasdfghjklzxcvbnm"))

#80- Desarrollar un algoritmo que decodifique una cadena de caracteres mediante una cadena de
#correspondencias de caracteres dada. La cadena de correspondencias tiene como el primer
#carácter el carácter equivalente para el carácter ‘a’, el segundo carácter para 
#la ‘b’y así sucesivamente hasta la ‘z’. No se tiene traducción para las mayúsculas ni para la ‘ñ’.
def numeroALetra(num):

  abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]  

  for j in range(0,len(abecedario)):
    if num == j:
      return abecedario[j]

  return -1
def posicionLetra(letra,cadenaCorrespondencia):

    for k in range(0,len(cadenaCorrespondencia)):
        if letra == cadenaCorrespondencia[k]:
            return k
  
    return -1
def decodifique(cadena,cadenaCorrespondencia):

  cadenaDecodificada = ""

  for i in range(0,len(cadena)):
    if cadena[i] == " ":
      cadenaDecodificada = cadenaDecodificada + " "
    elif posicionLetra(cadena[i],cadenaCorrespondencia) == -1:
      cadenaDecodificada = cadenaDecodificada + cadena[i]
    else:
      cadenaDecodificada = cadenaDecodificada + numeroALetra(posicionLetra(cadena[i],cadenaCorrespondencia))

  return cadenaDecodificada

print(decodifique("qs lxk rt Cgsgdwoq","qwertyuiopasdfghjklzxcvbnm"))
# /////////////////////////////////////////////////////// Fin CADENAS ///////////////////////////////////////////////////////////////////////