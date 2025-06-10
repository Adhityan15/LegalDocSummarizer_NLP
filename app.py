from flask import Flask, render_template, request
from nlp_engine.extractor import extract_clauses
from nlp_engine.summarizer import summarize_text
import os
import fitz  # PyMuPDF

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}
    if request.method == "POST":
        pdf = request.files["pdf"]
        path = os.path.join(UPLOAD_FOLDER, pdf.filename)
        pdf.save(path)

        # Extract PDF text
        text = ""
        with fitz.open(path) as doc:
            for page in doc:
                text += page.get_text()

        clauses = extract_clauses(text)
        summarized = {k: summarize_text(v) for k, v in clauses.items()}
        result = summarized

    return render_template("index.html", result=result)
