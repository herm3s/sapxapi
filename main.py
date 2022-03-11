from flask import Flask, request, jsonify  # เพิ่ม request

import json
main = Flask(__name__)
mats = []

@main.route('/')
def hello():
    return "ทดสอบ SAP Send API"

@main.route('/mat', methods=['POST', 'GET'])
def mat():
    if request.method == 'POST':
        body = request.get_json()
        mats.append(body)

        return {"message": "Materials already add to database", "body": body}, 201
    elif request.method == 'GET':
        return jsonify(mats)
        #return {"Materials": mat}, 200

main.run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
