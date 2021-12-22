""" importacion librerias necesarias"""
from flask import Flask, request, redirect
app = Flask(__name__)
@app.route("/",methods=["GET"])
   
def index():
    """ ruta index"""
    return redirect("http://localhost/prepara_pedido.html", code=302)
@app.route("/pizza",methods=["GET","POST"])
def mostrar_ruta():
    """ obtiene campos para viajar a otro html"""
    name = request.form.get("nombreCliente")
    surname = request.form.get("apellidosCliente")
    print(name,surname)
    return redirect( "http://localhost/solicita_pedido.html", code=302)
if __name__ == '__main__':
    """ ruta inicial """
    app.run()
 