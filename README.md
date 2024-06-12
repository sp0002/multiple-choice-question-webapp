# Multiple-choice Question webapp
This is a web app that lets users do multiple choice questions.
This python project uses a module named Flask to serve resources.

## Making your own
After downloading the files, put them in a folder.

Download Python 3 if you do not have it. Be sure to install pip while installing.

If you already have Python 3 but do not have pip, install pip.
For Debian or Debian based linux users, do: 
`sudo apt-get update
sudo apt-get install python3-pip`

It is recommended that you put the project in a virtual environment.
If using a virtual environment, activate it.
Install the module Flask by doing `pip install flask`. If it does not work, do `pip3 install flask`. If it still does not work, be sure you have installed pip.

In your terminal/command prompt, navigate to the folder.
Execute the python program "sql_db_creator.py" by issuing the command:
- `python sql_db_creator.py` or `py sql_db_creator.py`(if you have enabled this alias) if you only have only one major version of Python.
- `python3 sql_db_creattor.py` if you have both major versions of Python.

Then, execute the python program "add_questions.py". If familar, you might want to change or add your own questions in this file.
- `python add_questions.py` or `py add_questions.py`(if you have enabled this alias) if you only have only one major version of Python.
- `python3 add_questions.py` if you have both major versions of Python.

Lastly, run "main.py".
- `python main.py` or `py main.py`(if you have enabled this alias) if you only have only one major version of Python.
- `python3 main.py` if you have both major versions of Python.

You should see a message ending with the likes of "Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)".
Go to the link in your browser, and voilà! The web app is running!

To close the web app go back to your terminal and press "Ctrl" and "C" at the same time.

#
## Upcoming
- Revamp method of adding questions.
- Allow multiple answers to one question.
