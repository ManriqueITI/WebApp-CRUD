import web
import json

render = web.template.render('views/')

urls = (
    '/index','index',
    '/acercaDe','acercaDe',
    '/RezagoSocial','RezagoSocial'
)

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

if __name__ == '__main__':
    app=web.application(urls, globals())
    web.config.debug=True
    app.run()