import requests
import re
from bs4 import BeautifulSoup

def extract_text_content(base_url: str) -> str:
    try:
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        words = re.findall(r'\b\w+\b', text.lower())
        common_words = set(["the", "and", "to", "of", "a", "in", "for", "is", "on", "that", "by", "this", "with", "i", "you", "it", "not", "or", "be", "are", 'เป็น', 'อยู่', 'คือ', 'หรือ', 'และ', 'ใน'])
        filtered_words = [word for word in words if word not in common_words]
        return ' '.join(filtered_words)
    except Exception as e:
        print(f'Error fetching {base_url}: {e}')
        return ''


# Function to classify URL based on extracted features
def classify_url_content(base_url: str) -> bool:
    content = extract_text_content(base_url)
    if not content:
        print("Unable to classify URL due to content extraction failure.")
        return False

    # Implement your classification logic here based on extracted features
    # Example classification based on specific features (mock-up)
    features = {
        'ครสมาช': content.count('ครสมาช'),
        'à¹': content.count('à¹'),
        '2024': content.count('2024'),
        'continue': content.count('continue'),
        'vite': content.count('vite'),
        'อมข': content.count('อมข'),
        'กหวยไม': content.count('กหวยไม'),
        'tradingfutures': content.count('tradingfutures'),
        'บาทละ': content.count('บาทละ'),
        '8a292ab70b3fc3aa': content.count('8a292ab70b3fc3aa'),
        'discount': content.count('discount'),
        '120': content.count('120'),
        'นธ': content.count('นธ'),
        # Add more features as needed based on your classification model
    }

    # Example classification rules (mock-up)
    if features['ครสมาช'] <= 0.5:
        if features['à¹'] <= 10.5:
            if features['2024'] <= 0.5:
                if features['continue'] <= 0.5:
                    if features['vite'] <= 0.5:
                        if features['อมข'] <= 0.5:
                            if features['กหวยไม'] <= 0.5:
                                if features['tradingfutures'] <= 1.0:
                                    if features['บาทละ'] <= 0.5:
                                        if features['8a292ab70b3fc3aa'] <= 0.5:
                                            return True
                                        else:  # if features['8a292ab70b3fc3aa'] > 0.5
                                            return False
                                    else:  # if features['บาทละ'] > 0.5
                                        return False
                                else:  # if features['tradingfutures'] > 1.0
                                    return False
                            else:  # if features['กหวยไม'] > 0.5
                                return False
                        else:  # if features['อมข'] > 0.5
                            return False
                    else:  # if features['vite'] > 0.5
                        return False
                else:  # if features['continue'] > 0.5
                    if features['discount'] <= 0.5:
                        return False
                    else:  # if features['discount'] > 0.5
                        return True
            else:  # if features['2024'] > 0.5
                return True
        else:  # if features['à¹'] > 10.5
            if features['120'] <= 0.5:
                return False
            else:  # if features['120'] > 0.5
                return True
    else:  # if features['ครสมาช'] > 0.5
        if features['นธ'] <= 2.5:
            return False
        else:  # if features['นธ'] > 2.5
            return True