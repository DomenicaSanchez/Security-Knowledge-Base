import os

# Buscamos el archivo flag.txt en el directorio actual
flag_file = 'flag.txt'

if os.path.exists(flag_file):
    with open(flag_file, 'r') as f:
        # Al imprimirlo, el contenido aparecerá en tu conexión de netcat
        print("\n--- INICIO DE LA FLAG ---")
        print(f.read())
        print("--- FIN DE LA FLAG ---\n")
else:
    print("No se encontró el archivo flag.txt en este directorio.")
