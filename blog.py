""" Basic blog using webpy 0.3 """
import web
import model

### Url mappings

urls = (
    '/', 'index',
    '/view/(\d+)', 'view',
    '/nuevo', 'nuevo',
    '/eliminar/(\d+)', 'eliminar',
    '/editar/(\d+)', 'editar',
)


### Templates
t_globals = {
    'datestr': web.datestr
}
render = web.template.render('templates', base='base', globals=t_globals)


class index:

    def GET(self):
        """ Show page """
        posts = model.get_posts()
        return render.index(posts)


class view:

    def GET(self, id):
        """ View single post """
        post = model.get_post(int(id))
        return render.view(post)


class nuevo:

    form = web.form.Form(
        web.form.Textbox('carrera', web.form.notnull, 
            size=30,
            description="CARRERA :"),
        web.form.Textarea('descripcion', web.form.notnull, 
            rows=30, cols=80,
            description="DESCRIPCION:"),
        web.form.Button('REGISTRAR'),
    )

    def GET(self):
        form = self.form()
        return render.nuevo(form)

    def POST(self):
        form = self.form()
        if not form.validates():
            return render.nuevo(form)
        model.new_post(form.d.carrera, form.d.descripcion)
        raise web.seeother('/')


class eliminar:

    def POST(self, id):
        model.del_post(int(id))
        raise web.seeother('/')


class editar:

    def GET(self, id):
        post = model.get_post(int(id))
        form = nuevo.form()
        form.fill(post)
        return render.editar(post, form)


    def POST(self, id):
        form = nuevo.form()
        post = model.get_post(int(id))
        if not form.validates():
            return render.editar(post, form)
        model.update_post(int(id), form.d.carrera, form.d.descripcion)
        raise web.seeother('/')


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()