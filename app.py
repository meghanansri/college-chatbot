from flask import Flask, render_template, request

app = Flask(__name__)

# Change these answers to match your college
COLLEGE_INFO = {
    "football_team": "Yes, the college has a football team.",
    "cs_major": "Yes, the college offers a Computer Science major.",
    "tuition": "The in-state tuition is approximately $11,000 per year.",
    "housing": "Yes, the college provides on-campus housing."
}

# Change this to YOUR details
CREATOR_INFO = {
    "first_name": "Meghana",
    "last_name": "Sri Tadikonda",
    "email": "yourschoolemail@school.edu"
}

QUESTIONS = [
    ("football_team", "Does the college have a football team?"),
    ("cs_major", "Does it offer a Computer Science major?"),
    ("tuition", "What is the in-state tuition?"),
    ("housing", "Does it provide on-campus housing?")
]

@app.route("/", methods=["GET", "POST"])
def home():
    user = {"first_name": "", "last_name": "", "email": ""}
    selected_question = None
    answer = None

    if request.method == "POST":
        user["first_name"] = request.form.get("first_name", "").strip()
        user["last_name"] = request.form.get("last_name", "").strip()
        user["email"] = request.form.get("email", "").strip()
        selected_question = request.form.get("question")

        if selected_question in COLLEGE_INFO:
            answer = COLLEGE_INFO[selected_question]

    return render_template(
        "index.html",
        user=user,
        questions=QUESTIONS,
        selected_question=selected_question,
        answer=answer,
        creator=CREATOR_INFO
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)