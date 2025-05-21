import tkinter as tk
from tkinter import filedialog, messagebox
import os
import re
import fitz  # PyMuPDF
from docx import Document
from openpyxl import load_workbook
import csv
from odf.opendocument import load as odf_load
from odf.text import P

def anonimizar_texto(texto, palabras):
    patrones = [
        r'\b\d{8}[A-Za-z]\b',  # DNI
        r'\b[A-Z]\d{8}\b',  # CIF
        r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}\b',  # Email
        r'\+?\d{2,3}[ -]?\d{3}[ -]?\d{3}[ -]?\d{3}',  # Teléfono
        r'\b\d{5}\b',  # Código Postal
        r'Expediente\s*[:\s]?\s*[A-Za-z0-9./-]+',  # Expedientes
        r'\d{4}-\d{2}-\d{2}',  # Fecha ISO
        r'\d{1,2}\s+de\s+\w+\s+de\s+\d{4}',  # Fecha larga
        r'\bES\d{3}\b',  # Código NUTS
        r'\b\d{8}\b',  # Código CPV
        r'Sor Ángela de la Cruz,\s*\d+',  # Dirección específica
        r'ID:\s*\d+-\d+',  # Códigos ID
    ]

    for patron in patrones:
        texto = re.sub(patron, '***', texto, flags=re.IGNORECASE)

    for palabra in palabras:
        texto = re.sub(re.escape(palabra), '***', texto, flags=re.IGNORECASE)

    return texto


def cargar_lista_anonimizables():
    try:
        with open("anonimizables.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def obtener_ruta_salida(filepath, output_dir):
    nombre_archivo = os.path.basename(filepath)
    nombre, extension = os.path.splitext(nombre_archivo)
    return os.path.join(output_dir, f"{nombre}_anonimizado{extension}")

def anonimizar_docx(filepath, palabras, output_dir):
    doc = Document(filepath)
    for p in doc.paragraphs:
        p.text = anonimizar_texto(p.text, palabras)
    doc.save(obtener_ruta_salida(filepath, output_dir))

def anonimizar_xlsx(filepath, palabras, output_dir):
    wb = load_workbook(filepath)
    for sheet in wb.worksheets:
        for row in sheet.iter_rows():
            for cell in row:
                if isinstance(cell.value, str):
                    cell.value = anonimizar_texto(cell.value, palabras)
    wb.save(obtener_ruta_salida(filepath, output_dir))

def anonimizar_pdf(filepath, palabras, output_dir):
    doc = fitz.open(filepath)
    nuevo_doc = fitz.open()
    for page in doc:
        texto = page.get_text()
        texto_anon = anonimizar_texto(texto, palabras)
        nueva_pagina = nuevo_doc.new_page(width=page.rect.width, height=page.rect.height)
        nueva_pagina.insert_text((50, 50), texto_anon, fontsize=11)
    nuevo_doc.save(obtener_ruta_salida(filepath, output_dir))

def anonimizar_csv(filepath, palabras, output_dir):
    salida = obtener_ruta_salida(filepath, output_dir)
    with open(filepath, "r", encoding="utf-8") as f_in, open(salida, "w", encoding="utf-8", newline='') as f_out:
        reader = csv.reader(f_in)
        writer = csv.writer(f_out)
        for row in reader:
            writer.writerow([anonimizar_texto(c, palabras) for c in row])

def anonimizar_odt(filepath, palabras, output_dir):
    odt_doc = odf_load(filepath)
    texto = ""
    for elem in odt_doc.getElementsByType(P):
        texto += elem.firstChild.data if elem.firstChild else ""
    texto_anon = anonimizar_texto(texto, palabras)
    salida = obtener_ruta_salida(filepath, output_dir).replace(".odt", ".txt")
    with open(salida, "w", encoding="utf-8") as f:
        f.write(texto_anon)

def seleccionar_archivo():
    filepath = filedialog.askopenfilename(filetypes=[
        ("Documentos soportados", "*.docx *.xlsx *.pdf *.csv *.odt")
    ])
    if not filepath:
        return

    output_dir = filedialog.askdirectory(title="Selecciona carpeta de destino")
    if not output_dir:
        return

    try:
        palabras = cargar_lista_anonimizables()
        ext = filepath.lower()
        if ext.endswith(".docx"):
            anonimizar_docx(filepath, palabras, output_dir)
        elif ext.endswith(".xlsx"):
            anonimizar_xlsx(filepath, palabras, output_dir)
        elif ext.endswith(".pdf"):
            anonimizar_pdf(filepath, palabras, output_dir)
        elif ext.endswith(".csv"):
            anonimizar_csv(filepath, palabras, output_dir)
        elif ext.endswith(".odt"):
            anonimizar_odt(filepath, palabras, output_dir)

        messagebox.showinfo("Éxito", f"Archivo anonimizado guardado correctamente.")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    root.withdraw()
    seleccionar_archivo()

if __name__ == "__main__":
    main()
