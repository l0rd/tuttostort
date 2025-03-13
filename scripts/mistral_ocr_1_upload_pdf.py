from mistralai import Mistral
import os

api_key = os.environ["MISTRAL_API_KEY"]

client = Mistral(api_key=api_key)

uploaded_pdf = client.files.upload(
    file={
        "file_name": "Tuttostort-Num1.pdf",
        "content": open("Tuttostort-Num1.pdf", "rb"),
    },
    purpose="ocr"
)

