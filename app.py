from flask import Flask, jsonify, request
from flask_cors import CORS
from flask import jsonify
import json
from dotenv import load_dotenv
import os
from db_control import crud, mymodels
from module import mdlQuestions,mdlAssessment,mdlArea,mdlHello
import requests
import openai

app = Flask(__name__)
CORS(app)
# CORS(app, resources={r"/api/*": {"origins": os.getenv('ORIGINS')}})   # CORS設定を更新

# 全ての質問データを取得
@app.route("/allQuestions", methods=['GET'])
def read_all_questions():
    return mdlQuestions.getAll(), 200

# アセスメント実施
@app.route("/doAssessment", methods=['POST'])
def do_assessment():
    data = request.get_json()  # JSONデータを取得
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    return mdlAssessment.do(data), 200

# おすすめエリア生成
@app.route("/doResult", methods=['POST'])
def do_result():
    data = request.get_json()  # JSONデータを取得
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    return mdlArea.do(data), 200

### Sample/Test ###
@app.route('/requestGpt', methods=['POST'])
def requestGpt():

    print("requestGpt")
    data = request.get_json()  # JSONデータを取得
    print(data)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    # 'message' プロパティが含まれていることを確認
    message = data.get('message', 'No message provided')

    # OpenAIのAPIキーを設定  
    openai.api_key = os.getenv("OPEN_API_KEY")

    prompt = f"次の質問に対して400文字以内に要約して回答してください。{message}"

    response =  openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt },
        ],
    )
    # 返って来たレスポンスの内容はresponse.choices[0].message.content.strip()に格納されているので、これをoutput_contentに代入
    output_content = response.choices[0].message.content.strip()
    return jsonify({"message": f"{output_content}"})


@app.route('/subHello', methods=['GET'])
def hello():
    return mdlHello.Hello()

@app.route('/hello', methods=['GET'])
def hello_world():
    return mdlHello.Hello()
    # load_dotenv(override=True)
    # # backend.env確認
    # return jsonify(message=os.getenv('TEST_ENV'))

@app.route('/multiply/<int:id>', methods=['GET'])
def multiply(id):
    # print("multiply")
    # idの2倍の数を計算
    # doubled_value = id * 2
    # return jsonify({"doubled_value": doubled_value})
    print("connect db test")
    result = crud.myselect(mymodels.Customers, id)
    print(result)
    return result, 200

@app.route('/echo', methods=['POST'])
def echo():
    print("echo")
    data = request.get_json()  # JSONデータを取得
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    # 'message' プロパティが含まれていることを確認
    message = data.get('message', 'No message provided')
    return jsonify({"message": f"echo: {message}"})

if __name__ == '__main__':
    app.run(debug=True)
