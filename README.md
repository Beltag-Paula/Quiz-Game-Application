# Quiz-Game-Application
This project offers a step by step development of how a simple quiz game that is played on a terminal can be made into a GUI application that can be used as a simple game between two users.  
The project is made of 4 python files in this order:
- main.py
   Features : This code defines a simple quiz game between two players: Player 1 (who can add questions) and Player 2 (who can answer them). The game involves saving and retrieving questions from a text file (which is created with the name of promptFile.txt if it doesn't exist) on the desktop. The code saves questions in a JSON format on a file called promptFile.txt on the desktop. Player 1 can input questions which are saved on that file, while Player 2 can answer questions from that file and see their score.
afterwards.

   How It Works:
Initialize the Game: Create an instance of the QuizGame class.
Add Questions: Player 1 can input questions with multiple-choice options and a correct answer.
Save Questions: Questions are saved to promptFile.txt on the desktop.
Answer Questions: Player 2 answers the questions and gets a score based on their answers.

   Methods:
__init__
Purpose: Initializes an empty list to store questions.

write_or_check_existing_file(question)
Purpose: Saves a new question to promptFile.txt on the desktop. If the file exists, it adds the question to the file.
Parameters: question (type: dictionary): Contains the question prompt, options, and the correct answer.

read_questions_from_file(file_path)
Purpose: Loads questions from the specified file into self.questions.
Parameters: file_path (type string): Path to the file containing questions.

player1_adds_question(prompt, options, answer)
Purpose: Adds a question to the game.
Parameters:
prompt (string): The question text.
options (list): List of options.
answer (string): The correct answer.

player2_answers_question()
Purpose: Player 2 answers the questions. The game prints each question and options, checks the answers, and prints the final score.

- main2shuffleprompt.py This code is an update version of main.py
- quizGameMain.py
- quizGame2.py



