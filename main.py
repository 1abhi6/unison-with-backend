from flask import Flask, render_template

app = Flask(__name__)

# Endpoint for landing page


@app.route('/')
def index():
    return render_template("index.html")


# Endpoint for homepage


@app.route('/home')
def home():
    return render_template("index.html")

# Endpoint for blog page


@app.route('/blog')
def blog():
    return render_template("blog.html")

# Endpoint for about page


@app.route('/about')
def about():
    return render_template("about.html")

# Endpoints for articles


@app.route('/sample')
def sample():
    return render_template("article_html/sample.html")


@app.route('/sample2')
def sample2():
    return render_template("article_html/sample2.html")


@app.route('/sample3')
def sample3():
    return render_template("article_html/sample3.html")


if __name__ == '__main__':
    app.run(debug=True)
