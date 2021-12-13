from flask import Flask, render_template, request,redirect
 
 

app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    return render_template('prepara_pedido.html')

 

@app.route("/pizza",methods=["GET","POST"])
def mostrarRuta():   
  name = request.form.get("nombreCliente")
  surname = request.form.get("apellidosCliente")
  print(name,surname)
  return redirect ("http://localhost/templates/solicita_pedido")
  
       
   
    


if __name__ == '__main__':
 app.run(debug=True,port=5000)