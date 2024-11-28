# 診断結果・基礎情報からおすすめエリアを生成します

from flask import jsonify

def do(data):
    # dataから基礎情報取得

    # 基礎情報をDBに登録

    # 診断結果を取得

    # プロンプト作成

    # GPTによる生成

    # 返答の解析

    # おすすめエリアをDBに登録

    # 結果を構成

    return jsonify({'message': '[dummy]Assessment Result'})

    # 参考ソース(GPT)
    # data = request.get_json()  # JSONデータを取得
    # print(data)
    # if data is None:
    #     return jsonify({"error": "Invalid JSON"}), 400
    # # 'message' プロパティが含まれていることを確認
    # message = data.get('message', 'No message provided')

    # # OpenAIのAPIキーを設定  
    # openai.api_key = os.getenv("OPEN_API_KEY")

    # prompt = f"次の質問に対して400文字以内に要約して回答してください。{message}"

    # response =  openai.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[
    #         {"role": "user", "content": prompt },
    #     ],
    # )
    # # 返って来たレスポンスの内容はresponse.choices[0].message.content.strip()に格納されているので、これをoutput_contentに代入
    # output_content = response.choices[0].message.content.strip()
    # return jsonify({"message": f"{output_content}"})