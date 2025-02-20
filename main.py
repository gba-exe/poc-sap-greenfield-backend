from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask (__name__)
CORS(app)

df_transactions = pd.DataFrame(columns=['name', 'description', 'functional', 'keyUser'])

@app.route("/transactions", methods=["GET"])
def transactions_get():
    return jsonify(df_transactions.to_dict(orient="records"))

@app.route("/transactions/code", methods=["GET"])
def transactions_code():
    return jsonify(df_transactions["Transaction Code"].to_list())

@app.route("/transactions", methods=["POST"])
def transactions_post():
    global df_transactions
    transactions = request.get_json()

    if not transactions or not isinstance(transactions, list):
        print("a")
        return jsonify({"error": "Invalid input. A list of transactions was expected."}), 400

    required_keys = {'name', 'description', 'functional', 'keyUser'}

    for transaction in transactions:
        if not required_keys.issubset(transaction):
            print("b")
            return jsonify({"error": "Each transaction must have a name, description, functional and a keyUser."}), 400

    new_transactions = pd.DataFrame(transactions)
    df_transactions = pd.concat([df_transactions, new_transactions], ignore_index=True)

    return jsonify({"message": "Transactions recieved successfully", "transactions": transactions}), 200


if __name__ == "__main__":
    app.run(debug=True)