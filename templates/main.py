from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from google import genai
from google.genai import types

app = Flask(__name__)
CORS(app)

client = genai.Client(api_key='AIzaSyD8uPfCT3r0RCU1ze74uxnxEa6EvciESws')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json(force=True)

        user_message = data.get('message')

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=types.Part.from_text(text=user_message)
        )

        return jsonify({
            "response": response.text
        })

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
