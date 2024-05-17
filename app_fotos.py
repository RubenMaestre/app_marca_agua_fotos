import os
import shutil
from PIL import Image, ImageDraw, ImageFont
import winshell

def aplicar_marca_agua(imagen, texto):
    ancho, alto = imagen.size
    if imagen.mode != 'RGBA':
        imagen = imagen.convert('RGBA')

    try:
        font = ImageFont.truetype("arial.ttf", 72)
    except IOError:
        print("No se pudo cargar la fuente. Usando fuente por defecto.")
        font = ImageFont.load_default(size=72)

    textlayer = Image.new('RGBA', imagen.size, (255, 255, 255, 0))
    textdraw = ImageDraw.Draw(textlayer)
    textbbox = textdraw.textbbox((0, 0), texto, font=font)
    textwidth = textbbox[2] - textbbox[0]
    textheight = textbbox[3] - textbbox[1]

    # Posición
    x_center = (ancho - textwidth) / 2
    y_center = (alto - textheight) / 2

    borde_offset = 2  # Aquí tamaño borde
    color_borde = (0, 0, 0, 255)  
    color_texto = (255, 255, 255, 162)  # Damos transparencia

    for dx in [-borde_offset, 0, borde_offset]:
        for dy in [-borde_offset, 0, borde_offset]:
            textdraw.text((x_center + dx, y_center + dy), texto, font=font, fill=color_borde)

    textdraw.text((x_center, y_center), texto, font=font, fill=color_texto)
    imagen = Image.alpha_composite(imagen, textlayer)

    if imagen.mode == 'RGBA':
        imagen = imagen.convert('RGB')

    return imagen

def procesar_carpetas(carpeta_origen, carpeta_destino):
    print(f"Procesando carpetas desde {carpeta_origen} hasta {carpeta_destino}")
    for directorio, subdirs, archivos in os.walk(carpeta_origen):
        if not archivos:
            continue
        nombre_carpeta = os.path.basename(directorio)
        ruta_destino = os.path.join(carpeta_destino, nombre_carpeta)
        if not os.path.exists(ruta_destino):
            os.makedirs(ruta_destino)

        for archivo in archivos:
            if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                ruta_completa = os.path.join(directorio, archivo)
                imagen = Image.open(ruta_completa)
                imagen_con_marca = aplicar_marca_agua(imagen, nombre_carpeta)
                
                ruta_imagen_destino = os.path.join(ruta_destino, archivo)
                imagen_con_marca.save(ruta_imagen_destino)
                print(f"Archivo guardado: {ruta_imagen_destino}")

    limpiar_carpeta(carpeta_origen)

def limpiar_carpeta(carpeta):
    for nombre_archivo in os.listdir(carpeta):
        archivo_path = os.path.join(carpeta, nombre_archivo)
        try:
            if os.path.isfile(archivo_path) or os.path.islink(archivo_path):
                os.unlink(archivo_path)
            elif os.path.isdir(archivo_path):
                shutil.rmtree(archivo_path)
            print(f"Eliminado: {archivo_path}")
        except Exception as e:
            print(f"Fallo al eliminar {archivo_path}. Razón: {e}")

# Aquí podemos encontrarnos que igual el escritorio tiene diferentes nombres, y creamos nuestras carpetas de origen y destino
def main():
    escritorio = winshell.desktop()

    # Aquí podemos modificar el nombre de las carpetas
    carpeta_origen = os.path.join(escritorio, 'MARCA_DE_AGUA', 'fotos_sin')
    carpeta_destino = os.path.join(escritorio, 'MARCA_DE_AGUA', 'fotos_con')
    os.makedirs(carpeta_origen, exist_ok=True)
    os.makedirs(carpeta_destino, exist_ok=True)

    # Procesamos
    print(f"Procesando carpetas desde {carpeta_origen} hasta {carpeta_destino}")
    procesar_carpetas(carpeta_origen, carpeta_destino)

if __name__ == "__main__":
    main()
