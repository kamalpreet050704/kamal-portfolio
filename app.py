from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Jinja loop example
@app.route("/jinja")
def jinja_example():
    items = ["Apple", "Banana", "Cherry", "Date"]
    return render_template("jinja.html", items=items)


# Login example
@app.route("/login")
def login():
    is_logged_in = True
    return render_template("login.html", is_logged_in=is_logged_in)


# Project / Profile page
@app.route("/project")
def project():
    user = {
        "name": "Preet Kaur",
        "job_title": "Web Developer",
        "active": True
    }
    return render_template("project.html", user=user)


# Todo list page
@app.route("/todo")
def todo():
    todos = [
        "Learn Flask",
        "Build an App",
        "Sleep"
    ]
    return render_template("todo.html", todos=todos)


# Run the app (ONLY ONCE)
if __name__ == "__main__":
    app.run(debug=True)
