print(" ")#espacio
print("nolasco_aguilar_martha_sofia_0948_3W")#datos
class Calculadora():#crea una clase
    def __init__(self, num1, num2):#define funcion
        self._num1=num1 #valores
        self._num2=num2 #valores

    def suma(self):#define funcion
        resultado=self._num1 + self._num2 #calcula los valores
        print(f"»El resultado de la suma es: {self._num1} + {self._num2}={resultado}»")#imprime resultado

    def resta(self):#define funcion
        resultado=self._num1 - self._num2 #calcula los valores
        print(f"»El resultado de la resta es: {self._num1} – {self._num2}={resultado}»")#imprime resultado

    def division(self):#define la funcion
        resultado=self._num1 // self._num2 #calcula los valores
        print(f"»El resultado de la divisón es: {self._num1} // {self._num2}= {resultado}»")#imprime resultado

    def multiplicacion(self):#define funcion
        resultado=self._num1 * self._num2 #calcula resultados
        print(f"»El resultado de la multiplicación es: {self._num1} * {self._num2} = {resultado}»")#imprime resultado

operacion=Calculadora(10, 5)#calcula
operacion.suma()#imprime resultado

operacion=Calculadora(20, 5)#calcula
operacion.resta()#imprime resultado

operacion=Calculadora(15, 3)#calcula
operacion.division()#imprime resultado

operacion=Calculadora(8, 4)#calcula
operacion.multiplicacion()#imprime resultado 
