import json, base64, sys, os
from pathlib import Path

config_path = Path.home() / ".gemini-imagegen.json"
config = json.loads(config_path.read_text())

from google import genai
from google.genai import types

client = genai.Client(api_key=config["api_key"])

prompt = """Glowing neural network nodes arranged in a flowing temporal sequence, waves of information propagating forward through layers of attention heads, recurrent connections forming spirals of light, deep blue and cyan electric palette, futuristic scientific illustration, no text labels"""

response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=prompt,
    config=types.GenerateContentConfig(
        response_modalities=["IMAGE"],
        image_config=types.ImageConfig(aspect_ratio="16:9", image_size="1K"),
    ),
)

output_dir = Path("E:\\Projects\\Books\\TemporalAI/part-3-temporal-deep-learning/images")
output_dir.mkdir(exist_ok=True)
output_path = output_dir / "hero.jpg"

for part in response.candidates[0].content.parts:
    if part.inline_data:
        img_bytes = base64.b64decode(part.inline_data.data)
        output_path.write_bytes(img_bytes)
        print(f"Saved: {output_path}")
        break
