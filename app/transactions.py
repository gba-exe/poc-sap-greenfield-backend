from flask import Blueprint, jsonify, request
import pandas as pd
import os

transactions_bp = Blueprint('transactions', __name__)


def load_transactions():
    if os.path.exists("transactions.csv"):
        return pd.read_csv("transactions.csv")
    return pd.DataFrame(columns=[
        'transaction', 'description', 'functional', 'keyUser'])


def save_transactions(df):
    df.to_csv("transactions.csv", index=False)


@transactions_bp.route('/', methods=['GET'])
def get_transactions():
    df = load_transactions()
    return jsonify(df.to_dict(orient='records'))


@transactions_bp.route('/code', methods=['GET'])
def get_transaction_codes():
    df = load_transactions()
    return jsonify(df['transaction'].tolist())


@transactions_bp.route('/', methods=['POST'])
def add_transactions():
    data = request.get_json()
    if not data or not isinstance(data, list):
        return jsonify({
            "error": "Invalid input. A list of transactions was expected."
        }), 400

    required_keys = {'transaction', 'description', 'functional', 'keyUser'}
    for transaction in data:
        if not required_keys.issubset(transaction):
            return jsonify({
                "error": "Each transaction must have a transaction, " +
                "description, functional, and a keyUser."
            }), 400

    df = load_transactions()
    new_df = pd.DataFrame(data)
    df = pd.concat([df, new_df], ignore_index=True)
    save_transactions(df)

    return jsonify({
        "message": "Transactions received successfully",
        "transactions": data
    }), 200
