import sys

def escribir_config_mqtt(campos):
    # Formatear el bloque MQTT con los campos recibidos
    bloque_mqtt = f'''
[[inputs.mqtt_consumer]]
  servers = ["tcp://mqtt:1883"]
  topics = ["datos/#"]
  data_format = "json"
  json_string_fields = {campos}
'''

    # Escribir el bloque en el archivo telegraf.conf
    with open('../telegraf/telegraf.conf', 'a') as archivo:
        archivo.write(bloque_mqtt)

if __name__ == '__main__':
    # Obtener los argumentos por línea de comandos
    if len(sys.argv) != 2:
        print("Uso: python script.py campo1,campo2,campo3,...")
        sys.exit(1)

    argumento = sys.argv[1]
    campos = argumento.split(',')

    # Llamar a la función para escribir el bloque MQTT en telegraf.conf
    escribir_config_mqtt(campos)

    print("Bloque MQTT escrito correctamente en telegraf.conf.")
