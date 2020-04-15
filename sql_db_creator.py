import sqlite3

questions_db = sqlite3.connect('mcq.db')
cursor = questions_db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS "Users" (
                "UserID"	INTEGER PRIMARY KEY AUTOINCREMENT, 
                "Username"	TEXT NOT NULL UNIQUE
                );''')
cursor.execute('''CREATE TABLE IF NOT EXISTS "Questions" (
                "QuestionID"	INTEGER PRIMARY KEY AUTOINCREMENT,
                "QuestionToAsk"	TEXT NOT NULL UNIQUE,
                "Answer"	TEXT NOT NULL,
                "WrongAnswer1"	TEXT NOT NULL,
                "WrongAnswer2"	TEXT,
                "WrongAnswer3"	TEXT
            );''')
cursor.execute('''CREATE TABLE IF NOT EXISTS "Attempt" (
                "UserID"	INTEGER NOT NULL,
                "QuestionID"	INTEGER NOT NULL,
                "Response"	TEXT NOT NULL,
                "AttemptsCount" INTEGER NOT NULL,
                FOREIGN KEY("UserID") REFERENCES "Users"("UserID"),
                PRIMARY KEY("UserID","QuestionID"),
                FOREIGN KEY("QuestionID") REFERENCES "Questions"("QuestionID")
            );''')
questions_db.commit()
questions_db.close()
