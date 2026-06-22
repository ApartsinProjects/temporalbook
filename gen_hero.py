import json, base64, sys
from pathlib import Path

config_path = Path.home() / ".gemini-imagegen.json"
config = json.loads(config_path.read_text())

from google import genai
from google.genai import types

client = genai.Client(api_key=config["api_key"])

prompt = """Abstract latent space rendered as a luminous manifold, time-series data points clustering into meaningful geometric patterns, diffusion paths drawn as graceful arcs from noise to structure, purple and violet tones with soft gold highlights, scientific art nouveau style, no text"""

models_to_try = [
    "gemini-3.1-flash-image-preview",
    "gemini-2.5-flash-image",
    "gemini-2.0-flash-preview-image-generation",
]

response = None
for model in models_to_try:
    try:
        print(f"Trying model: {model}", flush=True)
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"],
                image_config=types.ImageConfig(aspect_ratio="16:9", image_size="1K"),
            ),
        )
        print(f"Success with model: {model}", flush=True)
        break
    except Exception as e:
        print(f"Model {model} failed: {e}", flush=True)

if response is None:
    print("All models failed", flush=True)
    sys.exit(1)

output_dir = Path(r"E:\Projects\Books\TemporalAI\part-4-temporal-representation-learning\images")
output_dir.mkdir(exist_ok=True)
output_path = output_dir / "hero.jpg"

found = False
for part in response.candidates[0].content.parts:
    if part.inline_data:
        img_bytes = base64.b64decode(part.inline_data.data)
        output_path.write_bytes(img_bytes)
        print(f"Saved: {output_path}", flush=True)
        found = True
        break

if not found:
    print("No image data found in response parts", flush=True)
    for i, part in enumerate(response.candidates[0].content.parts):
        print(f"Part {i}: type={type(part)}, has inline_data={part.inline_data is not None}", flush=True)
    sys.exit(1)
