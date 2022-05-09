from flask import Flask, redirect, render_template


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def redir_root():
        return redirect("/page1")

    @app.route("/page1")
    def page_one():
        return render_template("page1.html")

    @app.route("/page2")
    def page_two():
        return render_template("page2.html")

    @app.route("/page3")
    def page_three():
        return render_template("page3.html")

    return app


app = create_app()

if __name__ == "main":
    app.run()
