import os,json
from mistralai import Mistral, DocumentURLChunk, OCRResponse


def replace_images_in_markdown(markdown_str: str, images_dict: dict) -> str:
    for img_name, base64_str in images_dict.items():
        markdown_str = markdown_str.replace(f"![{img_name}]({img_name})", f"![{img_name}]({base64_str})")
    return markdown_str

def get_combined_markdown(ocr_response: OCRResponse) -> str:
  markdowns: list[str] = []
  for page in ocr_response.pages:
    image_data = {}
    for img in page.images:
      image_data[img.id] = img.image_base64
    markdowns.append(replace_images_in_markdown(page.markdown, image_data))


  return "\n\n".join(markdowns)

api_key = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

uploaded_pdf_id = "04162fbf-1d5a-4a9c-9e1d-12d531e37571"

signed_url = client.files.get_signed_url(file_id=uploaded_pdf_id)

# ocr_response = client.ocr.process(
#     model="mistral-ocr-latest",
#     document={
#         "type": "document_url",
#         "document_url": signed_url.url,
#     },
#     include_image_base64=True
# )

# print(ocr_response)

pdf_response = client.ocr.process(
    document = DocumentURLChunk(document_url = signed_url.url),
    model="mistral-ocr-latest",
    include_image_base64=True
)

response_dict = json.loads(pdf_response.json())
json_string = json.dumps(response_dict, indent=4)

file = open('pdf_response.json', 'w')
file.write(json_string)
file.close()

md = get_combined_markdown(pdf_response)

file = open('ocr_result.md', 'w')
file.write(md)
file.close()
