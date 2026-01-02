from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"

def generate_response(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()
    return response.json()["response"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")

    system_prompt = (
        "You are a helpful Python Code Assistant. "
        "Write clean, efficient, well-commented code. "
        "Explain only when necessary."
    )

    full_prompt = f"{system_prompt}\n\nUser:\n{user_input}\n\nAssistant:"

    reply = generate_response(full_prompt)
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
