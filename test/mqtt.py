import time
import random
import paho.mqtt.client as mqtt
import json

# Configuración del cliente MQTT
broker_address = "localhost"  # Cambia a la dirección IP o nombre del servidor MQTT si no está en tu máquina local
broker_port = 1883  # Puerto del servidor MQTT

# Crear un cliente MQTT
client = mqtt.Client()

# Conectar al broker MQTT
client.connect(broker_address, broker_port)

# Función para generar datos de ejemplo
def generar_datos():
    datos = {
        "temperatura": random.uniform(20, 30),
        "humedad": random.uniform(40, 60),
        "presion": random.uniform(1000, 1010)
    }
    return datos

try:
    while True:
        # Generar datos de ejemplo
        datos_ejemplo = generar_datos()
        data_out=json.dumps(datos_ejemplo)
        # Publicar los datos en el tema "datos/ejemplo"
        client.publish("datos/ejemplo", str(data_out))

        print(f"Datos publicados: {datos_ejemplo}")

        # Esperar un tiempo antes de generar nuevos datos
        time.sleep(5)

except KeyboardInterrupt:
    # Cerrar la conexión cuando se interrumpe el script
    client.disconnect()
    print("Conexión MQTT cerrada.")
