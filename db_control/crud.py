# uname() error回避
import platform
print("platform", platform.uname())
 

from sqlalchemy import create_engine, insert, delete, update, select
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import json
import pandas as pd

from db_control.connect import engine
from db_control.mymodels import Customers

def myinsert(mymodel, values):
    # session構築
    Session = sessionmaker(bind=engine)
    session = Session()
    print("VALUES:")
    print(values)
    # SQLAlchemy ORMを使ったデータ挿入
    new_customer = Customers(
        customer_name=values["customer_name"],
        age=values["age"],
        gender=values["gender"]
    )
    try:
        # トランザクションを開始
        with session.begin():
            # データの挿入
                session.add(new_customer)
    except sqlalchemy.exc.IntegrityError:
        print("データ挿入に失敗しました")
        session.rollback()

    # query = insert(mymodel).values(values)
    # try:
    #     # トランザクションを開始
    #     with session.begin():
    #         # データの挿入
    #         result = session.execute(query)
    # except sqlalchemy.exc.IntegrityError:
    #     print("一意制約違反により、挿入に失敗しました")
    #     session.rollback()

    new_customer_id = new_customer.customer_id
    # セッションを閉じる
    session.close()
    return new_customer_id
 
def myselect(mymodel, customer_id):
    # session構築
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(mymodel).filter(mymodel.customer_id == customer_id)
    try:
        # トランザクションを開始
        with session.begin():
            result = query.all()
        # 結果をオブジェクトから辞書に変換し、リストに追加
        result_dict_list = []
        for customer_info in result:
            result_dict_list.append({
                "customer_id": customer_info.customer_id,
                "customer_name": customer_info.customer_name,
                "age": customer_info.age,
                "gender": customer_info.gender
            })
        # リストをJSONに変換
        result_json = json.dumps(result_dict_list, ensure_ascii=False)
    except sqlalchemy.exc.IntegrityError:
        print("一意制約違反により、挿入に失敗しました")

    # セッションを閉じる
    session.close()
    return result_json


def myselectAll(mymodel):
    # session構築
    Session = sessionmaker(bind=engine)
    session = Session()
    query = select(mymodel)
    try:
        # トランザクションを開始
        with session.begin():
            df = pd.read_sql_query(query, con=engine)
            result_json = df.to_json(orient='records', force_ascii=False)

    except sqlalchemy.exc.IntegrityError:
        print("一意制約違反により、挿入に失敗しました")
        result_json = None

    # セッションを閉じる
    session.close()
    return result_json

def myupdate(mymodel, values):
    # session構築
    Session = sessionmaker(bind=engine)
    session = Session()

    upd_customer_id = values.pop("customer_id")
    upd_customer_name = values.pop("customer_name")
    upd_age = values.pop("age")
    upd_gender = values.pop("gender")
    query = (
        update(mymodel)
        .where(mymodel.customer_id == upd_customer_id)
        .values(customer_name=upd_customer_name, age=upd_age, gender=upd_gender)
    )
    # クエリの内容をターミナルに出力
    print("Parameters:", query.compile().params)  # クエリに渡されるパラメータを出力
    # クエリ実行
    try:
        # トランザクションを開始
        with session.begin():
            result = session.execute(query)
    except sqlalchemy.exc.IntegrityError:
        print("一意制約違反により、挿入に失敗しました")
        session.rollback()
    # セッションを閉じる
    session.close()
    return "put"

def mydelete(mymodel, customer_id):
    # session構築
    Session = sessionmaker(bind=engine)
    session = Session()
    query = delete(mymodel).where(mymodel.customer_id==customer_id)
    try:
        # トランザクションを開始
        with session.begin():
            result = session.execute(query)
    except sqlalchemy.exc.IntegrityError:
        print("一意制約違反により、挿入に失敗しました")
        session.rollback()
 
    # セッションを閉じる
    session.close()
    return customer_id + " is deleted"