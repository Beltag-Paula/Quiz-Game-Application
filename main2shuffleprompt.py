import os
import json
import random


class QuizGame:
    def __init__(self):
        self.questions = []

    def print_all_prompts(self):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop_path, "promptFile2.txt")

        if os.path.exists(file_path):
            if os.path.getsize(file_path) == 0:  # Check if the promptFile.txt is empty
                print("File is empty.")
            else:
                with open(file_path, "r") as file:
                    prompts = json.load(file)
                    if not prompts:
                        print("No prompts found in the file")
                    else:
                        for i, prompt in enumerate(prompts):
                            print(f"{i + 1}. {prompt['prompt']}")
                            for j, option in enumerate(prompt['options']):
                                print(f"   {chr(65 + j)}. {option}")
                            print(f"   Answer: {prompt['answer']}\n")
        else:
            print("File does not exist.")

    def write_or_check_existing_file(self, question):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop_path, "promptFile2.txt")
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                json.dump([question], file, indent=4)
            print("File created and dictionary written successfully")
        else:
            with open(file_path, "r") as file:
                try:
                    existing_prompts = json.load(file)
                except json.decoder.JSONDecodeError:
                    existing_prompts = []

             #Check if player1 adds a prompt that already exists in the file
            if question not in existing_prompts:
                existing_prompts.append(question)
                with open(file_path, "w") as file:
                    json.dump(existing_prompts, file, indent=4)
                print("File already exists. New prompts added to the file")
            else:
                print("Prompt already exists in the file")

    def read_questions_from_file(self, file_path):
        self.questions = []  # Clear the list before appending questions from the file
        with open(file_path, "r") as file:
            questions_from_file = json.load(file)
        self.questions.extend(questions_from_file)

    def delete_questions_from_file(self, file_path):
        # file_path = os.path.join(os.path.expanduser("~"), "Desktop", "promptFile.txt")
        with open(file_path, "w") as file:
            file.write("")
        print("Contents of promptFile.txt deleted successfully.")

    def delete_prompt_by_index(self, index):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop_path, "promptFile2.txt")

        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                existing_prompts = json.load(file)
            if 0 <= index < len(existing_prompts):
                del existing_prompts[index]  # Remove the prompt at the specified index
                with open(file_path, "w") as file:
                    json.dump(existing_prompts, file, indent=4)
                print("Prompt deleted successfully.")
            else:
                print("Invalid index. Please provide a valid index.")
        else:
            print("File does not exist.")

    def player1_adds_question(self, prompt, options, answer):
        question = {"prompt": prompt, "options": options, "answer": answer}
        self.questions.append(question)

    def player2_answers_question(self):
        # Shuffle the list of questions for player 2
        random.shuffle(self.questions)
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
    print("Hello Player 1!")
    flag = True
    while flag:
        message = input(
            " press 1 preview the prompts, 2 to add new prompts, 3 to delete a prompt, 4 to delete all the prompts, 5 to exit, 6 to pass to Player 2")
        if message == "1":
            game.print_all_prompts()

        elif message == "2":
            while True:
                prompt = input("Enter the question prompt (or 'done' to finish): ")
                if prompt.lower() == "done":
                    break

                options = []
                for i in range(4):
                    options.append(input(f"Enter option {chr(65 + i)}: "))
                answer = input("Enter the correct answer (A, B, C, or D): ").upper()

                question_dict = {
                    "prompt": prompt,
                    "options": options,
                    "answer": answer
                }

                game.write_or_check_existing_file(question_dict)
                game.player1_adds_question(prompt, options, answer)

        elif message == "3":
            game.print_all_prompts()
            index = int(input("Which index would you like to delete? "))
            game.delete_prompt_by_index(index - 1)

        elif message == "4":
            game.delete_questions_from_file(os.path.join(os.path.expanduser("~"), "Desktop", "promptFile2.txt"))

        elif message == "5":
            flag = False

        elif message == "6":
            flag = False  # exiting the while loop and going to player 2
            game.read_questions_from_file(os.path.join(os.path.expanduser("~"), "Desktop", "promptFile2.txt"))
            print("\nHello Player 2!")
            game.player2_answers_question()
