import web

# Habilitar sesiones
web.config.debug = False

urls = (
    "/", "Index",
    "/login", "Login",
    "/logout", "Logout",
    "/administracion", "Administracion",
    )

# Crear una aplicación web.py
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"))
render = web.template.render("templates/")


class Index:
    def GET(self):
        logged_in = session.get("logged_in")
        username = session.get("username")
        if session.get("logged_in"):
            return render.index(username)
        else:
            raise web.seeother("/login")

class Administracion:
    def GET(self):
        logged_in = session.get("logged_in")
        username = session.get("username")
        if session.get("logged_in"):
            return render.administracion(username)
        else:
            raise web.seeother("/login")


class Login:
    def GET(self):
        if session.get("logged_in"):
            raise web.seeother("/")
        return render.login()

    def POST(self):
        i = web.input()
        print(f"username: {i.username}")
        print(f"password: {i.password}")
        if i.username == "admin" and i.password == "1234":
            session.logged_in = True
            session.username = i.username
            raise web.seeother("/")
        else:
            return render.login("El nombre de usuario o contraseña son incorrectos")


class Logout:
    def GET(self):
        session.kill()
        raise web.seeother("/login")


if __name__ == "__main__":
    app.run()

