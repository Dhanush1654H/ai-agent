from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set!")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-pro")

@app.route("/")
def home():
    return "AI Agent Running 🚀"

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    text = data.get("text", "")
    
    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        response = model.generate_content(f"Summarize this:\n{text}")
        return jsonify({"summary": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    print(f"Starting server on port {port}...")
    app.run(host="0.0.0.0", port=port)