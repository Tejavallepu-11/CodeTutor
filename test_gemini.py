import google.generativeai as genai

# ⚠️ Replace with your real API key from MakerSuite
genai.configure(api_key="AIzaSyCNC_Qh1_yNstaVQfFVaUjPcjFTtbCTX6M")
models = genai.list_models(model_name="gemini-2.5-pro")

for model in models:
    print(model.name, "→", model.supported_generation_methods)
