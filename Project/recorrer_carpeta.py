import os
class generador_documento_qrc:
    def __init__(self):
        self.ruta = os.listdir("icons/")
        self.contenido_generico = self.crear_documento(self.ruta)
        with open("iconos.qrc", "w") as archivo_qrc:
            archivo_qrc.write(self.contenido_generico)

    def crear_documento(self, imagenes):
        self.contenido_generico = """<!DOCTYPE RCC><RCC version="1.0">\n<qresource>\n"""
        for nombre_imagen in imagenes:
            self.contenido_generico += f"<file>icons/{nombre_imagen}</file>\n"

        self.contenido_generico += """</qresource>\n</RCC>
        """
        return self.contenido_generico


generador_documento_qrc()
