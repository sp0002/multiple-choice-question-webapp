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

# question 11
cursor.execute('''INSERT INTO Questions
                ( "QuestionToAsk", "Answer", "WrongAnswer1", "WrongAnswer2", "WrongAnswer3")
                VALUES (
                "A stack data structure can be implemented using:",
                "linked list or array",
                "random number generator",
                "SQL right middle join",
                "merge sort"
                );''')

# question 12
cursor.execute('''INSERT INTO Questions
                ( "QuestionToAsk", "Answer", "WrongAnswer1", "WrongAnswer2", "WrongAnswer3")
                VALUES (
                "How do you find the letter 6 positions after 'B' in python?",
                "chr(ord('B') + 6)",
                "chr(ASCII('B') + 6)",
                "'B' + 6",
                "'B' >> 6"
                );''')

# question 13
cursor.execute('''INSERT INTO Questions
                ( "QuestionToAsk", "Answer", "WrongAnswer1", "WrongAnswer2", "WrongAnswer3")
                VALUES (
                "How do you run a python file in IDLE?",
                "Click Run, then click Run Module.",
                "Press Alt + F4",
                "Wait 224 seconds after doing a change.",
                "Press Ctrl/Cmd + S then press Ctrl/Cmd + r + u + n."
                );''')

# question 14
cursor.execute('''INSERT INTO Questions
                ( "QuestionToAsk", "Answer", "WrongAnswer1", "WrongAnswer2", "WrongAnswer3")
                VALUES (
                "What does i++ do?",
                "Increment i by one after.",
                "Wrong syntax.",
                "Acts as a breakpoint for the code.",
                "Boosts me."
                );''')

# question 15
cursor.execute('''INSERT INTO Questions
                ( "QuestionToAsk", "Answer", "WrongAnswer1", "WrongAnswer2", "WrongAnswer3")
                VALUES (
                "Which of the following is a NoSQL database?",
                "MongoDB",
                "MySQL",
                "SQLite3",
                "PostgreSQL"
                );''')

# question blank
"""cursor.execute('''INSERT INTO Questions
                ( "QuestionToAsk", "Answer", "WrongAnswer1", "WrongAnswer2", "WrongAnswer3")
                VALUES (
                "question",
                "answer",
                "wrong1",
                "wrong2",
                "wrong3"
                );''')"""
questions_db.commit()
questions_db.close()
