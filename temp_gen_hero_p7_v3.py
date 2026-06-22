import json, base64, sys
from pathlib import Path

config_path = Path.home() / ".gemini-imagegen.json"
config = json.loads(config_path.read_text())

from google import genai
from google.genai import types

client = genai.Client(api_key=config["api_key"])

prompt = """A massive interconnected temporal intelligence system rendered as a luminous city skyline at night, data streams flowing between towers representing different AI modules, spatial and temporal graphs woven into the architecture, electric blue and warm orange, architectural illustration, no text"""

response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents=prompt,
    config=types.GenerateContentConfig(
        response_modalities=["IMAGE", "TEXT"],
    ),
)

output_dir = Path("E:\\Projects\\Books\\TemporalAI/part-7-building-intelligent-systems/images")
output_dir.mkdir(exist_ok=True)
output_path = output_dir / "hero.jpg"

saved = False
for part in response.candidates[0].content.parts:
    if hasattr(part, 'inline_data') and part.inline_data:
        img_bytes = base64.b64decode(part.inline_data.data)
        output_path.write_bytes(img_bytes)
        print(f"Saved: {output_path}")
        saved = True
        break

if not saved:
    print("No image in response")
    for part in response.candidates[0].content.parts:
        print(f"  Part type: {type(part)}, has inline_data: {hasattr(part, 'inline_data')}")
    sys.exit(1)
