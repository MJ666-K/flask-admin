from flask import Flask
import json


app = Flask(__name__) 

data = [
        {
            "date": "2023-10-24",
            "title": "穆桂英挂帅",
            "user": "MJ666_K",
            "id": 1,
            "check": True
        },
    ]


# 路由 (装饰器)
@app.route('/data/query')
def get():
    
    result = data
    return result

        

if __name__ == '__main__':
   app.run(
       host='0.0.0.0',
       port=3300
   )