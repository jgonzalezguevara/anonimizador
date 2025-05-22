🛡️ Document Anonymizer
Interactive Python script to anonymize common documents (.pdf, .docx, .xlsx, .csv, .odt). Automatically replaces sensitive data such as:

📧 Email addresses

🆔 National IDs and company tax numbers

📞 Phone numbers

🏢 Addresses

📁 Administrative codes and case numbers

📆 Dates

🔑 User-defined custom words

⚙️ Requirements
You need Python 3.12 and Tkinter.
Install the required modules with:

pip install -r requirements.txt

On Ubuntu (and WSL), it’s recommended to use a virtual environment:
sudo apt install python3.12-venv python3-tk
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

🧪 Usage

Run the script like this:
python3 anonimizar.py

A graphical file selector will open to choose the file to anonymize and the destination folder.
The anonymized file will be saved there with _anonimizado added to the name.

📂 Supported file types
.docx
.xlsx
.pdf
.csv
.odt

✏️ Custom list: anonimizables.txt
You can create or edit a file called anonimizables.txt in the same directory as the script, where you define custom words or phrases to anonymize.
One per line, no quotation marks.

Example:

Add names, locations or keywords to anonymize manually.
One word or phrase per line. Do not use quotes.
Juan Pérez
Madrid
Empresa S.A.
Calle Falsa 123
ejemplo@correo.com
Departamento Legal
NIF12345678

👤 Author
Jose González Ladrón de Guevara
github.com/jgonzalezguevara

