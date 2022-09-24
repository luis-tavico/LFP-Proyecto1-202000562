from modeloLexema import Lexema

class AnalizadorLexico:
    def __init__(self):
        self.errores = []
        self.tokens = []
        self.tokensReservados = ["Tipo", "Operacion", "SUMA", "RESTA", "MULTIPLICACION", "DIVISION", "POTENCIA",
                                 "RAIZ", "INVERSO", "SENO", "COSENO", "TANGENTE", "MOD", "Numero", "Texto",
                                 "ESCRIBIR", "Funcion", "Estilo"]
        self.numLinea = 1 
        self.numColumna = 0
        self.numError = 0
        self.numToken = 0
        self.scanner = ""
        self.estado = 0 #Estado inicial 
        self.i = 0 
        self.texto = False

    def agregarToken(self, numToken, lexema, tipo, numLinea, numColumna):
        self.tokens.append(Lexema(numToken, lexema, tipo, numLinea, numColumna)) 
        if self.scanner == "Texto":
            self.texto = not(self.texto)
        self.scanner = ""

    def agregarError(self, numError, lexema, numLinea, numColumna):
        self.errores.append(Lexema(numError, lexema, "Error", numLinea, numColumna))

    def s0(self, lexema:str):
        #ESTADO S0
        if lexema.isalpha() or lexema.isdigit():
            self.estado = 1
            self.scanner += lexema
            self.numColumna += 1
        elif lexema == ".":
            self.estado = 1
            self.scanner += lexema
            self.numColumna +=1
        elif lexema == '<':
            self.estado = 2
            self.scanner += lexema
            self.numColumna +=1
        elif lexema == '/':
            self.estado = 3
            self.scanner += lexema
            self.numColumna +=1
        elif lexema == '=':
            self.estado = 4
            self.scanner += lexema
            self.numColumna +=1
        elif lexema == '>':
            self.estado = 5
            self.scanner += lexema
            self.numColumna +=1
        elif lexema == '[':
            self.estado = 6
            self.scanner += lexema
            self.numColumna +=1
        elif lexema == ']':
            self.estado = 7
            self.scanner += lexema
            self.numColumna +=1
        elif lexema == '\n':
            self.numColumna = 0
            self.numLinea += 1
        elif lexema in ["\t"," "]:
            self.numColumna += 1
        else:
            self.numColumna += 1           
            if self.texto == False:
                self.numError += 1
                self.agregarError(self.numError, lexema, self.numLinea, self.numColumna)  
            
    def s1(self,lexema:str):
        #ESTADO S1
        if lexema.isalpha():
            self.estado = 1
            self.scanner += lexema
            self.numColumna += 1
        elif lexema.isdigit():
            self.estado = 1
            self.scanner += lexema
            self.numColumna += 1  
        elif lexema == '.':
            self.estado = 1
            self.scanner += lexema
            self.numColumna += 1
        else:
            if self.scanner in self.tokensReservados:
                self.numToken += 1
                self.agregarToken(self.numToken, self.scanner, "token reservado {}".format(self.scanner), self.numLinea, self.numColumna)
            else:
                self.numToken += 1
                self.agregarToken(self.numToken, self.scanner, "contenido", self.numLinea, self.numColumna)
            self.estado = 0
            self.i -= 1

    def s2(self):
        #Estado S2
        self.numToken += 1
        self.agregarToken(self.numToken, self.scanner, "Menor que", self.numLinea, self.numColumna)
        self.estado = 0
        self.i -= 1

    def s3(self):
        #Estado S3
        self.numToken += 1
        self.agregarToken(self.numToken, self.scanner, "Barra Diagonal", self.numLinea, self.numColumna)
        self.estado = 0
        self.i -= 1
        
    def s4(self):
        #Estado S4
        self.numToken += 1
        self.agregarToken(self.numToken, self.scanner, "Igual", self.numLinea, self.numColumna)
        self.estado = 0
        self.i -= 1

    def s5(self):
        #Estado S5
        self.numToken += 1
        self.agregarToken(self.numToken, self.scanner, "Mayor que", self.numLinea, self.numColumna)
        self.estado = 0
        self.i -= 1

    def s6(self):
        #Estado S6
        self.numToken += 1
        self.agregarToken(self.numToken, self.scanner, "Corchete Abierto", self.numLinea, self.numColumna)
        self.estado = 0
        self.i -= 1
        
    def s7(self):
        #Estado S7
        self.numToken += 1
        self.agregarToken(self.numToken, self.scanner, "Corchete Cerrado", self.numLinea, self.numColumna)
        self.estado = 0
        self.i -= 1
  
    def analizar(self, contenido):
        self.i = 0
        while self.i < len(contenido):
            if self.estado == 0:
                self.s0(contenido[self.i])
            elif self.estado == 1:
                self.s1(contenido[self.i])
            elif self.estado == 2:
                self.s2()
            elif self.estado == 3:
                self.s3()
            elif self.estado == 4:
                self.s4()
            elif self.estado == 5:
                self.s5()
            elif self.estado == 6:
                self.s6()
            elif self.estado == 7:
                self.s7()
            self.i += 1