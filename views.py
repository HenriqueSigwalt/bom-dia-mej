from flask import Flask
#from main import *
import os

app=Flask(__name__)

@app.route("/")
def land():
    #asyncio.run(main())
    print(os.environ.get("API_KEY"))
    teste=os.environ.get("API_KEY")
    return teste