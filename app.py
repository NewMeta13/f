from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/get_keywords', methods=['POST'])
def get_keywords():
    data = request.json
    if 'text' in data:
        text = data['text']
        keywords = extract_keywords(text)
        return jsonify(keywords)
    else:
        return jsonify({'error': 'Missing "text" parameter'})


def extract_keywords(text):
    text = text.lower()
    keywords = []
    if 'шаурма' in text:
        keywords.append('шаурма')
    if 'таук' in text:
        keywords.append('таук')
    return keywords


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
