from flask import render_template, request
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    name = city = hobby = age = None
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')

    return render_template('blog.html', name=name, city=city, hobby=hobby, age=age)

