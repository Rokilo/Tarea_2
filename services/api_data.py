from Models.User_Model import User_Model as model

class Data:
    def __init__(self,Archivo):
        self.Data = self.Cargar_Data(Archivo)
    
    def Cargar_Data(self,Archivo):
        Datos = []
        Lineas = Archivo.readlines()
        for Dato in Lineas:
            Dato = Dato.strip("\n")
            Dato =Dato.split(";")
            Agregar = model(Dato[0],Dato[1],Dato[2],Dato[3],Dato[4],Dato[5],Dato[6],Dato[7])
            Datos.append(Agregar)
        return Datos
    
    def Buscar_Data(self,Pass):
        for Dato in  self.Data:
            if Dato.Contraseña == Pass:
                return Dato.Generar_JSON()