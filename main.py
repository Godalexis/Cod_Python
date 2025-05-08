import random

class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def atacar(self, otro):
        daño = random.randint(1, self.ataque)
        print(f"{self.nombre} ataca a {otro.nombre} y causa {daño} de daño.")
        otro.recibir_daño(daño)

    def recibir_daño(self, daño):
        self.vida -= daño
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nombre} ahora tiene {self.vida} de vida.")

    def esta_vivo(self):
        return self.vida > 0


jugador = Personaje("Alexis", 100, 20)
enemigo = Personaje("Orco", 80, 15)



#def operacion_matematica(operador, *args):
#    if not args:
#        return "Error: No se proporcionaron números."

#    if operador == 'suma':
#        return sum(args)

#    elif operador == 'resta':
#        resultado = args[0]
#        for num in args[1:]:
#            resultado -= num
#        return resultado

#    elif operador == 'multiplicacion':
#        resultado = 1
#        for num in args:
#            resultado *= num
#        return resultado

#    elif operador == 'division':
#        resultado = args[0]
#        try:
#            for num in args[1:]:
#                resultado /= num
#            return resultado
#        except ZeroDivisionError:
#            return "Error: División por cero."

#    else:
#        return "Operación no reconocida"

#def anio_bisiesto():
#    try:
#        anio = int(input("Ingrese un año: "))
        
#        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
#            print(f"El año {anio} es bisiesto")
#        else:
#            print(f"El año {anio} no es bisiesto")
#    except ValueError:
#        print("Por favor, ingrese un número válido.")


#anio_bisiesto()


#def tabla_multiplicar(número):
  #  for i in range(1, 11):
 #       print(f"{número} x {i} = {número * i}")


#número = int(input("Ingrese un número: "))
#tabla_multiplicar(número)

    
#def maximo (a, b, c):
 #   return max (a, b, c)

#num1 = float(input("Ingrese el primer número"))
#num2 = float(input("Ingrese el segundo número"))
#num3 = float(input("Ingrese el tercer número"))

#print(f"El mayor número es: {maximo(num1, num2, num3)}")


#import operator

#def calcular_expresion(expresion):
    #operadores = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    
    #for op in operadores.keys():
        #if op in expresion:
         #   num1, num2 = map(str.strip, expresion.split(op))
        #    try:
       #         num1, num2 = float(num1), float(num2)
      #          return operadores[op](num1, num2)
     #       except ValueError:
    #            return "Error: Entrada no válida"
   #         except ZeroDivisionError:
  #              return "Error: División por cero"
     
 #   return "Error: Operador no válido"

#expresion = input("Ingrese una operación matemática (ejemplo: 1 + 2): ")
#resultado = calcular_expresion(expresion)
#print("Resultado:", resultado)


#def mostrar_menu():
 #   print("\n1. Ver Saldo\n2. Retirar\n3. Depositar\n4. Salir")

#def consultar_saldo(saldo):
 #   print("Saldo actual:", saldo)

#def retirar_dinero(saldo):
 #   retirar = float(input("Ingrese la cantidad de dinero que desea retirar: "))
#   while retirar > saldo or retirar > 10000:
     #   print("No se puede retirar más dinero del que hay disponible.")
    #    retirar = float(input("Ingrese una cantidad válida que no exceda el saldo disponible: "))
   # saldo -= retirar
  #  print(f"Retiro exitoso. Su nuevo saldo es: {saldo}")
 #   return saldo

#def depositar_dinero(saldo):
 #   depositar = float(input("Ingrese la cantidad de dinero que desea depositar: "))
#    while depositar > 50000:
    #    print("No se puede depositar más de $50.000.")
   #     depositar = float(input("Ingrese una cantidad válida que no exceda $50.000: "))  
  #  saldo += depositar
 #   print(f"Depósito exitoso. Su nuevo saldo es: {saldo}")
#    return saldo

#def iniciar_cajero():
 #   saldo = 0  
#    while True:
     #   mostrar_menu()
    #    opcion = int(input("Opción: "))
        
   #     if opcion == 1:
  #          consultar_saldo(saldo)
 #       elif opcion == 2:
        #    saldo = retirar_dinero(saldo)
       # elif opcion == 3:
      #      saldo = depositar_dinero(saldo)
     #   elif opcion == 4:
    #        print("Gracias por usar nuestro cajero.")
   #         break
  #      else:
 #           print("Opción inválida. Intente nuevamente.")

#iniciar_cajero()




#def contar_vocales(cadena):
    
 #   vocales = "aeiou"
  #  contador = 0
    
  #  for letras in cadena:
  #      if letras in vocales:
  #          contador += 1
    
  #  return contador


#texto = "Hola Mundo, este es mi texto"
#i = contar_vocales(texto)
#print("La cantidad de vocales es: " +str(i))


#email=False

#miEmail=input("Ingresa el email ")

#for i in miEmail:
    
    #if (i=="@"):
    
        #email=True
        
#if email==True:
    #print("El email es correcto")
    
#else:
    #print("El email es incorrecto")


#print("Escoge un equipo para fichar")
#print("Equipos interesados: Barcelona - Chelsea - Milan")
#equipo=input("Equipo que quiere ir: ")

#if equipo in ("Barcelona", "Chelsea", "Milan"):
    #print("Equipo escogido " + equipo)
    
#else:
    #print("Ese equipo no esta interesado")



#print("Programa de Progresar")
#edad_persona=int(input("Edad de la persona"))
#print("edad_persona")

#numero_hermanos=int(input("Numero de hermanos"))
#print("numero_hermanos")

#salario_familiar=int(input("Sueldo mensual de la familia"))
#print("salario_familiar")

#if edad_persona>15 and numero_hermanos>2 or salario_familiar<=40000: 
    #print("Podes tener el Progresar")

#else:
    #print("Progresar rechazado")#




#print("Clasificacion a copas")

#puntos_equipos=int(input("Puntos de equipos: "))

#if puntos_equipos<20:
    #print("Desciende")
    
#elif puntos_equipos<45:
    #print("Se queda sin copas")
    
#elif puntos_equipos<60:
    #print("Europa League")
    
#else:
    #print("Champions League")
    


#print("Tabla de posiciones")
#tabla_de_posiciones=input()

#def tabla(puntos):
    #posicion="clasificado"
   # if puntos <50:
  #      posicion="descalificado"
 #   return posicion

#print(tabla(int(tabla_de_posiciones)))
        
        

#midiccionario={"Alemania": "Berlin", "España":"Madrid"}
#print(midiccionario["Alemania"])
#midiccionario["Portugal"]="Lisboa"
#print(midiccionario)
#del midiccionario ["España"]
#print(midiccionario)
#mitupla=["España", "Francia", "Alemania", "Argentina"]
#midiccionario={mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Berlin", mitupla[3]:"Santa Fe"}
#print(midiccionario)


#milista=["Luis", 18, 3, 2812]
#mitupla=tuple(milista)
#print(len(mitupla))


#miLista=["Jose", "Mia", "Liam", "Marta"] *4

#print(miLista[:]) 



#def mensaje():  #Declaracion
    
   # print('Hola mundo')
    #print('¿Como estas?')
    #print('Estamos en Python')
    
#mensaje()  #llamada a la funcion    

#mensaje()
#print('ejecutando codigo')
#mensaje()

#def suma():
    
#     num1 = 4
#    num2 = 5
#    print(num1 + num2)
    
    
#suma()

#def suma(num1, num2):
    
 #   print(num1 + num2)
    
    
#suma(6, 8)

#suma(3, 7)

#suma(235, 561)


#def resta():
    
   # num1 = 4
  #  num2 = 5
 #   print(num1 - num2)
    
    
#resta()


#numero1 = 3
#numero2 = 5 

#numero3 = numero1 + numero2

#numero4 = numero1 * numero2

#numero5 = numero2 - numero1

#numero6 = numero2 / numero1

#numero7 = numero2**numero1

#print(numero7)


#numero1= 9
#numero2= 10

#if numero1>numero2:
    #print('numero 1 es mayor')
#else:
    #print('numero 2 es mayor') 
    
    