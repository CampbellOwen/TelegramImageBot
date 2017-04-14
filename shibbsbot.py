from flask import Flask, request
import os
import json
import requests
import config
app = Flask(__name__)

image_responses = []
i = 0
for img in config.image_urls:
    image_responses.append({
        'type':'photo',
        'id': str(i),
        'photo_url': img,
        'thumb_url': img
    })
    i += 1

@app.route("/shibbs", methods=['POST'])
def hello():
    jsonResponse = request.get_json()
    
    caption = jsonResponse.get('inline_query', {}).get('query', '')
    print json.dumps(jsonResponse, indent=4)
    print caption
    for img in image_responses:
        img['caption'] = caption
    answer = {
        'inline_query_id' : str(jsonResponse.get('inline_query', {}).get('id', 'no id?')),
        'results': json.dumps(image_responses),
    }
    r = requests.post('https://api.telegram.org/bot{0}/answerInlineQuery'.format(config.token), params=answer)
    print r.status_code
    print r.text
    return json.dumps(answer)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
