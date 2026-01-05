from flask import Flask, render_template, request, session
import pickle
from questions import get_random_questions, APTITUDE_QUESTIONS, SOFT_SKILL_QUESTIONS

app = Flask(__name__)
app.secret_key = "placement_secret_key"

model = pickle.load(open("model/model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/softskill")
def softskill():
    qs = get_random_questions(SOFT_SKILL_QUESTIONS)
    session["soft_answers"] = [q[2] for q in qs]
    return render_template("softskill_test.html", questions=qs)

@app.route("/aptitude")
def aptitude():
    qs = get_random_questions(APTITUDE_QUESTIONS)
    session["apt_answers"] = [q[2] for q in qs]
    return render_template("aptitude_test.html", questions=qs)

@app.route("/softskill_result", methods=["POST"])
def softskill_result():
    score = 0
    for i, ans in enumerate(session["soft_answers"]):
        if request.form.get(f"q{i}") == ans:
            score += 100 // len(session["soft_answers"])

    session["soft_skill"] = score
    return render_template("index.html", msg="Soft Skill Test Completed ✔")

@app.route("/aptitude_result", methods=["POST"])
def aptitude_result():
    score = 0
    for i, ans in enumerate(session["apt_answers"]):
        if request.form.get(f"q{i}") == ans:
            score += 100 // len(session["apt_answers"])

    session["aptitude"] = score
    return render_template("index.html", msg="Aptitude Test Completed ✔")

@app.route("/predict", methods=["POST"])
def predict():
    features = [
        float(request.form["CGPA"]),
        int(request.form["Internships"]),
        int(request.form["LeetCode"]),
        int(request.form["HackerRank"]),
        int(request.form["Certifications"]),
        session.get("soft_skill", 50),
        session.get("aptitude", 50)
    ]

    prediction = model.predict([features])[0]
    result = "PLACED 🎉" if prediction == 1 else "NOT PLACED ❌"

    return render_template("result.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
