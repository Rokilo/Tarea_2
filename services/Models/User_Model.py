from ast import literal_eval as le

class User_Model:
    def __init__(self,Con,Nom,Ape,Ser,Ini,Ter,Pre,Est):
        self.Contraseña = Con
        self.Nombre = Nom
        self.Apellido = Ape
        self.Servicio = Ser
        self.Inicio = Ini
        self.Termino = Ter
        self.Precio = Pre
        self.Estado = Est

    def Generar_JSON(self):
        String = f'"Nombre":"{self.Nombre}","Apellido":"{self.Apellido}","Servicio":"{self.Servicio}","Inicio_Servicio":"{self.Inicio}","Termino_Servicio":"{self.Termino}","Precio":"{self.Precio}","Estado":"{self.Estado}"'
        String = "{"+String+"}"
        return le(String)