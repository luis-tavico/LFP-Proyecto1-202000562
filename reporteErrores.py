class GenerarReporteErrores:
  
  def __init__(self, errores):
    self.errores = errores
    self.reporteErrores = ""
    self.crearArchivo()

  def crearArchivo(self):
    self.reporteErrores += """<!DOCTYPE html>
    <html lang="es">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Errores_202000562</title>
        <link rel="stylesheet" href="styleTablas.css" />
      </head>
      <body>
        <div class="container">
          <h2>TABLA DE ERRORES</h2>
          <table>
            <thead>
              <tr>
                <th>No.</th>
                <th>Lexema</th>
                <th>Tipo</th>
                <th>Columna</th>
                <th>Linea</th>
              </tr>
            </thead>
            <tbody>\n"""
    for error in self.errores:
        self.reporteErrores += '              <tr>\n'
        self.reporteErrores += '                <td>'+ str(error.getNo()) +'</td>\n'
        self.reporteErrores += '                <td>'+ error.getLexema() +'</td>\n'
        self.reporteErrores += '                <td>'+ error.getTipo() +'</td>\n'
        self.reporteErrores += '                <td>'+ str(error.getColumna()) +'</td>\n'
        self.reporteErrores += '                <td>'+ str(error.getLinea()) +'</td>\n'
        self.reporteErrores += '              </tr>\n'
    self.reporteErrores += """            </tbody>
          </table>
        </div>
      </body>
    </html>"""

    archivo = open("Errores_202000562.html", "w")
    archivo.write(self.reporteErrores)
    archivo.close()