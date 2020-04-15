from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import random
import secrets

app = Flask(__name__)

# get some values and cache it
questions_db = sqlite3.connect('mcq.db')
cursor = questions_db.cursor()
cursor.execute("SELECT COUNT(*) FROM Questions;")
number_of_questions = cursor.fetchone()[0]
questions_db.close()


def get_randomised_options(options, seed):
    print(options, seed)
    random.seed(seed)
    random.shuffle(options)
    return options


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/confirm', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':  # just accessed the page
        return redirect(url_for('main'))
    username = request.form.get('login_username', None)
    if not username:  # not sent from main page
        return redirect(url_for('main'))
    else:  # typed a username
        mcq_db = sqlite3.connect('mcq.db')
        cur = mcq_db.cursor()
        cur.execute("SELECT 1 FROM Attempt " +
                    "WHERE UserID = " +
                    "(SELECT UserID FROM Users WHERE Username = ?);",
                    (username, ))
        if not cur.fetchone():  # username has no attempts?
            cur.execute("SELECT 1 FROM Users " +
                        "WHERE Username = ?", (username, ))
            if not cur.fetchone():
                cur.execute("INSERT INTO Users (Username)" +
                            "VALUES (?);", (username, ))
                mcq_db.commit()
                mcq_db.close()
            return render_template('confirm.html', new_user=True, u_name=username)
        else:
            mcq_db.close()
            return render_template('confirm.html', new_user=False, u_name=username)


@app.route('/questions', methods=['GET', 'POST'])
def mcq():
    question_username = request.form.get('question_username', None)
    if not question_username:  # username field not present? send to main page
        return redirect(url_for('main'))
    question = request.form.get('question', None)
    answer = request.form.get('answer', None)
    random_seed = request.form.get('seed', None)
    print(random_seed)
    if not random_seed:
        random_seed = secrets.randbelow(279936)
    print(random_seed)
    if not question:  # sent from confirm
        question_selected = False
        answered_questions = set()
        while not question_selected:
            question_no = secrets.randbelow(number_of_questions)
            if len(answered_questions) == number_of_questions:
                return render_template('finish.html')
            elif question_no not in answered_questions:  # answered before?
                mcq_db = sqlite3.connect('mcq.db')
                cur = mcq_db.cursor()
                cur.execute("SELECT 1 FROM Attempt WHERE " +
                            "UserID = (SELECT UserID FROM Users WHERE UserID = ?) AND " +
                            "Response = (SELECT Answer FROM Questions WHERE QuestionID = ?);",
                            (question_username, question_no))
                if cur.fetchone():
                    answered_questions.add(question_no)  # answered correctly before, pick another question
                else:
                    question = question_no
                    question_selected = True
        cur.execute("SELECT Answer, WrongAnswer1, WrongAnswer2, WrongAnswer3, QuestionToAsk " +
                    "FROM Questions WHERE QuestionID = ?;", (question,))
        options = list(cur.fetchone())
        mcq_db.close()
        question_text = options[-1]
        options.pop()
        print(options, '123')
        options = get_randomised_options(options, random_seed)
        print(options)
        return render_template("question.html", question=question,
                               question_text=question_text, option1=options[0],
                               option2=options[1], option3=options[2],
                               option4=options[3], seed=random_seed,
                               u_name=question_username)
    elif not answer:  # answer somehow not in form data?
        mcq_db = sqlite3.connect('mcq.db')
        cur = mcq_db.cursor()
        cur.execute("SELECT Answer, WrongAnswer1, WrongAnswer2, WrongAnswer3, QuestionToAsk " +
                    "FROM Questions WHERE QuestionID = ?;", (question,))
        options = list(cur.fetchone())
        if answer not in options:  # bogus answer? ask question again
            question_text = options[-1]
            options.pop()
            print(options, '123')
            options = get_randomised_options(options, random_seed)
            print(options)
            return render_template("question.html", question=question,
                                   question_text=question_text, option1=options[0],
                                   option2=options[1], option3=options[2],
                                   option4=options[3], error=True,
                                   seed=random_seed, u_name=question_username)
    else:
        try:
            question = int(question)  # questionid?
        except ValueError:
            return redirect(url_for('main'))  # question number not found? serve index.html
        else:
            if question > number_of_questions:  # huh? questionid more than the number of questions?
                return redirect(url_for('main'))
            else:  # answering question
                mcq_db = sqlite3.connect('mcq.db')
                cur = mcq_db.cursor()
                cur.execute("SELECT Answer, WrongAnswer1, WrongAnswer2, WrongAnswer3, QuestionToAsk " +
                            "FROM Questions WHERE QuestionID = ?;", (question,))
                options = list(cur.fetchone())
                if answer not in options:  # bogus answer? ask question again
                    question_text = options[-1]
                    options.pop()
                    print(options, '123')
                    options = get_randomised_options(options, random_seed)
                    print(options)
                    return render_template("question.html", question=question,
                                           question_text=question_text, option1=options[0],
                                           option2=options[1], option3=options[2],
                                           option4=options[3], error=True,
                                           seed=random_seed, u_name=question_username)
                else:  # user answered question
                    if answer != options[0]:  # answer not correct?
                        cur.execute("SELECT 1 FROM Attempt " +
                                    "WHERE UserID = " +
                                    "(SELECT UserID FROM Users WHERE Username = ?) " +
                                    "AND QuestionID = ? " +
                                    "AND Response = ?;",
                                    (question_username, question, answer))
                        if not cur.fetchone():  # has the user answered the option before?
                            cur.execute("INSERT INTO Attempt " +
                                        "VALUES ((SELECT UserID FROM Users WHERE Username = ?), ?, ?, ?);",
                                        (question_username, question, answer, 1))
                            mcq_db.close()
                            question_text = options[-1]
                            options.pop()
                            print(options, '123')
                            options = get_randomised_options(options, random_seed)
                            print(options)
                            return render_template("incorrect.html", question=question,
                                                   question_text=question_text, option1=options[0],
                                                   option2=options[1], option3=options[2],
                                                   option4=options[3], seed=random_seed,
                                                   u_name=question_username)
                        else:  # user answered the option before
                            cur.execute("UPDATE Attempt " +
                                        "SET AttemptsCount = AttemptsCount + 1" +
                                        "WHERE UserID = (SELECT UserID FROM Users WHERE Username = ?) " +
                                        "AND QuestionID = ? " +
                                        "AND Response = ?;",
                                        (question_username, question, answer))
                            mcq_db.close()
                            question_text = options[-1]
                            options.pop()
                            print(options, '123')
                            options = get_randomised_options(options, random_seed)
                            print(options)
                            return render_template("incorrect.html", question=question,
                                                   question_text=question_text, option1=options[0],
                                                   option2=options[1], option3=options[2],
                                                   option4=options[3], seed=random_seed,
                                                   u_name=question_username)
                    else:  # ding ding ding!
                        question_text = options[-1]
                        options.pop()
                        print(options, '123')
                        options = get_randomised_options(options, random_seed)
                        print(options)
                        return render_template("correct.html", question=question,
                                               question_text=question_text, option1=options[0],
                                               option2=options[1], option3=options[2],
                                               option4=options[3], u_name=question_username,
                                               option_chosen=answer)


if __name__ == "__main__":
    app.run(debug=True)
