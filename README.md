# 🛡️ Anonimizador de Documentos

Script interactivo en Python para anonimizar documentos comunes (`.pdf`, `.docx`, `.xlsx`, `.csv`, `.odt`). Sustituye automáticamente datos sensibles como:

- 📧 Correos electrónicos  
- 🆔 DNI y CIF  
- 📞 Teléfonos  
- 🏢 Direcciones  
- 📁 Códigos y expedientes administrativos  
- 📆 Fechas  
- 🔑 Palabras personalizadas definidas por el usuario

---

## ⚙️ Requisitos

Necesitas tener Python 3.12 y `Tkinter`.  
Instala los módulos necesarios con:

```bash
pip install -r requirements.txt


### En Ubuntu (y WSL), se recomienda usar un entorno virtual:

sudo apt install python3.12-venv python3-tk
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


🧪 Uso
### Lanza el script así:

python3 anonimizar.py

Se abrirá un selector gráfico para elegir el archivo a anonimizar y la carpeta de destino.
El archivo anonimizado se guardará allí con _anonimizado añadido al nombre.


📂 Tipos de archivo soportados
.docx

.xlsx

.pdf

.csv

.odt


✏️ Lista personalizada: anonimizables.txt
Puedes crear o editar un archivo llamado anonimizables.txt en el mismo directorio que el script, donde defines palabras o frases personalizadas a anonimizar.
Una por línea, sin comillas.

Ejemplo:

# Añade aquí nombres, ubicaciones o palabras clave a anonimizar manualmente.
# Una palabra o frase por línea. No uses comillas.

Juan Pérez
Madrid
Empresa S.A.
Calle Falsa 123
ejemplo@correo.com
Departamento Legal
NIF12345678


👤 Autor
Jose González Ladrón de Guevara
github.com/jgonzalezguevara



📤 Subir al repositorio

git add .
git commit -m "El texto que quieras"
git push

