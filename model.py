import web, datetime

db = web.database(dbn='mysql', db='carrerasUniversitarias',pw='utec', user='root')

def get_registro():
    return db.select('registrosCU', order='id DESC')

def get_registro(id):
    try:
        return db.select('registrosCU', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def nuevo_registro(carrera, descripcion):
    db.insert('registrosCU', carrera=carrera, descripcion=descripcion, periodo=datetime.datetime.utcnow())

def eliminar_registro(id):
    db.eliminar('registrosCU', where="id=$id", vars=locals())

def update_registro(id, carrera, descripcion):
    db.update('registrosCU', where="id=$id", vars=locals(),
        carrera=carrera, descripcion=descripcion)