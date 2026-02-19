import requests

def extract_text_from_image(image_bytes):
    # Example using OCR.space free API
    url = "https://api.ocr.space/parse/image"
    payload = {
        'apikey': 'helloworld',  # free demo key
        'language': 'eng',
    }
    files = {'file': image_bytes}
    response = requests.post(url, files=files, data=payload)
    return response.json()
