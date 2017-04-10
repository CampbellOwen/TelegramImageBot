from flask import Flask, request
import os
app = Flask(__name__)

token = "313551569:AAEImqIDB64Eqa69R_-ybyx6wjNy4eT0g30"

@app.route("/shibbs", methods=['POST'])
def hello():
    for i in request.form:
        print i
    print request.form.get("update_id", "no id?")
    print request.form.get("inline_query", "Not inline?")
    return "Hello World!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

'''
http://i.imgur.com/6cjQfgQ.jpg
http://i.imgur.com/XQrb6D3.jpg
http://i.imgur.com/CWBmr04.png
http://i.imgur.com/nUIL4CA.png
http://i.imgur.com/bcpaMqK.png
http://i.imgur.com/1yAH4qi.png
http://i.imgur.com/VkJoQHO.png
http://i.imgur.com/fPMyYZY.png
http://i.imgur.com/t7LpSLv.png
'''