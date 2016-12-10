import web
import json
from data import data
from web import form

render = web.template.render('views/')

urls = (
    '/index','index',
    '/acercaDe','acercaDe',
    '/RezagoSocial','RezagoSocial',
    '/busqueda','busqueda',
    '/indexDatos','indexDatos',
    '/CrudDB','CrudDB',
    '/login','login'  
)
app = web.application(urls, globals())
data = data()  
data.read() 
myform = form.Form(  
            form.Dropdown('Entidad', data.getEntidad()),
            form.Dropdown('Municipio',data.getMunicipio()) )

class index:
    def GET (datos):
        return render.index()

class acercaDe:
    def GET (datos):
        return render.acercaDe()

class RezagoSocial:
    def GET (datos):
        datos=[]
        with open("datos.json","r")as file:
            datos=json.load(file)
        return render.RezagoSocial(datos)

class busqueda:
    def GET (datos):
        datos=[]
        enti=[]
        with open("datos.json","r")as file:
            datos=json.load(file)
            for row in datos:
                en=row['ent']
                enti.append(en)
                entidad=dict.fromkeys(enti,'vmm')

        datos=entidad

        return render.busqueda(datos)

if __name__ == '__main__':
    app=web.application(urls, globals())
    web.config.debug=True
    app.run()