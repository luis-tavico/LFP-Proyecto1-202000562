class GenerarReporteTokens:
  
  def __init__(self, tokens):
    self.tokens = tokens
    self.reporteTokens = ""
    self.crearArchivo()

  def crearArchivo(self):
    self.reporteTokens += """<!DOCTYPE html>
    <html lang="es">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Tokens_202000562</title>
        <link rel="stylesheet" href="styleTablas.css" />
      </head>
      <body>
        <div class="container">
          <h2>TABLA DE TOKENS</h2>
          <table>
            <thead>
              <tr>
                <th>No.</th>
                <th>Lexema/Token</th>
                <th>Tipo</th>
                <th>Columna</th>
                <th>Linea</th>
              </tr>
            </thead>
            <tbody>\n"""
    for token in self.tokens:
        self.reporteTokens += '              <tr>\n'
        self.reporteTokens += '                <td>'+ str(token.getNo()) +'</td>\n'
        self.reporteTokens += '                <td>'+ token.getLexema() +'</td>\n'
        self.reporteTokens += '                <td>'+ token.getTipo() +'</td>\n'
        self.reporteTokens += '                <td>'+ str(token.getColumna()) +'</td>\n'
        self.reporteTokens += '                <td>'+ str(token.getLinea()) +'</td>\n'
        self.reporteTokens += '              </tr>\n'
    self.reporteTokens += """            </tbody>
          </table>
        </div>
      </body>
    </html>"""

    archivo = open("Tokens_202000562.html", "w")
    archivo.write(self.reporteTokens)
    archivo.close()