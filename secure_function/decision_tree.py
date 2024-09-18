import requests
import joblib
import requests
import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import pytesseract
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def extract_text_from_url(url: str, max_images=3):
    session = requests.Session()
    retry = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    try:
        response = session.get(url, timeout=5)  # Removed verify=False for security
        response.raise_for_status()  # Raise an error for bad responses (e.g., 404)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract text from HTML
        text = soup.get_text(separator=' ', strip=True)

        # Extract images and use OCR, but limit to max_images
        images = soup.find_all('img')[:max_images]
        for img in images:
            img_url = urljoin(url, img.get('src'))  # Handle relative URLs
            if img_url:
                try:
                    img_response = session.get(img_url, stream=True, timeout=5)
                    img_response.raise_for_status()  # Ensure valid image response
                    img = Image.open(BytesIO(img_response.content))
                    # Perform OCR, add OCR language support if needed (e.g., lang='tha')
                    text += " " + pytesseract.image_to_string(img)
                    img.close()  # Close the image after processing
                except Exception as e:
                    print(f"Error processing image: {e}")
                    continue  # Skip any OCR errors

        return text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return ""
    finally:
        session.close()


# Function to classify a new URL
def classify_url(url: str):

    # Load the model from the uploaded file
    model_filename = os.path.join('ML', 'SVM_with_OCR.pkl')
    # model_filename = 'SVM_with_OCR.pkl'
    pipeline = joblib.load(model_filename)
    print(f"Model loaded from {model_filename}")

    text = extract_text_from_url(url)
    print(f"Extracted text from {url}:\n{text}") #--> ใช้ check ว่าในเว็บได้คำอะไรบ้าง
#    if not text:
#        return "Could not extract text from the URL"  #---> แจ้งเตือนไม่สามารถ extract text ออกมาได้เพราะมีการป้องกัน

    prediction = pipeline.predict([text])
    print(prediction)
    return True if prediction[0] == 1 else False
