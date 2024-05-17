# Marca de Agua Automática

Este programa permite aplicar una marca de agua a fotos de manera automática. Al ejecutarlo, creará una estructura de carpetas específica en tu escritorio y procesará las fotos según el nombre de las carpetas que determines.

## Estructura de Carpetas

Al ejecutar el programa por primera vez, se crearán las siguientes carpetas en tu escritorio:



- `fotos_sin`: Aquí debes crear subcarpetas con el nombre del proveedor que quieres que aparezca como marca de agua en las fotos. 
- `fotos_con`: Aquí se guardarán las fotos con la marca de agua aplicada.

## Instrucciones de Uso

1. **Preparar las Fotos**: Dentro de la carpeta `fotos_sin`, crea subcarpetas con el nombre que quieres usar como marca de agua para cada conjunto de fotos. Por ejemplo:


Descarga las fotos de WhatsApp o de cualquier otra fuente y colócalas en la subcarpeta correspondiente.

2. **Ejecutar el Programa**: Dentro de la carpeta `app`, encontrarás un ejecutable llamado `app_fotos.exe`. Ejecútalo en Windows. El programa procesará todas las subcarpetas dentro de `fotos_sin`, aplicará la marca de agua correspondiente y guardará las fotos resultantes en la carpeta `fotos_con`.

3. **Resultado**: Una vez que el programa termine de ejecutar:
- Las fotos con la marca de agua aplicada estarán en `fotos_con`.
- Todas las carpetas y fotos dentro de `fotos_sin` serán eliminadas.

## Detalles Técnicos

### Requisitos

- Sistema operativo: Windows
- Librerías: PIL (Python Imaging Library)

### Funcionamiento Interno

1. **Creación de Carpetas**: Si no existen, el programa creará las carpetas `MARCA_DE_AGUA`, `fotos_sin`, y `fotos_con` en el escritorio.
2. **Procesamiento de Fotos**: El programa recorrerá cada subcarpeta dentro de `fotos_sin`, aplicará la marca de agua usando el nombre de la subcarpeta, y guardará las fotos resultantes en `fotos_con`.
3. **Limpieza**: Al finalizar el procesamiento, el programa eliminará todas las carpetas y fotos dentro de `fotos_sin`.

## Ejecución

Para ejecutar el programa, simplemente haz doble clic en `app_fotos.exe` dentro de la carpeta `app`.

## Notas Adicionales

- Si el programa no encuentra la fuente `arial.ttf`, utilizará una fuente predeterminada.
- Asegúrate de que las fotos estén en formatos compatibles: `.png`, `.jpg`, `.jpeg`, `.bmp`.

---

¡Gracias por usar nuestro programa de Marca de Agua Automática!
