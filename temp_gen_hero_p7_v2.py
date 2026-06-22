import json, base64, sys, os, traceback
from pathlib import Path

try:
    config_path = Path.home() / ".gemini-imagegen.json"
    config = json.loads(config_path.read_text())
    print(f"Config loaded, api_key present: {'api_key' in config}", flush=True)

    from google import genai
    from google.genai import types

    client = genai.Client(api_key=config["api_key"])

    prompt = """A massive interconnected temporal intelligence system rendered as a luminous city skyline at night, data streams flowing between towers representing different AI modules, spatial and temporal graphs woven into the architecture, electric blue and warm orange, architectural illustration, no text"""

    print("Trying model: gemini-2.0-flash-preview-image-generation", flush=True)
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-preview-image-generation",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"],
            ),
        )
    except Exception as e1:
        print(f"Model 1 failed: {e1}", flush=True)
        print("Trying model: imagen-3.0-generate-002", flush=True)
        try:
            response = client.models.generate_images(
                model="imagen-3.0-generate-002",
                prompt=prompt,
                config=types.GenerateImagesConfig(
                    number_of_images=1,
                    aspect_ratio="16:9",
                ),
            )
            output_dir = Path("E:\\Projects\\Books\\TemporalAI/part-7-building-intelligent-systems/images")
            output_dir.mkdir(exist_ok=True)
            output_path = output_dir / "hero.jpg"
            img_bytes = response.generated_images[0].image.image_bytes
            output_path.write_bytes(img_bytes)
            print(f"Saved: {output_path}", flush=True)
            sys.exit(0)
        except Exception as e2:
            print(f"Model 2 failed: {e2}", flush=True)
            raise

    output_dir = Path("E:\\Projects\\Books\\TemporalAI/part-7-building-intelligent-systems/images")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "hero.jpg"

    saved = False
    for part in response.candidates[0].content.parts:
        if hasattr(part, 'inline_data') and part.inline_data:
            img_bytes = base64.b64decode(part.inline_data.data)
            output_path.write_bytes(img_bytes)
            print(f"Saved: {output_path}", flush=True)
            saved = True
            break

    if not saved:
        print("No image found in response parts", flush=True)
        print(f"Parts: {response.candidates[0].content.parts}", flush=True)

except Exception as e:
    print(f"ERROR: {e}", flush=True)
    traceback.print_exc()
    sys.exit(1)
