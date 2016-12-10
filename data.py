import json

class data:  
    data = []

    def read(self):
        with open('data/data.json','r') as file:
            data = json.load(file)
            self.data = data['results'] 

    def getEntidad(self): 
        entidades = []
        for row in self.data:
            entidad = row['ent']
            if entidad not in entidades:
                entidades.append(entidad)
        return entidades

    def getMunicipio(self): 
        municipios = []
        for row in self.data:
            municipio = row['mun']
            if municipio not in municipios:
                municipios.append(municipio)
        return municipios       
        
    def getPorcentajeDeAnalfabebizacion(self, ent, porcAnalfa00):
        PorcentajeAnalf = []  
        for row in self.data:
            entidadP = row['ent']
            municipioP = row['mun']
            analfP=row['porcAnalfa00']
            if entidadP == ent and municipioP == municipio:
                PorcentajeAnalf.append([row['ent'], municipioP, row['porcAnalfa00']])
        return PorcentajeAnalf       
                