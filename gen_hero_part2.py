import json, base64, sys, os
from pathlib import Path

config_path = Path.home() / ".gemini-imagegen.json"
config = json.loads(config_path.read_text())

from google import genai
from google.genai import types

client = genai.Client(api_key=config["api_key"])

prompt = """An elegant antique laboratory filled with brass instruments, pendulums, and mechanical prediction devices, charts and time-series graphs on aged parchment, a vintage statistical model rendered as beautiful clockwork, deep warm amber and brown tones, detailed illustration, no text"""

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
        model="gemini-2.5-flash-preview-05-20",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
        ),
    )

output_dir = Path("E:\\Projects\\Books\\TemporalAI/part-2-classical-forecasting/images")
output_dir.mkdir(exist_ok=True)
output_path = output_dir / "hero.jpg"

saved = False
for part in response.candidates[0].content.parts:
    if part.inline_data:
        img_bytes = base64.b64decode(part.inline_data.data)
        output_path.write_bytes(img_bytes)
        print(f"Saved: {output_path}")
        saved = True
        break

if not saved:
    print("ERROR: No image data found in response")
    sys.exit(1)
