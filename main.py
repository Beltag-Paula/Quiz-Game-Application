import os
import json


class QuizGame:
    def __init__(self):
        self.questions = []

    def write_or_check_existing_file(self, question):
        # Get the path to the desktop directory
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        # File path on the desktop
        file_path = os.path.join(desktop_path, "promptFile.txt")

        # Check if the file exists
        if not os.path.exists(file_path):
            # If the file doesn't exist, create it and write the dictionary into it
            with open(file_path, "w") as file:
                json.dump([question], file, indent=4)
            print("File created and dictionary written successfully")
        else:
            # If the file already exists, load existing prompts and append new ones
            with open(file_path, "r") as file:
                existing_prompts = json.load(file)
            existing_prompts.append(question)
            with open(file_path, "w") as file:
                json.dump(existing_prompts, file, indent=4)
            print("File already exists. New prompts added to the file")

    def read_questions_from_file(self, file_path):
        with open(file_path, "r") as file:
            questions_from_file = json.load(file)
        self.questions.extend(questions_from_file)

    def player1_adds_question(self, prompt, options, answer):
        # We create a dictionary called questions to store the questions player1 inputs
        question = {"prompt": prompt, "options": options, "answer": answer}
        self.questions.append(question)

    def player2_answers_question(self):
        score = 0
        for question in self.questions:
            print(question["prompt"])
            for letter, option in enumerate(question["options"]):
                print(f"{chr(65 + letter)}. {option}")

            player2_answer = input("Your answer? : ").upper()
            if player2_answer == question["answer"]:
                print("Yay!")
                score += 1
            else:
                print("Nope")
            print()

        print(f"Your final score is {score}/{len(self.questions)}")


if __name__ == "__main__":
    game = QuizGame()

    # Player 1 adds questions
    # First we ask if the player1 wants to take the questions from the promptFile so they won't need to add new questions
    message = input("Do you want to add new prompts to promptFile?")
    if message == "yes":
        # Then, if they say they want to add, do the thing below
        while True:
            prompt = input("Enter the question prompt (or 'done' to finish): ")
            if prompt.lower() == "done":
                break

            options = []
            for i in range(4):
                options.append(input(f"Enter option {chr(65 + i)}: "))
            answer = input("Enter the correct answer (A, B, C, or D): ").upper()

            # Construct question dictionary
            question_dict = {
                "prompt": prompt,
                "options": options,
                "answer": answer
            }

            # Call write_or_check_existing_file method after constructing question dictionary
            game.write_or_check_existing_file(question_dict)

            game.player1_adds_question(prompt, options, answer)

        # Player 2 plays the game
        game.player2_answers_question()

    else:
        # Player 2 plays the game
        game.read_questions_from_file(os.path.join(os.path.expanduser("~"), "Desktop", "promptFile.txt"))
        game.player2_answers_question()
