from flask import Flask, request, render_template
import utils
app = Flask(__name__)

@app.route('/')
def page_index():
    candidates = utils.get_all()
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:id>")
def get_candidate_by_id(id):
    candidate = utils.get_candidate_by_id(id)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<name>")
def get_candidates_by_name(name):
    candidates = utils.get_candidate_by_name(name)
    return render_template('search.html', candidates=candidates, count=len(candidates))


@app.route("/skill/<skill>")
def get_candidates_by_skill(skill):
    candidates = utils.get_by_skill(skill.lower())
    return render_template('skill.html', candidates=candidates, count=len(candidates), skill=skill)


app.run(debug=True)
