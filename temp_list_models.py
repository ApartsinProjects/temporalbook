import json
from pathlib import Path

config_path = Path.home() / ".gemini-imagegen.json"
config = json.loads(config_path.read_text())

from google import genai

client = genai.Client(api_key=config["api_key"])

for m in client.models.list():
    if "image" in m.name.lower() or "imagen" in m.name.lower():
        print(m.name, getattr(m, 'supported_actions', None) or getattr(m, 'supported_generation_methods', None))
