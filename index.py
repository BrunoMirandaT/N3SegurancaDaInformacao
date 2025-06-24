from flask import Flask, jsonify, render_template, request, flash, redirect, url_for


app = Flask(__name__, template_folder = 'pages')

@app.route("/", methods=['GET', 'POST'])
def cadastrar():
    if request.method == "POST":
        info = [request.form.get['nome'], request.form.get['email'], request.form.get['email']]

    return render_template("registro.html")


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(port=3000, debug=True)
