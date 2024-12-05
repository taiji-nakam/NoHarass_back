# 質問項目から診断を実施します

from flask import jsonify
from db_control import crud, mymodels

def do(data):
    # dataから質問回答を取得
    print(data)
    
    # 診断をDBに登録
    new_assessment_id = crud.insert_assessment()

    # 診断回答をDBに登録


    # 診断結果をDBに登録
    categoryAverages = data['categoryAverages']
    
    return jsonify({'assessment_id': new_assessment_id})

def getResult(assessmentId):
    # dataから質問回答を取得
    print('ID:')
    print(assessmentId)
    # 診断結果取得
    return crud.select_assessment_result(assessmentId)