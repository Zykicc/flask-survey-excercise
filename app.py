from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey


app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)



responses = []


@app.route("/", methods=['GET', 'POST'])
def start_of_survey():
  return render_template('survey_start.html', survey=survey)

@app.route('/questions/<int:qid>', methods=['GET', 'POST'])
def question(qid):

  if (len(responses) != qid):
        flash(f"Invalid question")
        return redirect(f"/questions/{len(responses)}")
  

  return render_template('question_0.html', question=survey.questions[qid])

@app.route("/answer", methods=['GET', 'POST'])
def answer():
  choice = request.form['answer']

  responses.append(choice)
  
  if (responses is None):
        return redirect("/")

  if (len(responses) == len(survey.questions)):
        return redirect("/complete")

  return redirect(f"/questions/{len(responses)}")

@app.route('/complete', methods=['GET', 'POST'])
def complete_page():
   return render_template('complete.html')