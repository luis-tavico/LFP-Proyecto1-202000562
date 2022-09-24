class Lexema:
    def __init__(self, no, lexema, tipo, linea, columna):
        self.no = no
        self.lexema = lexema
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

    def getNo(self):
        return self.no

    def getLexema(self):
        return self.lexema

    def getTipo(self):
        return self.tipo

    def getLinea(self):
        return self.linea

    def getColumna(self):
        return self.columna

    def setNo(self, no):
        self.no = no
    
    def setLexema(self, lexema):
        self.lexema = lexema

    def setTipo(self, tipo):
        self.tipo = tipo

    def setTipo(self, linea):
        self.linea = linea

    def setTipo(self, columna):
        self.columna = columna