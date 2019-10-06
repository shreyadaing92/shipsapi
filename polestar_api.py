from flask import Flask, request, redirect, render_template
from api_db import polestar_api_db as db
import json

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('index.html')

@app.route('/api/ships/',methods=["GET"])
def getShips():
    results = db.getShips('''SELECT * from ships''')
    row_headers = ["imo","name"]
    json_data=[]
    for result in results:
        json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data,indent=4, sort_keys=True)

@app.route('/api/positions/<int:imo_number>',methods=["GET"])
def getShipPosition(imo_number):
    results = db.getPositions('''SELECT * from positions1 where imo_number = ? order by timestamp''',(imo_number,))
    row_headers = ["id","imo_number","timestamp","latitude","longitude"]
    json_data=[]
    for result in results:
        json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data,indent=4, sort_keys=True)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')
