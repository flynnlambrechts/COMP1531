import flask
# import src.auth

app = flask.Flask(__name__)


@app.route("/", methods=["GET"])
def foo():
    return "<h1> Joe mama <h1>"


# @app.route("/auth/register/v2", methods=["POST"])
# def auth_register_v2():
#     params = flask.request.get_json()

#     email = str(params["email"])
#     password = str(params["password"])
#     name_first = str(params["name_first"])
#     name_last = str(params["name_last"])

#     return auth.auth_register_v1(email, password, name_first, name_last)


if __name__ == "__main__":
    app.run()
