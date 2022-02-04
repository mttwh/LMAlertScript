from flask import Flask, request
from v230DayAlertReport import grab_alerts

app = Flask(__name__)


@app.get('/')
def hello_world():
    return 'Hello World!'

@app.get('/GrabAlerts30Days')
def pull_alerts():
    args = request.args
    lmAccessId = args.get("accessId")
    lmAccessKey = args.get("accessKey")
    lmCompany = args.get("lmCompany")
    return grab_alerts(lmAccessId, lmAccessKey, lmCompany)