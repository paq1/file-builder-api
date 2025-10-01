from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from weasyprint import HTML
import tempfile
import os

# Création de l’application FastAPI
app = FastAPI(
    title="HTML to PDF API",
    description="Convertit un fichier HTML en PDF avec WeasyPrint",
    version="1.0.0"
)

@app.post("/convert", summary="Convertir un fichier HTML en PDF")
async def convert_html_to_pdf(file: UploadFile):
    """
    Reçoit un fichier HTML en entrée et retourne un PDF généré.
    """
    # Sauvegarde temporaire du HTML
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp_html:
        content = await file.read()
        tmp_html.write(content)
        tmp_html_path = tmp_html.name

    # Fichier PDF temporaire
    tmp_pdf_path = tmp_html_path.replace(".html", ".pdf")

    # Conversion HTML -> PDF
    HTML(tmp_html_path).write_pdf(tmp_pdf_path)

    # Retourner le PDF au client
    return FileResponse(tmp_pdf_path, media_type="application/pdf", filename="output.pdf")

@app.get("/", summary="Page d'accueil")
async def root():
    return {"message": "Bienvenue dans l'API HTML -> PDF 🚀"}
