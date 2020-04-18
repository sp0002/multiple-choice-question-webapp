import sqlite3

questions_db = sqlite3.connect('mcq.db')
cursor = questions_db.cursor()

cursor.execute('drop table Questions')
cursor.execute('''CREATE TABLE "Questions" (
                "QuestionID"	INTEGER PRIMARY KEY AUTOINCREMENT,
                "QuestionToAsk"	TEXT NOT NULL UNIQUE,
                "Answer"	TEXT NOT NULL,
                "WrongAnswer1"	TEXT NOT NULL,
                "WrongAnswer2"	TEXT,
                "WrongAnswer3"	TEXT
            );''')

# question 1
cursor.execute('''INSERT INTO Questions
                ( "QuestionToAsk", "Answer", "WrongAnswer1", "WrongAnswer2", "WrongAnswer3")
                VALUES (
                "There are 48 legs in a farm. There are only snakes, horses and dogs in the farm. If there are ''' +
               'twice as many snakes as dogs and three times as many horses as dogs, how many pigs are there?",' + '''
                "0",
                "3",
                "12",
                "6"
                );''')

# question 2
cursor.execute('''INSERT INTO Questions
                ( "QuestionToAsk", "Answer", "WrongAnswer1", "WrongAnswer2", "WrongAnswer3")
                VALUES (
                "Bob uses up 5ml of ink when he does his Mathematics homework, 7ml when doing his Physics ''' +
               'homework and 3ml of ink when thirsty. How much ink does Bob uses when he is not thirsty and did ' +
               'a piece of Mathematics and two pieces of Mathematics homework?",' + '''
                "15ml",
                "0ml",
                "19oz",
                "19ml"
                );''')

# question 3
cursor.execute('''INSERT INTO Questions
                ( "QuestionToAsk", "Answer", "WrongAnswer1", "WrongAnswer2", "WrongAnswer3")
                VALUES (
                "What does LAN stand for in networking?",
                "Local Area Network",
                "Lua Action Network",
                "Lazer Area Net",
                "Liquid Action Niche"
                );''')

# question 4
cursor.execute('''INSERT INTO Questions
                ( "QuestionToAsk", "Answer", "WrongAnswer1", "WrongAnswer2", "WrongAnswer3")
                VALUES (
                "What does a Python for loop cannot iterate through?",
                "A class.",
                "A list.",
                "A string.",
                "A tuple."
                );''')

# question 5
cursor.execute('''INSERT INTO Questions
                ( "QuestionToAsk", "Answer", "WrongAnswer1", "WrongAnswer2", "WrongAnswer3")
                VALUES (
                "In programming, what is a common mistake in using a 'while' loop?",
                "No exit condition.",
                "Using while True.",
                "Doing the same code over and over.",
                "Using another 'while' loop inside a 'while' loop."
                );''')

# question 6
cursor.execute('''INSERT INTO Questions
                ( "QuestionToAsk", "Answer", "WrongAnswer1", "WrongAnswer2", "WrongAnswer3")
                VALUES (
                "How many semicolon(s) does one add to end their code statement in Python?",
                "It depends.",
                "Only one.",
                "Zero.",
                "-1"
                );''')

# question 7
cursor.execute('''INSERT INTO Questions
                ( "QuestionToAsk", "Answer", "WrongAnswer1", "WrongAnswer2", "WrongAnswer3")
                VALUES (
                "What are the 'html' files rendered in Flask called?",
                "Templates",
                "Static",
                "Fluid pages",
                "Hypertext Preprocessor (PHP)"
                );''')

# question 8
cursor.execute('''INSERT INTO Questions
                ( "QuestionToAsk", "Answer", "WrongAnswer1", "WrongAnswer2", "WrongAnswer3")
                VALUES (
                "In html, which tags does not have a closing tag?",
                "<meta>",
                "<style>",
                "<title>",
                "<p>"
                );''')

# question 9
cursor.execute('''INSERT INTO Questions
                ( "QuestionToAsk", "Answer", "WrongAnswer1", "WrongAnswer2", "WrongAnswer3")
                VALUES (
                "In SQL, which keyword is used to get data from a database?",
                "select",
                "left join",
                "from",
                "where"
                );''')

# question 10
cursor.execute('''INSERT INTO Questions
               ( "QuestionToAsk", "Answer", "WrongAnswer1", "WrongAnswer2", "WrongAnswer3")
               VALUES (
               "After assigning variable y as x in Python 3, where x is a list of 5 objects, ''' +
               'why does changing a value in y changes the same value in x?"' + ''', 
               "The two variables point to the same list.",
               "There is a bug in Python that does this.",
               "Python intelligently detects that the programmer wants to change both lists.",
               "Python used a type of variable copying called linked copy, so the two variables are linked."
               );''')

# question blank
"""cursor.execute('''INSERT INTO Questions
                ( "QuestionToAsk", "Answer", "WrongAnswer1", "WrongAnswer2", "WrongAnswer3")
                VALUES (
                "question",
                "",
                "",
                "",
                ""
                );''')"""
questions_db.commit()
questions_db.close()
