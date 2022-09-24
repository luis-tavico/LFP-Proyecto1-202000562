import os
from tkinter import Frame, Menu, Text, Tk, filedialog, messagebox
from analizadorLexico import AnalizadorLexico
from reporteErrores import GenerarReporteErrores
from reporteTokens import GenerarReporteTokens
from archivoSalida import GenerarResultados
from crearEstiloTabla import EstiloTabla

class Interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        ventanaAncho, ventanaAlto = 550, 400
        pantallaAncho = self.ventana.winfo_screenwidth()
        pantallaAlto = self.ventana.winfo_screenheight()
        posicionX = int(pantallaAncho/2 - ventanaAncho/2)
        posicionY = int(pantallaAlto/2 - ventanaAlto/2)
        self.ventana.geometry(f'{ventanaAncho}x{ventanaAlto}+{posicionX}+{posicionY}')
        self.ventana.minsize(550, 400)
        self.ventana.title("AnalizadorLexicoApp")
        self.ventana.resizable(True, True)
        self.rutaDelPrograma = os.getcwd()
        self.ventana.protocol("WM_DELETE_WINDOW", self.salir)
        self.ruta = ""
        self.contenidoArchivo = ""
        self.contenidoAreaTexto = ""
        self.iniciarComponentes()

    def iniciarComponentes(self):
        self.agregarMenu()
        self.agregarPanel()
        self.agregarAreadeTexto()
        EstiloTabla()

    def agregarMenu(self):
        self.menu = Menu(self.ventana)
        self.archivoMenu = Menu(self.menu, tearoff=0)
        self.archivoMenu.add_command(label="Abrir", command=self.abrir)
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label="Guardar", command=self.guardar)
        self.archivoMenu.add_command(label="Guardar como", command=self.guardarComo)
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label="Analizar", command=self.analizar)
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label="Errores", command=self.errores)
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label="Salir", command=self.salir)
        self.menu.add_cascade(menu=self.archivoMenu, label="Archivo")
        self.ayudaMenu = Menu(self.menu, tearoff=0)
        self.ayudaMenu.add_command(label="Manual Tecnico", command=self.manualT)
        self.ayudaMenu.add_command(label="Manual de Usuario", command=self.manualU)
        self.menu.add_cascade(menu=self.ayudaMenu, label="Ayuda")
        self.ventana.config(menu=self.menu)

    def agregarPanel(self):
        self.panel = Frame(self.ventana)
        self.panel.config(bg="white")
        self.panel.pack(fill="both", expand="true")

    def agregarAreadeTexto(self):
        self.areaTexto = Text(self.panel, font=("Segoe UI", 12), bd=0, )
        self.areaTexto.pack(fill="both", expand=1)
        self.areaTexto.config(padx=10, pady=5)

    def abrir(self):
        self.ruta = filedialog.askopenfilename(title="Abrir")
        if self.ruta != "":
            ruta, extension = os.path.splitext(self.ruta)
            if extension.lower() == ".lfp":
                self.areaTexto.delete(1.0, "end")
                archivo = open(self.ruta, 'r')
                self.contenidoArchivo = archivo.readlines()
                archivo.close()
                self.contenidoArchivo = "".join(self.contenidoArchivo)
                self.areaTexto.insert('insert', self.contenidoArchivo)
                self.contenidoAreaTexto = self.areaTexto.get(1.0, "end-1c")
            else: 
                messagebox.showwarning("Advertencia", "¡La extension del archivo es incorrecta!\nUnica extension aceptada -> (.lfp)")

    def guardar(self):
        self.contenidoAreaTexto = self.areaTexto.get(1.0, "end-1c")
        if self.ruta != "":
            archivo = open(self.ruta, "w")
            archivo.write(self.contenidoAreaTexto)
            archivo.close()
            self.contenidoArchivo = self.contenidoAreaTexto
        else:
            self.guardarComo()

    def guardarComo(self):
        self.contenidoAreaTexto = self.areaTexto.get(1.0, "end-1c")
        archivo = filedialog.asksaveasfile(
            title="Guardar como", mode="w", defaultextension=".lfp")
        if archivo != None:
            self.ruta = archivo.name
            archivo = open(self.ruta, "w")
            archivo.write(self.contenidoAreaTexto)
            archivo.close()
            self.contenidoArchivo = self.contenidoAreaTexto
            messagebox.showinfo(
                "Informacion", "¡Archivo Guardado Exitosamente!")

    def salir(self):
        self.contenidoAreaTexto = self.areaTexto.get(1.0, "end-1c")
        if self.contenidoAreaTexto != self.contenidoArchivo:
            respuesta = messagebox.askyesnocancel(
                "Pregunta", "¿Desea guardar los cambios?")
            if respuesta:
                if self.ruta != "":
                    archivo = open(self.ruta, "w")
                    archivo.write(self.contenidoAreaTexto)
                    archivo.close()
                    self.ventana.destroy()
                else:
                    self.guardarComo()
                    self.ventana.destroy()
            elif respuesta == False:
                self.ventana.destroy()
        else:
            self.ventana.destroy()

    def analizar(self):
        self.contenidoAreaTexto = self.areaTexto.get(1.0, "end-1c")
        if self.contenidoAreaTexto != "":
            self.guardar()
            analizadorLexico = AnalizadorLexico()
            analizadorLexico.analizar(self.contenidoAreaTexto)
            GenerarReporteTokens(analizadorLexico.tokens)
            generar = GenerarResultados()
            generar.leerArchivo(self.contenidoAreaTexto)
            os.system("Tokens_202000562.html")
            os.system("Resultados_202000562.html")
                            
    def errores(self):
        self.contenidoAreaTexto = self.areaTexto.get(1.0, "end-1c")
        if self.contenidoAreaTexto != "":
            self.guardar()
            analizadorLexico = AnalizadorLexico()
            analizadorLexico.analizar(self.contenidoAreaTexto)
            GenerarReporteErrores(analizadorLexico.errores)
            os.system("Errores_202000562.html")

    def manualT(self): 
        os.system("MANUAL_TECNICO.pdf")

    def manualU(self):
        os.system("MANUAL_DE_USUARIO.pdf")