from tkinter import messagebox
from claseOperar import Operar

class GenerarResultados:
    def __init__(self):
        self.colores = {"rojo":"red", "naranja":"orange", "amarillo":"yellow", "verde":"green", "azul":"blue", "violeta":"purple"}
        self.lexemasOperacion = []
        self.concatenarSigno = False
        self.operacion = ""
        self.parentesisAbiertos = 0
        self.scanner = ""
        self.numeroOperacion = 0
        self.Titulo = ""
        self.Descripcion = ""
        self.Contenido = ""
        self.styleResultados = "body {\n"
        self.styleResultados += "    margin: 10px;\n"
        self.styleResultados += "    min-height: 100vh;\n"
        self.styleResultados += "    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;\n"
        self.styleResultados += "}\n"
        self.htmlResultados = '<!DOCTYPE html>\n'
        self.htmlResultados += '<html lang="es">\n'
        self.htmlResultados += '  <head>\n'
        self.htmlResultados += '    <meta charset="UTF-8" />\n'
        self.htmlResultados += '    <meta http-equiv="X-UA-Compatible" content="IE=edge" />\n'
        self.htmlResultados += '    <meta name="viewport" content="width=device-width, initial-scale=1.0" />\n'
        self.htmlResultados += '    <title>Resultados_202000562</title>\n'
        self.htmlResultados += '    <link rel="stylesheet" href="styleResultados.css"/>\n'
        self.htmlResultados += '  </head>\n'
        self.htmlResultados += '  <body>\n'
        self.htmlResultados += '    <div class="container">\n'

    def leerArchivo(self, texto):
        self.Contenido += '      <div class="Contenido">\n'
        Areatexto = ""
        titulo = ""
        etiquetaTipo = False
        etiquetaTexto = False
        etiquetaFuncion = False
        etiquetaEstilo = False
        for linea in texto.split('\n'):
            tokenNumero = ""
            for lexema in linea:          
                if lexema.isalpha() or lexema == '\t':
                    self.scanner += lexema
                if etiquetaTipo:
                    if lexema.isdigit() or lexema == '.':
                        tokenNumero += lexema
                if etiquetaTexto or etiquetaFuncion or etiquetaEstilo:
                    Areatexto += lexema
            if self.scanner == 'Tipo':
                etiquetaTipo = not(etiquetaTipo)
            if self.scanner == 'Texto':
                etiquetaTexto = not(etiquetaTexto)
                if etiquetaTexto == False:
                    Areatexto = Areatexto.replace("</Texto>","")
                    self.Descripcion += '      <div class="Descripcion">\n'
                    self.Descripcion += '        <p>'+Areatexto+'</p>\n'
                    self.Descripcion += '      </div>\n'
                    Areatexto = ""
            if self.scanner in ['FuncionESCRIBIR', 'Funcion']:
                etiquetaFuncion = not(etiquetaFuncion)
                if etiquetaFuncion == False:
                    Areatexto = Areatexto.replace("<Titulo>","")
                    Areatexto = Areatexto.replace("\t","")
                    if "</Titulo>" in Areatexto:
                        Areatexto = Areatexto[0:Areatexto.index("</Titulo>")]
                        titulo = Areatexto
                        self.Titulo += '      <div class="Titulo">\n'
                        self.Titulo += '        <h1>'+titulo+'</h1>\n'
                        self.Titulo += '      </div>\n'
                    Areatexto = ""
            if self.scanner == 'Estilo':
                etiquetaEstilo = not(etiquetaEstilo)               
            if etiquetaEstilo:
                if "Titulo" in Areatexto:
                    color = ""
                    tamanio = ""
                    if "Color=" and "Tamanio=" in Areatexto:
                        indice = (Areatexto.index("Color=")+6)
                        while Areatexto[indice] != " ":
                            color += Areatexto[indice]
                            indice += 1
                        indice = (Areatexto.index("Tamanio=")+8)
                        while Areatexto[indice].isdigit():
                            tamanio += Areatexto[indice]
                            indice += 1
                        self.styleResultados += "\n.Titulo {\n"
                        if color.lower() in self.colores:                                     
                            self.styleResultados += "    color: " + self.colores[color.lower()]+";\n"
                        else: 
                            self.styleResultados += "    color: black;\n"
                        self.styleResultados += "    font-size: " + tamanio + "px;\n"
                        self.styleResultados += "}\n"
                elif "Descripcion" in Areatexto:
                    color = ""
                    tamanio = ""
                    if "Color=" and "Tamanio=" in Areatexto:
                        indice = (Areatexto.index("Color=")+6)
                        while Areatexto[indice] != " ":
                            color += Areatexto[indice]
                            indice += 1
                        indice = (Areatexto.index("Tamanio=")+8)
                        while Areatexto[indice].isdigit():
                            tamanio += Areatexto[indice]
                            indice += 1
                        self.styleResultados += "\n.Descripcion {\n"
                        if color.lower() in self.colores:                                     
                            self.styleResultados += "    color: " + self.colores[color.lower()]+";\n"
                        else: 
                            self.styleResultados += "    color: black;\n"
                        self.styleResultados += "    font-size: " + tamanio + "px;\n"
                        self.styleResultados += "}\n"
                elif "Contenido" in Areatexto:
                    color = ""
                    tamanio = ""
                    if "Color=" and "Tamanio=" in Areatexto:
                        indice = (Areatexto.index("Color=")+6)
                        while Areatexto[indice] != " ":
                            color += Areatexto[indice]
                            indice += 1
                        indice = (Areatexto.index("Tamanio=")+8)
                        while Areatexto[indice].isdigit():
                            tamanio += Areatexto[indice]
                            indice += 1
                        self.styleResultados += "\n.Contenido {\n"
                        if color.lower() in self.colores:                                     
                            self.styleResultados += "    color: " + self.colores[color.lower()]+";\n"
                        else: 
                            self.styleResultados += "    color: black;\n"
                        self.styleResultados += "    font-size: " + tamanio + "px;\n"
                        self.styleResultados += "}"
                Areatexto = ""
            if etiquetaTipo:
                self.tipo(tokenNumero)
            self.scanner = ""
        self.htmlResultados += self.Titulo
        self.htmlResultados += self.Descripcion
        self.htmlResultados += self.Contenido
        self.htmlResultados += "      </div>\n"
        self.htmlResultados += "    </div>\n"
        self.htmlResultados += "  </body>\n"
        self.htmlResultados += "</html>"
        archivoHtml = open("Resultados_202000562.html", "w", encoding="utf-8")
        archivoHtml.write(self.htmlResultados)
        archivoHtml.close()
        archivoHtml = open("styleResultados.css", "w", encoding="utf-8")
        archivoHtml.write(self.styleResultados)
        archivoHtml.close()

    def tipo(self, tokenNumero): 
        try: 
            if self.scanner.strip('\t') == 'OperacionSUMA':  
                self.lexemasOperacion.append('+')
                self.abrirParentesis()
            elif self.scanner.strip('\t') == 'OperacionRESTA':
                self.lexemasOperacion.append('-')
                self.abrirParentesis()
            elif self.scanner.strip('\t') == 'OperacionMULTIPLICACION':
                self.lexemasOperacion.append('*')
                self.abrirParentesis()
            elif self.scanner.strip('\t') == 'OperacionDIVISION':
                self.lexemasOperacion.append('/')
                self.abrirParentesis()
            elif self.scanner.strip('\t') == 'OperacionPOTENCIA':
                self.lexemasOperacion.append('^')
                self.abrirParentesis()
            elif self.scanner.strip('\t') == 'OperacionRAIZ':
                self.lexemasOperacion.append('√')
                self.abrirParentesis()
            elif self.scanner.strip('\t') == 'OperacionMOD':
                self.lexemasOperacion.append('%')
                self.abrirParentesis()
            elif self.scanner.strip('\t') == 'OperacionINVERSO':
                #self.lexemasOperacion.append('1/')
                self.abrirParentesis()
                self.operacion += "1/"
            elif self.scanner.strip('\t') == 'OperacionSENO':
                self.lexemasOperacion.append('sen')
                self.abrirParentesis()
            elif self.scanner.strip('\t') == 'OperacionCOSENO':
                self.lexemasOperacion.append('cos')
                self.abrirParentesis()
            elif self.scanner.strip('\t') == 'OperacionTANGENTE':
                self.lexemasOperacion.append('tan')
                self.abrirParentesis()
            elif self.scanner.strip('\t') == 'NumeroNumero': 
                self.concatenarSigno = not(self.concatenarSigno)
                if self.concatenarSigno and len(self.lexemasOperacion) > 0:
                    lexemaOperacion = self.lexemasOperacion.pop()
                else:
                    lexemaOperacion = ""                
                if lexemaOperacion in ['sen', 'cos', 'tan']:
                    self.operacion += lexemaOperacion + tokenNumero
                elif lexemaOperacion == "1/":
                    self.operacion += tokenNumero
                else:
                    self.operacion += tokenNumero + lexemaOperacion              
            elif self.scanner.strip('\t') == 'Operacion':
                if not(self.operacion[-1].isdigit() or self.operacion[-1] == ")"):
                    self.operacion = self.operacion[:-1]               
                if self.scanner.count('\t') > 0:
                    self.cerrarParentesis()
                else:
                    operar = Operar(self.operacion)
                    resultado = operar.operar()
                    self.operacion += ' = '+ str(resultado) 
                    self.Contenido += '        <p>'+self.operacion+'</p>\n'
                    self.operacion = ""
                    self.lexemasOperacion = []
                    self.parentesisAbiertos = 0
            self.scanner = ""            
        #except Exception as e:
        except:
            messagebox.showerror("Error", "¡Ocurrio un error al analizar el documento!")

    def abrirParentesis(self):
        self.concatenarSigno = False
        if self.operacion != "" and (self.operacion[-1].isdigit() or self.operacion[-1] == ")"):
            if len(self.lexemasOperacion) >= 2:
                lexemaOperacion = self.lexemasOperacion.pop(-2)
                self.operacion += lexemaOperacion
            else:
                lexemaOperacion = self.lexemasOperacion[0]
                self.operacion += lexemaOperacion
        if self.scanner.count('\t') > 0:
            self.operacion += "("
            self.parentesisAbiertos += 1 
        else: 
            self.numeroOperacion += 1
            self.Contenido += '        <h4>'+"Operacion "+str(self.numeroOperacion)+'</h4>\n'
            
    def cerrarParentesis(self):       
        if self.parentesisAbiertos > 0:
            self.operacion += ")"
            self.parentesisAbiertos -= 1