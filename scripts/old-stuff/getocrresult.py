import os
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

uploaded_pdf_id = "04162fbf-1d5a-4a9c-9e1d-12d531e37571"

signed_url = client.files.get_signed_url(file_id=uploaded_pdf_id)

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type": "document_url",
        "document_url": signed_url.url,
    },
    include_image_base64=True
)

print(ocr_response)
