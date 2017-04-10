from flask import Flask, request
import os
import json
app = Flask(__name__)

token = "313551569:AAEImqIDB64Eqa69R_-ybyx6wjNy4eT0g30"
image_urls = ['http://i.imgur.com/6cjQfgQ.jpg','http://i.imgur.com/XQrb6D3.jpg', 'http://i.imgur.com/CWBmr04.jpg', 'http://i.imgur.com/nUIL4CA.jpg', 'http://i.imgur.com/bcpaMqK.jpg']
image_responses = []
i = 0
for img in image_urls:
    image_responses.append({
        'type':'photo',
        'id': i,
        'photo_url': img,
        'thumb_url': img
    })
    i += 1

@app.route("/shibbs", methods=['POST'])
def hello():
    jsonResponse = request.get_json()
    print jsonResponse.get('inline_query', 'no query?')
    print jsonResponse.get('update_id', 'no query?')

    answer = {
        'inline_query_id' : jsonResponse.get('update_id', 'no query?'),
        'results': image_responses
    }
    print json.dumps(answer)
    return json.dumps(answer)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

'''
http://i.imgur.com/6cjQfgQ.jpg
http://i.imgur.com/XQrb6D3.jpg
http://i.imgur.com/CWBmr04.jpg
http://i.imgur.com/nUIL4CA.jpg
http://i.imgur.com/bcpaMqK.jpg
http://i.imgur.com/1yAH4qi.jpg
http://i.imgur.com/VkJoQHO.jpg
http://i.imgur.com/fPMyYZY.jpg
http://i.imgur.com/t7LpSLv.jpg
'''