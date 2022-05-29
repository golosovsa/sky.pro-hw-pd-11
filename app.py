"""
    Homework №11
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/11-8d13de21a29f4467a5dd3c07217042fc

    App file
"""

from flask import Flask, render_template, request, redirect


from candidates import Candidates
from database import fabricate, JSONDatabase

import settings

app = Flask(__name__)


AppDatabase = fabricate("AppDatabase", JSONDatabase, Candidates)


app_database = AppDatabase()
app_database.connect(settings.APP_DATABASE, settings.APP_DATABASE_TIMEOUT)

app.config.update({
    "APP_DATABASE": app_database,
})


@app.route('/')
def index():
    candidates = app_database.select_all()
    return render_template('main.html', candidates=candidates)


@app.route('/search/')
@app.route('/search/', methods=["POST"])
@app.route('/search/<name>/')
def search(name=""):
    post_name = request.form.get("name", None)
    if post_name is not None:
        return redirect(f"/search/{post_name}")
    candidates = app_database.select_by_name(name)

    return render_template('search.html', name=name, candidates=candidates)


@app.route('/candidate/<int:pk>/')
@app.route('/candidate/<pk>/')
def candidate(pk):
    if type(pk) is not int:
        candidate_by_pk = None
    else:
        candidate_by_pk = app_database.select_one_by_pk(pk)
    error = candidate_by_pk is None
    return render_template('candidate.html', error=error, candidate=candidate_by_pk)


@app.route('/update/', methods=["POST"])
def update():
    data = {
        "id": int(request.form["id"]),
        "name": str(request.form["name"]),
        "picture": str(request.form["picture"]),
        "position": str(request.form["position"]),
        "gender": str(request.form["gender"]),
        "age": int(request.form["age"]),
        "skills": str(request.form["skills"]),
    }
    pk = data["id"]
    app_database.update_one_by_field("id", pk, data)
    return redirect(f"/candidate/{pk}/")


@app.route('/skill/')
@app.route('/skill/<skill>/')
def show_skill(skill=None):
    skills = sorted(app_database.select_skills())

    if skill is None:
        skill = skills[0]
    else:
        skill = skill.strip().lower()

    error = skill not in skills

    if not error:
        candidates_by_skill = app_database.select_by_skill(skill)
    else:
        candidates_by_skill = None

    return render_template('skills.html',
                           error=error,
                           skills=skills,
                           filter_skill=skill,
                           candidates=candidates_by_skill)


@app.route("/admin/")
def admin():
    return render_template('admin.html')


if __name__ == '__main__':
    app.run(debug=True)
