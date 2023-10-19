from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def ask_questions():
    """Display the form used to capture word prompts."""

    prompts = story.prompts

    return render_template("questions.html", prompts=prompts)


@app.route("/story")
def show_story():
    """Display story result."""

    text = story.generate(request.args)

    return render_template("story.html", text=text)
