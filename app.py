from flask import Flask, jsonify

# primero creamos una instancia de la aplicacion Flask ediante app = Flask(__name__)

app = Flask(__name__)

#Luego definimos una lista con nombres de personas que puede ser creada dinamicamente pero en este caso
#la definimos nosotros mismos

personas = ["Adriana", "Jesus", "Adrian", "Ana", "Laura", "Alfredo", "Elena",
    "Javier", "Lucia", "Miguel", "Carmen", "Alejandro", "Paula",
    "Fernando", "Rosa", "Pablo", "Isabel", "Daniel", "Eva"]

#Ahora definimos la ruta del endpoint la cual nos servirá para manejar las solicitudes
#tambien es la ruta que nos devolverá la lista de nombres

@app.route('/personas', methods=['GET'])
def obtener_personas():

#Aqui transformamos la lista de nombres en formato JSON y esta la podremos visualizar tanto en nuestro navegador 
# o utilizando Postman por ejemplo.

    return jsonify(personas)

#Ejecutar la aplicacion Flask

if __name__ == '__main__':
    app.run(debug=True)
