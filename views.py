from flask import Flask,request
from flask_cors import CORS
from main import *
import os

app=Flask(__name__)
CORS(app)

@app.route("/")
def land():
    call=request.args.get("send")
    if call=="1":
        asyncio.run(main())
    return "OI"

@app.route("/inoveq", methods=['POST','GET'])
def inoveq():
    if request.method=="POST":
        algo=request.get_json()
        user=algo["user"]
        text=algo["text"]
        asyncio.run(teste(user,text))
    return "OI"