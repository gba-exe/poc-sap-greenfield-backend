from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask (__name__)
CORS(app)

df_transactions = pd.read_csv("transactions.csv", delimiter=";")

@app.route("/transactions", methods=["GET"])
def transactions():
    print(df_transactions)
    return jsonify(df_transactions.to_dict())

@app.route("/transactions/code", methods=["GET"])
def transactions_code():
    print(df_transactions)
    return jsonify(df_transactions["Transaction Code"].to_list())


if __name__ == "__main__":
    app.run(debug=True)