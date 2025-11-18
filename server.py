import os
from g4f.api import run_api

port = int(os.environ.get("PORT", 8080))
run_api(host="0.0.0.0", port=port, openai=True)  # <-- це ключове
