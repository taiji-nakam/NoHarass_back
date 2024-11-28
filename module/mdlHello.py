
# モジュール呼び出しテスト

from flask import jsonify

def Hello():
    return jsonify({'message': 'Hello from sub module!'})
