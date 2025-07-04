from flask import Flask, request, jsonify
import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

app = Flask(__name__)

def load_prompt():
    with open("system_prompt.txt", "r", encoding="utf-8") as f:
        return f.read()

@app.route("/vera", methods=["POST"])
def vera():
    user_input = request.json.get("message", "")
    system_prompt = load_prompt()

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )
    return jsonify({"reply": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
