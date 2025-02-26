from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

df_transactions = pd.DataFrame(
    columns=['transaction', 'description', 'functional', 'keyUser'])

df_roles = pd.DataFrame(
    columns=['role', 'keyUser'])

df_csv = pd.read_csv("transactions.csv")
df_transactions = pd.concat([df_transactions, df_csv], ignore_index=True)


@app.route("/transactions", methods=["GET"])
def transactions_get():
    return jsonify(df_transactions.to_dict(orient="records"))


@app.route("/transactions/code", methods=["GET"])
def transactions_code():
    return jsonify(df_transactions["transaction"].to_list())


@app.route("/transactions", methods=["POST"])
def transactions_post():
    global df_transactions
    transactions = request.get_json()

    print(transactions)
    if not transactions or not isinstance(transactions, list):
        return jsonify({
            "error": "Invalid input. A list of transactions was expected."
        }), 400

    required_keys = {'transaction', 'description', 'functional', 'keyUser'}

    for transaction in transactions:
        if not required_keys.issubset(transaction):
            return jsonify({
                "error": "Each transaction must have a transaction, " +
                "description, functional and a keyUser."
            }), 400

    new_transactions = pd.DataFrame(transactions)
    df_transactions = pd.concat(
        [df_transactions, new_transactions], ignore_index=True)

    return jsonify({
        "message": "Transactions recieved successfully",
        "transactions": transactions
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
