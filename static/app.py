from flask import Flask 

app=Flask(__name__)

@app.route("/")
def firstpage():
    return "Welcome to flask"

@app.route('/second')
def second():
    return "this is a endpoint" 

if __name__ =="__main__":
    app.run(debug=True)
   