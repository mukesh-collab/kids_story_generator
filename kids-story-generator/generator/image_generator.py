import requests
import os
import base64
from dotenv import load_dotenv

load_dotenv()
HUGGINGFACE_API_TOKEN = os.getenv("HF_API_TOKEN")

def generate_image(prompt, return_base64=False):
    api_url = "https://api-inference.huggingface.co/models/prompthero/openjourney-v4"
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "inputs": prompt
    }

    response = requests.post(api_url, headers=headers, json=payload)
    content_type = response.headers.get("Content-Type", "")

    if response.status_code == 200 and "image" in content_type:
        image_bytes = response.content

        if return_base64:
            return base64.b64encode(image_bytes).decode("utf-8")

        else:
            return image_bytes
    else:
        # Safely parse error response without assuming it's UTF-8
        try:
            error_json = response.json()
            error_message = error_json.get("error", error_json)
        except Exception:
            error_message = f"Non-JSON error: {response.status_code}"
        raise Exception(f"Image generation failed: {response.status_code} - {error_message}")


