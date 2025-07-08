from flask import Flask, jsonify, render_template, request, flash, redirect, url_for
from flask_oidc import OpenIDConnect


app = Flask(__name__, template_folder = 'pages')
app.config['SECRET_KEY'] = 'super secret key'

app.config.update({
    'TESTING': True,
    'DEBUG': True,
    'OIDC_CLIENT_SECRETS': 'auth.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': True,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_OPENID_REALM': 'guess',
    'OIDC_SCOPES': ['openid', 'profile'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret',
})

oidc = OpenIDConnect(app)

@app.route("/", methods=['GET', 'POST'])
def cadastrar():
    if request.method == "POST":
        info = [request.form.get['nome'], request.form.get['email'], request.form.get['email']]

    return render_template("registro.html")


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(port=3000, debug=False)
