print(" ")
print("nolasco_aguilar_martha_sofia_0948_3W")#datos

class Triangulo:#crea clase
    def __init__(self, lado1, lado2, lado3):#define funcion
        self.lado1 = lado1#valor
        self.lado2 = lado2#valor
        self.lado3 = lado3#valor

    def lado_mayor(self):#define funcion
        return max(self.lado1, self.lado2, self.lado3)#devuelve valores

    def tipo(self):#define funcion
        if self.lado1 == self.lado2 == self.lado3:#verifica si la condicion es verdadera
            return 'Equilátero'#devuelve mensaje
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:#elif
            return 'Isósceles'#devuelve mensaje
        else:#verifica si la condicion es falsa
            return 'Escaleno'#devuelve mensaje

lado1 = float(input("Introduce el primer lado del triángulo: "))#solicita ingresar lado
print(" ") #espacio
lado2 = float(input("Introduce el segundo lado del triángulo: "))#solicita ingresar lado
print(" ") #espacio
lado3 = float(input("Introduce el tercer lado del triángulo: "))#solicita ingresar lado

triangulo = Triangulo(lado1, lado2, lado3)#valores
print(" ") #espacio
print(f"El lado mayor del triángulo es: {triangulo.lado_mayor()}") #imprime lado mayor
print(" ") #espacio
print(f"El triángulo es: {triangulo.tipo()}")#imprime tipo 

