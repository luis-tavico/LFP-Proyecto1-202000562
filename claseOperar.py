import math

class Operar:

    def __init__(self, operacion):
        self.operacion = operacion

    #FUNCIONES
    def seno (self, numero):
        resultado = math.sin(float(numero))
        return resultado

    def coseno (self, numero):
        resultado = math.cos(float(numero))
        return resultado

    def tangente (self, numero):
        resultado = math.tan(float(numero))
        return resultado

    def mod (self, numero1, numero2):
        resultado = float(numero1)%float(numero2)
        return resultado

    def potencia (self, base, exponente):
        resultado = float(base)**float(exponente)
        return resultado

    def raiz (self, radicando, indice):
        resultado = (float(radicando)**(1/float(indice)))
        return resultado

    def multiplicar (self, numero1, numero2):
        resultado = float(numero1)*float(numero2)   
        return resultado

    def dividir (self, numero1, numero2):
        resultado = float(numero1)/float(numero2)
        return resultado

    def sumar (self, numero1, numero2):
        resultado = float(numero1)+float(numero2)
        return resultado

    def restar (self, numero1, numero2):
        resultado = float(numero1)-float(numero2)
        return resultado
    #FiN FUNCIONES

    def resolver(self, operacion):
        #SEN
        while "sen" in operacion:
            posicion = operacion.index("sen") + 2
            posicionSiguiente = posicion+1
            numero = ""
            while ((operacion[posicion+1].isdigit() or operacion[posicion+1] == "." or operacion[posicionSiguiente] == "-")):
                posicionF = posicion+1
                numero += operacion[posicion+1]
                posicion += 1  
                if posicion+1 == len(operacion): break
            posicionI = operacion.index("sen")   
            operacion = operacion[0:posicionI] + str(self.seno(numero)) + operacion[posicionF+1:]
        #COS
        while "cos" in operacion:
            posicion = operacion.index("cos") + 2
            posicionSiguiente = posicion+1
            numero = ""
            while ((operacion[posicion+1].isdigit() or operacion[posicion+1] == "." or operacion[posicionSiguiente] == "-")):
                posicionF = posicion+1
                numero += operacion[posicion+1]
                posicion += 1  
                if posicion+1 == len(operacion): break
            posicionI = operacion.index("cos")   
            operacion = operacion[0:posicionI] + str(self.coseno(numero)) + operacion[posicionF+1:]
        #TAN
        while "tan" in operacion:
            posicion = operacion.index("tan") + 2
            posicionSiguiente = posicion+1
            numero = ""
            while ((operacion[posicion+1].isdigit() or operacion[posicion+1] == "." or operacion[posicionSiguiente] == "-")):
                posicionF = posicion+1
                numero += operacion[posicion+1]
                posicion += 1  
                if posicion+1 == len(operacion): break
            posicionI = operacion.index("tan")   
            operacion = operacion[0:posicionI] + str(self.tangente(numero)) + operacion[posicionF+1:]
        #MOD
        while "%" in operacion:
            posicion = operacion.index("%")         
            numero1 = ""
            numero2 = ""
            while ((operacion[posicion-1].isdigit() or operacion[posicion-1] == "." or operacion[posicion-1] == "-") and posicion-1 >= 0):
                if operacion[posicion] == "-": break
                if operacion[posicion-1] == "-" and posicion-2 > 0 and not(operacion[posicion-2].isdigit()):
                    posicionI = posicion-1
                    numero1 =  (operacion[posicion-1] + numero1)
                elif posicion-1 >= 0:
                    posicionI = posicion-1
                    numero1 =  (operacion[posicion-1] + numero1)
                posicion -= 1   
            posicion = operacion.index("%")
            posicionSiguiente = posicion+1
            while ((operacion[posicion+1].isdigit() or operacion[posicion+1] == "." or operacion[posicionSiguiente] == "-")):
                posicionF = posicion+1
                numero2 += operacion[posicion+1]
                posicion += 1 
                if posicion+1 == len(operacion): break    
            operacion = operacion[0:posicionI] + str(self.mod(numero1, numero2)) + operacion[posicionF+1:] 
        #POTEN
        while "^" in operacion:
            posicion = operacion.index("^")
            base = ""
            exponente = ""
            while ((operacion[posicion-1].isdigit() or operacion[posicion-1] == "." or operacion[posicion-1] == "-") and posicion-1 >= 0):
                if operacion[posicion] == "-": break
                if operacion[posicion-1] == "-" and posicion-2 > 0 and not(operacion[posicion-2].isdigit()):
                    posicionI = posicion-1
                    base =  (operacion[posicion-1] + base)
                elif posicion-1 >= 0:
                    posicionI = posicion-1
                    base =  (operacion[posicion-1] + base)
                posicion -= 1   
            posicion = operacion.index("^")
            posicionSiguiente = posicion+1
            while ((operacion[posicion+1].isdigit() or operacion[posicion+1] == "." or operacion[posicionSiguiente] == "-")):
                posicionF = posicion+1
                exponente += operacion[posicion+1]
                posicion += 1    
                if posicion+1 == len(operacion): break 
            operacion = operacion[0:posicionI] + str(self.potencia(base, exponente)) + operacion[posicionF+1:]
        #RAIZ
        while "√" in operacion:
            posicion = operacion.index("√")
            radicando = ""
            indice = ""
            while ((operacion[posicion-1].isdigit() or operacion[posicion-1] == ".") and posicion-1 >= 0):
                posicionI = posicion-1
                indice =  (operacion[posicion-1] + indice)
                posicion -= 1    
            posicion = operacion.index("√")
            posicionSiguiente = posicion+1
            while ((operacion[posicion+1].isdigit() or operacion[posicion+1] == "." or operacion[posicionSiguiente] == "-")):
                posicionF = posicion+1
                radicando += operacion[posicion+1]
                posicion += 1  
                if posicion+1 == len(operacion): break
            operacion = operacion[0:posicionI] + str(self.raiz(indice, radicando)) + operacion[posicionF+1:]
        #DIV
        while "/" in operacion:
            posicion = operacion.index("/")
            numero1 = ""
            numero2 = ""
            while ((operacion[posicion-1].isdigit() or operacion[posicion-1] == "." or operacion[posicion-1] == "-") and posicion-1 >= 0):
                if operacion[posicion] == "-": break
                if operacion[posicion-1] == "-" and posicion-2 > 0 and not(operacion[posicion-2].isdigit()):
                    posicionI = posicion-1
                    numero1 =  (operacion[posicion-1] + numero1)
                elif posicion-1 >= 0:
                    posicionI = posicion-1
                    numero1 =  (operacion[posicion-1] + numero1)
                posicion -= 1   
            posicion = operacion.index("/")
            posicionSiguiente = posicion+1
            while ((operacion[posicion+1].isdigit() or operacion[posicion+1] == "." or operacion[posicionSiguiente] == "-")):
                posicionF = posicion+1
                numero2 += operacion[posicion+1]
                posicion += 1 
                if posicion+1 == len(operacion): break   
            operacion = operacion[0:posicionI] + str(self.dividir(numero1, numero2)) + operacion[posicionF+1:]
        #MULTI
        while "*" in operacion:
            posicion = operacion.index("*")
            numero1 = ""
            numero2 = ""
            while ((operacion[posicion-1].isdigit() or operacion[posicion-1] == "." or operacion[posicion-1] == "-") and posicion-1 >= 0):
                if operacion[posicion] == "-": break
                if operacion[posicion-1] == "-" and posicion-2 > 0 and not(operacion[posicion-2].isdigit()):
                    posicionI = posicion-1
                    numero1 =  (operacion[posicion-1] + numero1)
                elif posicion-1 >= 0:
                    posicionI = posicion-1
                    numero1 =  (operacion[posicion-1] + numero1)
                posicion -= 1   
            posicion = operacion.index("*")
            posicionSiguiente = posicion+1      
            while ((operacion[posicion+1].isdigit() or operacion[posicion+1] == "." or operacion[posicionSiguiente] == "-")):
                posicionF = posicion+1
                numero2 += operacion[posicion+1]
                posicion += 1  
                if posicion+1 == len(operacion): break  
            operacion = operacion[0:posicionI] + str(self.multiplicar(numero1, numero2)) + operacion[posicionF+1:]     
        #RESTA
        pos = 0
        while pos < len(operacion):
            if operacion[pos] == "-":
                if pos > 0: 
                    if pos-1 >= 0 and operacion[pos-1].isdigit():
                        posicion = pos
                        numero1 = ""
                        numero2 = ""
                        while ((operacion[posicion-1].isdigit() or operacion[posicion-1] == "." or operacion[posicion-1] == "-") and posicion-1 >= 0):
                            if operacion[posicion-1] == "-" and posicion-2 > 0 and not(operacion[posicion-2].isdigit()):
                                posicionI = posicion-1
                                numero1 =  (operacion[posicion-1] + numero1)
                            elif posicion-1 >= 0:
                                posicionI = posicion-1
                                numero1 =  (operacion[posicion-1] + numero1)
                            posicion -= 1
                        posicion = pos
                        posicionSiguiente = posicion+1
                        while ((operacion[posicion+1].isdigit() or operacion[posicion+1] == "." or operacion[posicionSiguiente] == "-")):
                            posicionF = posicion+1
                            numero2 += operacion[posicion+1]
                            posicion += 1  
                            if posicion+1 == len(operacion): break 
                        operacion = operacion[0:posicionI] + str(self.restar(numero1, numero2)) + operacion[posicionF+1:] 
            pos += 1          
        #SUMA
        while "+" in operacion:
            posicion = operacion.index("+")
            numero1 = ""
            numero2 = ""
            while ((operacion[posicion-1].isdigit() or operacion[posicion-1] == "." or operacion[posicion-1] == "-") and posicion-1 >= 0):
                if operacion[posicion] == "-": break
                if operacion[posicion-1] == "-" and posicion-2 > 0 and not(operacion[posicion-2].isdigit()):
                    posicionI = posicion-1
                    numero1 =  (operacion[posicion-1] + numero1)
                elif posicion-1 >= 0:
                    posicionI = posicion-1
                    numero1 =  (operacion[posicion-1] + numero1)
                posicion -= 1  
            posicion = operacion.index("+")
            posicionSiguiente = posicion+1
            while ((operacion[posicion+1].isdigit() or operacion[posicion+1] == "." or operacion[posicionSiguiente] == "-")):
                posicionF = posicion+1
                numero2 += operacion[posicion+1]
                posicion += 1     
                if posicion+1 == len(operacion): break
            operacion = operacion[0:posicionI] + str(self.sumar(numero1, numero2)) + operacion[posicionF+1:]
        return operacion

    def operar(self):
        try:
            posicion = 0
            while posicion < len(self.operacion):
                if self.operacion[posicion] == "(":
                    posicionParentesisAbierto = posicion               
                elif self.operacion[posicion] == ")":
                    posicionParentesisCerrado = posicion  
                    subOperacion = self.operacion[posicionParentesisAbierto+1:posicionParentesisCerrado]
                    subOperacion = self.resolver(subOperacion)
                    self.operacion = self.operacion[0:posicionParentesisAbierto]+subOperacion+self.operacion[posicionParentesisCerrado+1:]
                    posicion = 0
                    continue
                posicion += 1
            resultado = float(self.resolver(self.operacion))
            return round(resultado, 2)
        except ZeroDivisionError:
            return "No es posible dividir 0 entre 0"
        except:
            return "No se pudo realizar la operacion"