 # Controla tus multas

**Que es controla tus multas?**

El presente proyecto elaborado para el fin de modulo “Tratamiento de datos”, parte de la maestría en Ciberseguridad impartida por la Universidad Internacional del Ecuador, parte de una necesidad que tienen los conductores ecuatorianos a nivel de notificación de multas o infracciones de transito registradas a nivel nacional.

**Problemática**

En la actualidad en el Ecuador existen varias formas de realizar control a los vehículos de transporte de cualquier tipo que este sea. Cuando un conductor incurre en una falta esta debe ser notificada por la autoridad competente para su impugnación en los siguientes 3 días hábiles, de esta forma el conductor tiene la oportunidad de librarse o en todo caso pagar a tiempo el valor correspondiente a la falta. Lamentablemente se han implementado sistemas que realizan la multa automáticamente pero su gestión no realiza la notificación oportunamente, llegando incluso a reportarse después de años. 

La ANT pone a disposición de los usuarios un sistema para la consulta de estos valores ya sea por placa, cédula, ruc o pasaporte el sistema de consulta, el inconveniente es que si no ingresas a realizar la consulta no recibes ninguna notificación adicional. El link para su ingreso es el siguiente: <https://consultaweb.ant.gob.ec/PortalWEB/paginas/clientes/clp_criterio_consulta.jsp>

**Propuesta**

Este programa desarrolla una herramienta que a través del scraping nos permita revisar constantemente si hemos recibido una multa en la ANT mediante la revisión de los datos obtenidos en una web personal,  via correo electrónico o Whatsapp.

A continuación, detallamos un esquema de las conexiones a realizar:
![Picture1.png](Images%2FPicture1.png)

**Instalación**

Es necesario tener instalado la librería Flask pymongo, se lo puede realizar con el siguiente comando en la consola

    pip install Flask pymongo

**Desarrollo**

Para realizar la extracción de la data se ha trabajado en las siguientes actividades:

**1. Desarollar una aplicación flask que se conecte a la base de datos generada.**

    # Configuramos la base de datos
    cliente = MongoClient('mongodb://localhost:27017/')
    db = cliente['PruebaFinal']
    base = db['citaciones']
    
    @app.route('/')
    def index():
        # Consulta la base de datos y devuelve los datos
        datos = list(base.find())
        return render_template('index.html', datos=datos)
    
    @app.route('/api/datos')
    def obtener_datos():
        # Consulta la base de datos y devuelve los datos en formato JSON
        datos = list(base.find({}, {'infraccion': 0,
        'entidad': 1,
        'citacion': 2,
        'placa': 3,
        'fechaemision': 4,
        'fechanotificacion': 5,
        'sancion': 6,
        'puntos': 7,
        'multa': 8,
        'remision': 9,
        'totalpagar': 10,
        'articulo': 11}))
        return jsonify(datos)


**2. Elaborar un cuadro de resumen en el cual se pueda visualizar las multas existentes del usuario.**

    <!DOCTYPE html>
    <html>
    <head>
        <title>Citaciones existentes</title>
    </head>
    <body>
        <h1>Datos obtenidos</h1>
        <ul>
            {% for dato in datos %}
                <li>
                    Número de infracción: {{dato.infraccion}},
                    Entidad responsable: {{dato.entidad}},
                    No. citación: {{dato.citacion}},
                    Placa del vehículo: {{dato.placa}},
                    Fecha de emisión: {{dato.fechaemision}},
                    Fecha de notificación: {{dato.fechanotificacion}},
                    Sanción: {{dato.sancion}},
                    Puntos reducidos: {{dato.puntos}},
                    Valor multa: {{dato.multa}},
                    Fecha remisión: {{dato.remision}},
                    Total a pagar: {{dato.totalpagar}},
                    Articulo infringido: {{dato.articulo}}
                </li>
            {% endfor %}
        </ul>
    </body>
    </html>

**Alcance**

En esta primera etapa se ha registrado la solicitud y almacenamiento de la información, la misma que será notificada al usuario final mediante la visualización WEB. En un siguiente scoope se tratará la notificación mediante correo y Whatsapp.


