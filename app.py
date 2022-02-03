from flask import Flask
from v230DayAlertReport import grab_alerts

app = Flask(__name__)


@app.get('/')
def hello_world():
    return 'Hello World!'

@app.get('/GrabAlerts30Days')
def pull_alerts():
    return grab_alerts()