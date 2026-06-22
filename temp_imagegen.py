import json, base64, sys, os
from pathlib import Path

config_path = Path.home() / ".gemini-imagegen.json"
config = json.loads(config_path.read_text())

from google import genai
from google.genai import types

client = genai.Client(api_key=config["api_key"])

prompt = """Abstract latent space rendered as a luminous manifold, time-series data points clustering into meaningful geometric patterns, diffusion paths drawn as graceful arcs from noise to structure, purple and violet tones with soft gold highlights, scientific art nouveau style, no text"""

try:
    response = client.models.generate_content(
        model="gemini-3.1-flash-image",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(aspect_ratio="16:9", image_size="1K"),
        ),
    )
except Exception as e:
    print(f"Primary model failed: {e}, trying fallback...")
    response = client.models.generate_content(
        model="gemini-2.0-flash-preview-image-generation",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"],
        ),
    )

output_dir = Path("E:\\Projects\\Books\\TemporalAI/part-4-temporal-representation-learning/images")
output_dir.mkdir(exist_ok=True)
output_path = output_dir / "hero.jpg"

for part in response.candidates[0].content.parts:
    if part.inline_data:
        img_bytes = base64.b64decode(part.inline_data.data)
        output_path.write_bytes(img_bytes)
        print(f"Saved: {output_path}")
        break
else:
    print("ERROR: No image data in response")
    sys.exit(1)
