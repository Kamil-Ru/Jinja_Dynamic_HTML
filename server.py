from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    actual_year = datetime.date.today().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=actual_year)

@app.route('/<name>')
def name(name):
    req_genderize = requests.get("https://api.genderize.io?name=" + name)
    results = req_genderize.json()
    req_agify = requests.get("https://api.agify.io?name=" + name)
    results_agify = req_agify.json()
    print(results_agify)
    return render_template("name.html", name=results['name'], gender=results['gender'], age=results_agify["age"], probability=results['probability'], count=results['count'])

@app.route('/blog/<number>')
def get_blog(number):
    blog_url = 'https://api.npoint.io/ed99320662742443cc5b'
    print(blog_url)
    response = requests.get(blog_url)
    response.raise_for_status()
    print(response)
    all_post = response.json()
    print(all_post)
    return render_template('blog.html', posts=all_post, number=number)

if __name__ == "__main__":
    app.run(debug=True)