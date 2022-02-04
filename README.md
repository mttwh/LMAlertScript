# LMAlerts

This Flask appplication exposes an API endpoint which can be used to run a Python script that grabs the past x number of alerts

The API endpoint accepts query params for the API credentials, portal name, and the number of days that you want alerts for. Below is a summary of the query params and an example API call

queryParams:

- accessId - the Access ID of the LogicMonitor API user (user needs read-only access to all resources and full manage access for reports)
- accessKey - the Access Key of the LogicMonitor API user
- lmCompany - the name of the company used in the portal URL (ex=haservices)
- daysOfAlerts - the number of days you want to go back and grab alerts from

Example query: (endpoint is /GrabAlerts30Days and the IP is the public IP of an Azure VM which the Flask application is running on port 5000)
http://40.121.251.46:5000/GrabAlerts30Days?accessId=<accessId>&accessKey=<accessKey>&lmCompany=haservices&daysOfAlerts=7
