#Lucia Guzman 20262
import hashlib


def leer_hashes(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        return file.read().splitlines()


def leer_palabras(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            return file.read().splitlines()
    except UnicodeDecodeError:
        try:
            with open(archivo, 'r', encoding='latin-1') as file:  
                return file.read().splitlines()
        except Exception as e:
            print(f"Error al leer el archivo {archivo}: {e}")
            return []


def generar_mutaciones(palabras):
    mutaciones = []
    for palabra in palabras:
        mutaciones.append(palabra)  
        mutaciones.append(palabra.upper())  
     
    return mutaciones


def descifrar_hashes(hashes, palabras):
    encontrados = {}
    for palabra in generar_mutaciones(palabras):
        hash_calculado = hashlib.sha1(palabra.encode()).hexdigest()
        if hash_calculado in hashes:
            encontrados[hash_calculado] = palabra
    return encontrados


hashes_objetivo = leer_hashes('target_hashes.txt')
palabras_basicas = leer_palabras('words.txt')
palabras_completas = leer_palabras('realhuman_phill.txt')


palabras_totales = palabras_basicas + palabras_completas


resultados = descifrar_hashes(set(hashes_objetivo), palabras_totales)


for hash_val, pass_val in resultados.items():
    print(f'Hash: {hash_val}, Contraseña: {pass_val}')

def guardar_claves_encontradas(resultados, archivo_salida):
    with open(archivo_salida, 'w', encoding='utf-8') as file:
        for hash_val, pass_val in resultados.items():
            file.write(f'Hash: {hash_val}, Contraseña: {pass_val}\n')

resultados = descifrar_hashes(set(hashes_objetivo), palabras_totales)
guardar_claves_encontradas(resultados, 'claves_encontradas.txt')