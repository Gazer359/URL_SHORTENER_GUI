
# 🧩 Acortador de URLs con Interfaz Gráfica (Tkinter)

Esta aplicación de escritorio desarrollada en Python permite acortar enlaces utilizando la API de [TinyURL](https://tinyurl.com/), todo desde una interfaz gráfica creada con `Tkinter`.

---


## 🚀 Características

- ✅ Acorta URLs automáticamente usando TinyURL.
- ✅ Interfaz gráfica amigable con campos de entrada y botones intuitivos.
- ✅ Copia al portapapeles con un clic.
- ✅ Limpia campos con un botón.
- ✅ Muestra una versión "engañosa" del enlace para pruebas (agregando una URL aleatoria como parámetro).
- ❌ Manejo de errores en caso de conexión fallida o URL inválida.

---

## 🛠️ Tecnologías Usadas

- Python 3.x
- Tkinter (Interfaz gráfica)
- Requests (para realizar peticiones HTTP)

---

## Autor

- [@Gazer359](https://www.github.com/Gazer359)

---

## 📂 Estructura de Archivos

- ├── img/
- │   └── url.png        # Icono de la ventana
- ├── app.py             # Archivo principal de la aplicación
- └── README.md          # Este archivo


---

# ⚠️ Nota de seguridad

La funcionalidad de crear URLs "engañosas" al final es solo para propósitos educativos o de prueba. No se recomienda su uso para fines maliciosos o engañar a otros usuarios.

---

## 🧠 Como usar 
- Ingresa una URL válida (debe comenzar con http://, https:// o www.).

- Presiona el botón "Acortar URL".

- Se mostrará el resultado en el cuadro de texto:

- La URL acortada real.

- Una versión "engañosa" que incluye una URL adicional como parámetro (solo para propósitos ilustrativos).

- Puedes copiar el resultado al portapapeles con el botón "Copiar".

- Usa el botón "Clear" para limpiar los campos.

---

## 📦 Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/Gazer359/URL_SHORTENER_GUI.git
cd URL_SHORTENER_GUI.git

