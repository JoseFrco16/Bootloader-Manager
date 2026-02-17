import serial

# Abrir puerto
ser = serial.Serial(
    port='/dev/ttyUSB0',   # En Linux
    # port='COM3',         # En Windows
    baudrate=9600,
    timeout=1
)

# Enviar datos
ser.write(b'Hola UART\n')

# Leer datos
data = ser.readline()
print(data)

# Cerrar puerto
ser.close()