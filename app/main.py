from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import pdfkit
import tempfile
import os

app = FastAPI()

@app.post("/convert")
async def convert_html_to_pdf(file: UploadFile = File(...)):
    # Lire contenu HTML
    contents = await file.read()

    # Créer fichiers temporaires
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as temp_html:
        temp_html.write(contents)
        temp_html_path = temp_html.name

    output_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    output_pdf_path = output_pdf.name
    output_pdf.close()

    # Convertir en PDF
    pdfkit.from_file(temp_html_path, output_pdf_path)

    # Supprimer le HTML temporaire
    os.remove(temp_html_path)

    # Retourner le PDF
    return FileResponse(output_pdf_path, media_type="application/pdf", filename="output.pdf")
