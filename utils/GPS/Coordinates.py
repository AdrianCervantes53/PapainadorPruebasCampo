#Funcion pa obtener cords

def getCoordinates() -> tuple[bool, float, float]:

    #===========# Obtener coordenadas #===========#

    latitud = 1234.56789
    longitud = 12345.67890
    return True, latitud, longitud



if __name__ == "__main__":
    import serial
    import math
    from icecream import ic
    #ser= serial.Serial('COM4',38400)
    ser= serial.Serial('COM5',9600)
    f=1
    contador=0
    radio_tierra=40075000.0/(360*60)

    if ser:
        while True:
            lectura=ser.readline().decode('utf-8').strip()
            ic(lectura)
            lectura=lectura.split(",")

            latitud=(lectura[2])
            longitud=(lectura[4])
            ic(latitud)
            ic(longitud)
            
            #latitud_grados=float(latitud[:2])
            """ latitud_minutos=float((latitud[3:]))
            latitud_gd=latitud_minutos

            #longitud_grados=float(longitud[:3])
            longitud_minutos=float((longitud[3:]))
            longitud_gd=longitud_minutos

            if f==1:
                primera_lat=latitud_gd
                primera_lon=longitud_gd
                f=2

            resta_lat=latitud_gd-primera_lat
            resta_lon=longitud_gd-primera_lon

            distancia=(math.sqrt((latitud_gd-primera_lat)**2+(longitud_gd-primera_lon)**2))*radio_tierra 

            if distancia>=5:
                primera_lat=latitud_gd
                primera_lon=longitud_gd
                contador+=1

            print(f"Latitud: {latitud}, Longitud: {longitud}, Distancia:{distancia}, Bloques: {contador}") """