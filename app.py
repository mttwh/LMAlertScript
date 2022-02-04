from flask import Flask, request
from pullAlerts import grab_alerts

app = Flask(__name__)


@app.get('/')
def hello_world():
    return 'Hello World!'

@app.get('/grabAlerts')
def pull_alerts():
    args = request.args
    lmAccessId = args.get("accessId")
    lmAccessKey = args.get("accessKey")
    lmCompany = args.get("lmCompany")
    daysOfAlerts = int(args.get("daysOfAlerts"))
    return grab_alerts(lmAccessId, lmAccessKey, lmCompany, daysOfAlerts)