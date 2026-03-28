from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    # Just in case it's not set
    print("Warning: GEMINI_API_KEY environment variable not set.")
genai.configure(api_key=api_key)

# Using gemini-2.5-flash as we determined earlier it works with this API key
model = genai.GenerativeModel("gemini-2.5-flash")

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

if __name__ == "__main__":
    print("Starting Flask server on port 8080...")
    app.run(host="127.0.0.1", port=8080, debug=True)