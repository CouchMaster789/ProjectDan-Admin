from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/invoices')
def invoices():
    return render_template("invoices.html")


@app.route('/invoice/<invoice_id>')
def invoice(invoice_id):
    return render_template("invoice.html")


@app.route('/clients')
def clients():
    return render_template("clients.html")


@app.route('/projects')
def projects():
    return render_template("projects.html")


@app.route('/blog_posts')
def blog_posts():
    return render_template("blog_posts.html")


@app.route('/users')
def users():
    return render_template("users.html")


if __name__ == '__main__':
    app.run()
