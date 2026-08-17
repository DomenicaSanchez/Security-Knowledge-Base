import base64
import zlib
import json

def decodificar_cookie_flask(cookie_raw: str):
    cookie = cookie_raw.strip()
    
    if not cookie:
        print("[!] Error: No ingresaste ninguna cookie.")
        return

    print("\n[+] Analizando estructura de la cookie...")
    partes = cookie.split('.')
    
    # Detectar si está comprimida (las cookies de Flask comprimidas comienzan con '.')
    comprimida = cookie.startswith('.')

    if comprimida:
        print("[i] Formato detectado: Comprimido con zlib (inicia con '.')")
        if len(partes) < 4:
            print("[!] Error: Estructura incompleta para cookie comprimida. Se esperaban al menos 4 secciones.")
            return
        payload_b64 = partes[1]
    else:
        print("[i] Formato detectado: Estándar (sin compresión inicial)")
        if len(partes) < 3:
            print("[!] Error: Estructura incompleta. Una cookie de Flask requiere al menos 3 secciones separadas por puntos.")
            return
        payload_b64 = partes[0]

    # Reparar relleno (padding) de Base64
    faltante_padding = -len(payload_b64) % 4
    if faltante_padding:
        print(f"[i] Ajustando relleno Base64 (añadiendo {faltante_padding} '=')...")
        payload_b64 += '=' * faltante_padding

    # Decodificación Base64
    try:
        print("[+] Decodificando Base64 URL-safe...")
        datos_bytes = base64.urlsafe_b64decode(payload_b64)
    except Exception as e:
        print(f"[!] Error al decodificar en Base64: {e}")
        return

    # Descompresión zlib si aplica
    if comprimida:
        try:
            print("[+] Descomprimiendo estructura zlib...")
            datos_bytes = zlib.decompress(datos_bytes)
        except Exception as e:
            print(f"[!] Error al descomprimir con zlib: {e}")
            return

    # Decodificación de caracteres e impresión
    try:
        texto_decodificado = datos_bytes.decode('utf-8', errors='replace')
        
        print("\n" + "="*45)
        print("     CONTENIDO DE LA SESIÓN DECODIFICADO     ")
        print("="*45)
        
        # Formatear bonito si el contenido es JSON
        try:
            json_data = json.loads(texto_decodificado)
            print(json.dumps(json_data, indent=4, ensure_ascii=False))
        except json.JSONDecodeError:
            print(texto_decodificado)
            
        print("="*45 + "\n")
        
    except Exception as e:
        print(f"[!] Error al convertir los datos a UTF-8: {e}")

if __name__ == "__main__":
    print("=============================================")
    print("   DECODIFICADOR GENERAL DE COOKIES FLASK   ")
    print("=============================================")
    
    cookie_usuario = input("\nPega la cookie de la sesión web aquí y presiona Enter:\n> ")
    decodificar_cookie_flask(cookie_usuario)
