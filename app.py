import web

# Habilitar sesiones
web.config.debug = False

urls = (
    '/', 'index',
    '/login', 'login'
)

# Crear una aplicación web.py
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'))
render = web.template.render('templates/')

class index:
    def GET(self):
        if session.get('logged_in'):
            return render.index()
        else:
            raise web.seeother('/login')

class login:
    def GET(self):
        if session.get('logged_in'):
            raise web.seeother('/')
        return render.login("hola")

    def POST(self):
        i = web.input()
        if i.username == 'admin' and i.password == 'admin':
            session.logged_in = True
            raise web.seeother('/')
        else:
            return render.login("El nombre de usuario o contraseña son incorrectos")

if __name__ == '__main__':
    app.run()
