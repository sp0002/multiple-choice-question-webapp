from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import random
import secrets
import operator

app = Flask(__name__)

# get some values and cache it
questions_db = sqlite3.connect('mcq.db')
cursor = questions_db.cursor()
cursor.execute("SELECT COUNT(*) FROM Questions;")
number_of_questions = cursor.fetchone()[0]
questions_db.close()


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
    if not question:  # sent from confirm
        mcq_db = sqlite3.connect('mcq.db')
        cur = mcq_db.cursor()
        # get number of questions user has answered correctly
        cur.execute("""select COUNT(*) from Attempt LEFT JOIN Questions 
                       ON Attempt.QuestionID = Questions.QuestionID AND 
                       Attempt.Response = Questions.Answer
                       WHERE Attempt.UserID = (SELECT UserID FROM Users WHERE Username = ?) 
                       AND Questions.QuestionID is not null;""", (question_username,))
        answered_questions = cur.fetchone()[0]
        if answered_questions == number_of_questions:
            mcq_db.close()
            return render_template('finish.html',
                                   u_name=question_username,
                                   number_of_questions=number_of_questions)
        # get which question is not answered correctly
        cur.execute("""select Questions.QuestionID from Questions LEFT JOIN Attempt 
                       ON Questions.Answer = Attempt.Response AND
                       Questions.QuestionID = Attempt.QuestionID 
                       AND Attempt.UserID = (SELECT UserID FROM Users WHERE Username = ?) 
                       WHERE Attempt.QuestionID is NULL;""", (question_username,))
        questions_choice = cur.fetchall()
        questions_choice = [i[0] for i in questions_choice]
        random.seed(secrets.randbelow(279936))
        question = random.choice(questions_choice)
        cur.execute("SELECT Answer, WrongAnswer1, WrongAnswer2, WrongAnswer3, QuestionToAsk " +
                    "FROM Questions WHERE QuestionID = ?;",
                    (question,))
        options = list(cur.fetchone())
        mcq_db.close()
        question_text = options[-1]
        options.pop()
        random.seed(question_username + question_text + str(question))
        random.shuffle(options)
        mcq_db.close()
        return render_template("question.html", question=question,
                               question_text=question_text, option1=options[0],
                               option2=options[1], option3=options[2],
                               option4=options[3], u_name=question_username)
    elif not answer:  # answer somehow not in form data?
        mcq_db = sqlite3.connect('mcq.db')
        cur = mcq_db.cursor()
        cur.execute("SELECT Answer, WrongAnswer1, WrongAnswer2, WrongAnswer3, QuestionToAsk " +
                    "FROM Questions WHERE QuestionID = ?;", (question,))
        options = list(cur.fetchone())
        question_text = options[-1]
        options.pop()
        random.seed(question_username + question_text + str(question))
        random.shuffle(options)
        mcq_db.close()
        return render_template("question.html", question=question,
                               question_text=question_text, option1=options[0],
                               option2=options[1], option3=options[2],
                               option4=options[3], error=True,
                               u_name=question_username)
    else:  # question and answer present
        try:
            question = int(question)  # questionid is integer?
        except ValueError:
            return redirect(url_for('main'))  # question number not found? serve index.html
        else:
            mcq_db = sqlite3.connect('mcq.db')
            cur = mcq_db.cursor()
            cur.execute("SELECT Answer, WrongAnswer1, WrongAnswer2, WrongAnswer3, QuestionToAsk " +
                        "FROM Questions WHERE QuestionID = ?;", (question,))
            options = list(cur.fetchone())
            question_text = options[-1]
            correct_answer = options[0]
            options.pop()
            random.seed(question_username + question_text + str(question))
            random.shuffle(options)
            if answer not in options:  # bogus answer? ask question again
                mcq_db.close()
                return render_template("question.html", question=question,
                                       question_text=question_text, option1=options[0],
                                       option2=options[1], option3=options[2],
                                       option4=options[3], error=True,
                                       u_name=question_username)
            else:
                if question > number_of_questions:  # huh? questionid more than the number of questions?
                    mcq_db.close()
                    return redirect(url_for('main'))
                else:  # answering question
                    if answer not in options:  # bogus answer? ask question again
                        mcq_db.close()
                        return render_template("question.html", question=question,
                                               question_text=question_text, option1=options[0],
                                               option2=options[1], option3=options[2],
                                               option4=options[3], error=True,
                                               u_name=question_username)
                    else:  # user answered question
                        if answer != correct_answer:  # answer not correct?
                            cur.execute("SELECT 1 FROM Attempt " +
                                        "WHERE UserID = " +
                                        "(SELECT UserID FROM Users WHERE Username = ?) " +
                                        "AND QuestionID = ? " +
                                        "AND Response = ?;",
                                        (question_username, question, answer))
                            if not cur.fetchone():  # has the user answered the option before?
                                cur.execute("INSERT INTO Attempt (UserID, QuestionID, Response, AttemptsCount)" +
                                            "VALUES ((SELECT UserID FROM Users WHERE Username = ?), ?, ?, ?);",
                                            (question_username, question, answer, 1))
                                mcq_db.commit()
                                mcq_db.close()
                                return render_template("incorrect.html", question=question,
                                                       question_text=question_text, option1=options[0],
                                                       option2=options[1], option3=options[2],
                                                       option4=options[3], u_name=question_username)
                            else:  # user answered the option before
                                cur.execute("UPDATE Attempt " +
                                            "SET AttemptsCount = (AttemptsCount + 1)" +
                                            "WHERE UserID = (SELECT UserID FROM Users WHERE Username = ?) " +
                                            "AND QuestionID = ? " +
                                            "AND Response = ?;",
                                            (question_username, question, answer))
                                mcq_db.commit()
                                mcq_db.close()
                                return render_template("incorrect.html", question=question,
                                                       question_text=question_text, option1=options[0],
                                                       option2=options[1], option3=options[2],
                                                       option4=options[3], u_name=question_username)
                        else:  # ding ding ding!
                            cur.execute("INSERT INTO Attempt (UserID, QuestionID, Response, AttemptsCount)" +
                                        "VALUES ((SELECT UserID FROM Users WHERE Username = ?), ?, ?, ?);",
                                        (question_username, question, answer, 1))
                            mcq_db.commit()
                            mcq_db.close()
                            return render_template("correct.html", question=question,
                                                           question_text=question_text, option1=options[0],
                                                           option2=options[1], option3=options[2],
                                                   option4=options[3], u_name=question_username,
                                                   option_chosen=answer)


@app.route('/leaderboard', methods=['GET', 'POST'])
def leaderboard():
    mcq_db = sqlite3.connect('mcq.db')
    cur = mcq_db.cursor()
    cur.execute("""select Users.Username, SUM(Attempt.AttemptsCount) from Attempt 
                   LEFT JOIN Questions 
                   ON Attempt.QuestionID = Questions.QuestionID AND 
                   Attempt.Response != Questions.Answer
                   LEFT JOIN Users 
                   ON Attempt.UserID = Users.UserID
                   WHERE Questions.QuestionID is not null
                   GROUP BY Attempt.UserID
                   ORDER BY Users.Username;""")
    wrong_attempts = cur.fetchall()
    cur.execute("""select Users.Username, SUM(Attempt.AttemptsCount) from Attempt 
                   LEFT JOIN Questions 
                   ON Attempt.QuestionID = Questions.QuestionID AND 
                   Attempt.Response = Questions.Answer 
                   LEFT JOIN Users 
                   ON Attempt.UserID = Users.UserID 
                   WHERE Questions.QuestionID is not null 
                   GROUP BY Attempt.UserID
                   ORDER BY Users.Username;""")
    correct_attempts = cur.fetchall()
    cur.execute("""select Username from Users
                   ORDER BY Username;""")
    users = cur.fetchall()
    mcq_db.close()

    results = {}
    for i in users:
        results[i[0]] = [0, 0] #  [correct attempts, wrong attempts]
    for i in correct_attempts:
        results[i[0]][0] = i[1]
    for i in wrong_attempts:
        results[i[0]][1] = i[1]

    ranking = []
    for i in results.keys():
        ranking.append((results[i][0], results[i][1], i))
    ranking = sorted(sorted(ranking, key=operator.itemgetter(1, 2)), key=operator.itemgetter(0), reverse=True)
    username = request.form.get('question_username', None)
    return render_template('leaderboard.html', ranking=ranking, username=username)


if __name__ == "__main__":
    app.run(debug=True)
