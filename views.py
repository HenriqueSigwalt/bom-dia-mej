from flask import Flask,request
from main import *
import os

app=Flask(__name__)

@app.route("/")
def land():
    call=request.args.get("send")
    if call==1:
        asyncio.run(main())
    return "OI"