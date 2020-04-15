import sqlite3

questions_db = sqlite3.connect('mcq.db')
cursor = questions_db.cursor()

# question 1
"""cursor.execute('''INSERT INTO Questions
                ( "QuestionToAsk", "Answer", "WrongAnswer1", "WrongAnswer2", "WrongAnswer3")
                VALUES (
                "There are 48 legs in a farm. There are only snakes, horses and dogs in the farm. If there are ''' +
               'twice as many snakes as dogs and three times as many horses as dogs, how many pigs are there?",' + '''
                "0",
                "3",
                "12",
                "6"
                );''')"""

# question 2
"""cursor.execute('''INSERT INTO Questions
                ( "QuestionToAsk", "Answer", "WrongAnswer1", "WrongAnswer2", "WrongAnswer3")
                VALUES (
                "Bob uses up 5ml of ink when he does his Mathematics homework, 7ml when doing his Physics ''' +
               'homework and 3ml of ink when thirsty. How much ink does Bob uses when he is not thirsty and did ' +
               'a piece of Mathematics and two pieces of Mathematics homework?",' + '''
                "15ml",
                "0ml",
                "19oz",
                "19ml"
                );''')"""

# question 3
"""cursor.execuce('''INSERT INTO Questions
                ( "QuestionToAsk", "Answer", "WrongAnswer1", "WrongAnswer2", "WrongAnswer3")
                VALUES (
                "Bob uses up 5ml of ink when he does his Mathematics homework, 7ml when doing his Physics ''' +
               'homework and 3ml of ink when thirsty. How much ink does Bob uses when he is not thirsty and did ' +
               'a piece of Mathematics and two pieces of Mathematics homework?",' + '''
                "15ml",
                "0ml",
                "19oz",
                "19ml"
                );''')"""
x = cursor.fetchone()
print(x)
# questions_db.commit()
questions_db.close()
