from ssl import AlertDescription
from flask import Flask,jsonify, request

app=Flask(__name__)

tasks=[
    {
        'contact':'1234567890',
        'id':1
        
},

    {
        'id':2,
        'contact': '0987654321'
    },
]

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"pls provide data"
        },400)

    task={
        'id':tasks[-1]['id']+1,
        'contact':request.json['contact'],
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })

if __name__=="__main__":
    app.run()
