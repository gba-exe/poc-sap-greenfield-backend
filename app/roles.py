from flask import Blueprint, jsonify, request
import pandas as pd
import os

roles_bp = Blueprint('roles', __name__)


def load_roles():
    if os.path.exists("roles.csv"):
        return pd.read_csv("roles.csv")
    return pd.DataFrame(columns=[
        'transaction', 'description', 'functional', 'keyUser'])


def save_roles(df):
    df.to_csv("roles.csv", index=False)


@roles_bp.route('/', methods=['GET'])
def get_roles():
    df = load_roles()
    return jsonify(df.to_dict(orient='records'))


@roles_bp.route('/', methods=['POST'])
def add_roles():
    data = request.get_json()
    if not data or not isinstance(data, list):
        return jsonify({
            "error": "Invalid input. A list of roles was expected."
        }), 400

    required_keys = {'role', 'description', 'keyUser'}
    for role in data:
        if not required_keys.issubset(role):
            return jsonify({
                "error": "Each role must have a role name, " +
                "description and a keyUser."
            }), 400

    df = load_roles()
    new_df = pd.DataFrame(data)
    df = pd.concat([df, new_df], ignore_index=True)
    save_roles(df)

    return jsonify({
        "message": "Roles received successfully",
        "roles": data
    }), 200
