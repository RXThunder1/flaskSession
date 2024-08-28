from flask import Flask, render_template, redirect, url_for, session, request, flash
from surveys import satisfaction_survey  # Import the survey object

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Set a secret key for sessions

@app.route('/')
def start():
    return render_template('start.html', survey=satisfaction_survey)

@app.route('/start-survey', methods=['POST'])
def start_survey():
    session['responses'] = []
    return redirect(url_for('show_question', question_id=0))

@app.route('/questions/<int:question_id>')
def show_question(question_id):
    responses = session.get('responses', [])
    if question_id != len(responses):
        flash("You cannot access this question out of order.")
        return redirect(url_for('show_question', question_id=len(responses)))
    if question_id >= len(satisfaction_survey.questions):
        return redirect(url_for('thank_you'))

    question = satisfaction_survey.questions[question_id]
    return render_template('question.html', question=question, question_id=question_id)

@app.route('/answer', methods=['POST'])
def handle_answer():
    answer = request.form.get('answer')
    responses = session.get('responses', [])
    responses.append(answer)
    session['responses'] = responses

    if len(responses) >= len(satisfaction_survey.questions):
        return redirect(url_for('thank_you'))

    return redirect(url_for('show_question', question_id=len(responses)))

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)