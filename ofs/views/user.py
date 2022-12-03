# -*- coding: utf8 -*-
from flask import request,jsonify
from ofs import app

@app.route("/login", methods=['POST'])
def user_login():
    username = request.json.get("username")
    password = request.json.get("password")
    if username and password:
        return jsonify({"status": 1, "msg": "登陆成功", "data": {
            "token": "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTY3MjQ2MDA1Nn0.ExBU-9SpkL4OgPPHo_4R8DULV58Xp_oc2nohtZ2JDuc"
        }})
