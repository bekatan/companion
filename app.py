import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        issue = request.form["issue"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(issue),
            temperature=1.0,
            max_tokens=100,
            top_p=1.0,
        )
        # print(response.choices[0].text)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

def generate_prompt(issue):
    return """example: 
        issue: I am sad
        response: It's okay to feel sad sometimes. You can talk to your close friends and family. 
        Try doing things that make you happy like taking a walk or treating yourself with some sweets.
        issue: \"{}\"
        response: """.format(
        issue.capitalize()
    )
