from flask import Flask, jsonify, request, Response
import json
from services.properties_of_num import is_prime, is_perfect, is_armstrong, digit_sum
from services.fun_fact import get_fun_fact
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/debug-routes", methods=["GET"])
def debug_routes():
    return jsonify({"routes": [str(rule) for rule in app.url_map.iter_rules()]}), 200


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "!"}), 200


@app.route("/api/classify_number", methods=["GET"])

def classify_number():
    """Fetch a fun fact about a number from the numbersapi.com"""
    number = request.args.get("number")

    if not number or not number.lstrip('-').isdigit():
        return jsonify({"number": number, "error": True}), 400

    number = int(number)
    
    # Determine number properties
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }
    return Response(
        json.dumps(response, sort_keys=False),
        mimetype="application/json"
    ), 200


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)