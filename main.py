from cnocr import CnOcr
from PIL import Image
import json
import flask
from flask import Flask, request
from io import BytesIO
import uuid
import os

app = Flask(__name__)

if not os.path.exists('./pic'):
    os.makedirs('./pic')
ocr_obj = CnOcr('conv-lite-fc')


@app.route('/ocr', methods=['POST'])
def ocr():
    file = request.get_data()
    image = Image.open(BytesIO(file))
    image = image.convert('RGB')
    file_name = './pic/' + str(uuid.uuid4()) + '.jpg'
    image.save(file_name)
    res = ocr_obj.ocr(file_name)
    result = []
    for i in res:
        temp = ''
        data = temp.join(i)
        result.append(data)
    return json.dumps(result, ensure_ascii=False)


app.run(host='127.0.0.1', port='6867', debug=False)
