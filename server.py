import os
from g4f.api import run_api

g4f.Provider.ProviderList.pop("PuterJS", None)

port = int(os.environ.get("PORT", 8080))
run_api(host="0.0.0.0", port=port)

