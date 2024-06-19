from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guessGenderAndAge', methods=['POST'])
def guessGenderAndAge():
    name = request.form['name']
    name = name.lower()
    param = {
    'name': name
    }
    genRes = requests.get('https://api.genderize.io', params=param)
    ageRes = requests.get('https://api.agify.io', params=param)
    gender = genRes.json()["gender"]
    age = str(ageRes.json()["age"])
    return render_template('name.html', gender = gender, age = age, name=  name)

if __name__ == '__main__':
    app.run(debug=True)