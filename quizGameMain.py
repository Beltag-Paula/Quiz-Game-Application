from tkinter import Tk, Button, Label, PhotoImage, filedialog, Entry, messagebox, StringVar, Radiobutton
import os
import json
import random
from tkinter.constants import LEFT, RIGHT

from PIL import Image, ImageTk


# ----------------Buttons for player 1-------------------------------------------------------------- #
def openFile():  #
    filepath = filedialog.askopenfilename(initialdir=os.path.expanduser("~"), title="Open file",
                                          filetypes=[("Text files", "*.txt")])

    if filepath:
        if os.path.exists(filepath):
            if os.path.getsize(filepath) == 0:
                file_contents = "File is empty."
            else:
                with open(filepath, 'r') as file:
                    try:
                        prompts = json.load(file)
                        if not prompts:
                            file_contents = "No prompts found in the file"
                        else:
                            file_contents = ""
                            for i, prompt in enumerate(prompts):
                                file_contents += f"{i + 1}. {prompt['prompt']}\n"
                                for j, option in enumerate(prompt['options']):
                                    file_contents += f"   {chr(65 + j)}. {option}\n"
                                file_contents += f"   Answer: {prompt['answer']}\n\n"
                    except json.JSONDecodeError:
                        file_contents = "File is not a valid JSON."
        else:
            file_contents = "File does not exist."

        test = Tk()
        test.geometry("800x800")
        test.title("File Contents")
        file_contents_label = Label(test, text=file_contents, wraplength=700)
        file_contents_label.pack()
        test.mainloop()


def addPromptToFile():
    filepath = filedialog.askopenfilename(initialdir=os.path.expanduser("~"), title="Select file",
                                          filetypes=[("Text files", "*.txt")])

    if filepath:
        prompt_window = Tk()
        prompt_window.geometry("400x500")
        prompt_window.title("Add New Prompt")

        Label(prompt_window, text="Enter prompt:").pack()
        prompt_text = Entry(prompt_window, width=50)
        prompt_text.pack()

        Label(prompt_window, text="Enter A:").pack()
        option1_text = Entry(prompt_window, width=50)
        option1_text.pack()

        Label(prompt_window, text="Enter B:").pack()
        option2_text = Entry(prompt_window, width=50)
        option2_text.pack()

        Label(prompt_window, text="Enter C:").pack()
        option3_text = Entry(prompt_window, width=50)
        option3_text.pack()

        Label(prompt_window, text="Enter option D:").pack()
        option4_text = Entry(prompt_window, width=50)
        option4_text.pack()

        Label(prompt_window, text="Enter answer:").pack()
        answer_text = Entry(prompt_window, width=50)
        answer_text.pack()

        def clear_fields():
            prompt_text.delete(0, 'end')
            option1_text.delete(0, 'end')
            option2_text.delete(0, 'end')
            option3_text.delete(0, 'end')
            option4_text.delete(0, 'end')
            answer_text.delete(0, 'end')

        def save_prompt():
            prompt = prompt_text.get()
            options = [option1_text.get(), option2_text.get(), option3_text.get(), option4_text.get()]
            answer = answer_text.get()

            question = {
                'prompt': prompt,
                'options': options,
                'answer': answer
            }

            if not os.path.exists(filepath):
                with open(filepath, "w") as file:
                    json.dump([question], file, indent=4)
                result_label.config(text="File created and prompt written successfully")
            else:
                with open(filepath, "r") as file:
                    try:
                        existing_prompts = json.load(file)
                    except json.decoder.JSONDecodeError:
                        existing_prompts = []

                if any(existing['prompt'] == prompt for existing in existing_prompts):
                    result_label.config(text="Prompt already exists in the file")
                else:
                    existing_prompts.append(question)
                    with open(filepath, "w") as file:
                        json.dump(existing_prompts, file, indent=4)
                    result_label.config(text="New prompt added to the file")

            clear_fields()

        save_button = Button(prompt_window, text="Save Prompt", command=save_prompt)
        save_button.pack()

        result_label = Label(prompt_window, text="")
        result_label.pack()

        prompt_window.mainloop()


def deletePromptFromFile():
    filepath = filedialog.askopenfilename(initialdir=os.path.expanduser("~"), title="Select file",
                                          filetypes=[("Text files", "*.txt")])

    if filepath:
        try:
            with open(filepath, 'r') as file:
                prompts = json.load(file)
                if not prompts:
                    file_contents = "No prompts found in the file"
                else:
                    file_contents = ""
                    for i, prompt in enumerate(prompts):
                        file_contents += f"{i + 1}. {prompt['prompt']}\n"
                        for j, option in enumerate(prompt['options']):
                            file_contents += f"   {chr(65 + j)}. {option}\n"
                        file_contents += f"   Answer: {prompt['answer']}\n\n"
        except json.JSONDecodeError:
            file_contents = "File is not a valid JSON."

        delete_window = Tk()
        delete_window.geometry("300x200")
        delete_window.title("Delete Prompt by Index")

        file_contents_label = Label(delete_window, text=file_contents, wraplength=700)
        file_contents_label.pack()

        Label(delete_window, text="Enter the index of the prompt to delete:").pack()
        index_entry = Entry(delete_window, width=10)
        index_entry.pack()

        def perform_deletion():
            try:
                index = int(index_entry.get()) - 1  # Convert to 0-based index
                if os.path.exists(filepath):
                    with open(filepath, "r") as file:
                        existing_prompts = json.load(file)
                    if 0 <= index < len(existing_prompts):
                        del existing_prompts[index]  # Remove the prompt at the specified index
                        with open(filepath, "w") as file:
                            json.dump(existing_prompts, file, indent=4)
                        result_label.config(text="Prompt deleted successfully.")
                    else:
                        result_label.config(text="Invalid index. Please provide a valid index.")
                else:
                    result_label.config(text="File does not exist.")
            except ValueError:
                result_label.config(text="Please enter a valid number.")

        delete_button = Button(delete_window, text="Delete Prompt", command=perform_deletion)
        delete_button.pack()

        result_label = Label(delete_window, text="")
        result_label.pack()

        delete_window.mainloop()


def deleteAllPromptsFromFile():
    filepath = filedialog.askopenfilename(initialdir=os.path.expanduser("~"), title="Select file",
                                          filetypes=[("Text files", "*.txt")])

    if filepath:
        with open(filepath, "w") as file:
            file.write("")


def returnToMenu(player1_menu_window):
    player1_menu_window.destroy()
    create_main_window()


# -------------------------------------------------------------------------------- #
#
#
#
# ---------------- Buttons for Player 2 + Quiz Game -------------------------------- #
def returnToMainFromQuiz(player_quiz_window):
    player_quiz_window.destroy()
    create_main_window()


# Load questions from a file
def load_questions_from_file():
    filepath = filedialog.askopenfilename(initialdir=os.path.expanduser("~"), title="Open file",
                                          filetypes=[("Text files", "*.txt")])

    if filepath and os.path.exists(filepath):
        with open(filepath, 'r') as file:
            try:
                questions = json.load(file)
                if not questions:
                    messagebox.showerror("Error", "No prompts found in the file")
                    return None
                return questions
            except json.JSONDecodeError:
                messagebox.showerror("Error", "File is not a valid JSON.")
                return None
    else:
        messagebox.showerror("Error", "File does not exist or not selected.")
        return None


# Actual quiz game
def play_game(player_quiz_window):
    questions = load_questions_from_file()
    if questions is None:
        return

    random.shuffle(questions)  # Shuffle the questions for randomness

    score = 0
    question_index = 0
    player_answer = StringVar()  # To hold the player's answer

    def display_question():
        nonlocal question_index
        if question_index < len(questions):
            question = questions[question_index]
            question_label.config(text=question["prompt"])

            for x, option in enumerate(question["options"]):
                option_buttons[x].config(text=f"{chr(65 + x)}. {option}", value=chr(65 + x))

            player_answer.set("")  # Clear previous answer
        else:
            # All questions answered, display final score
            messagebox.showinfo("Game Over", f"Your final score is {score}/{len(questions)}")
            player_quiz_window.destroy()
            create_main_window()

    def check_answer():
        nonlocal score, question_index
        question = questions[question_index]
        if player_answer.get().upper() == question["answer"]:
            score += 1

        question_index += 1
        display_question()

    # Create the quiz interface
    question_label = Label(player_quiz_window, text="", wraplength=700)
    question_label.pack()

    option_buttons = []
    for i in range(4):
        option_button = Radiobutton(player_quiz_window, text="", variable=player_answer, value=chr(65 + i),
                                    wraplength=700, indicatoron=False)
        option_button.pack(fill='x', padx=5, pady=2)
        option_buttons.append(option_button)

    submit_button = Button(player_quiz_window, text="Submit Answer", command=check_answer)
    submit_button.pack(pady=10)

    # Start the game by displaying the first question
    display_question()


# -------------------------------------------------------------------------------- #
#
#
#
# ------------------Player 1 Menu --------------------------------------------------#

def create_player1_menu():
    global main_window
    main_window.destroy()

    player1_menu_window = Tk()
    player1_menu_window.geometry("800x800")
    player1_menu_window.title("Player 1 Menu")

    button_player1_1 = Button(player1_menu_window, text="View prompts", command=openFile)
    button_player1_1.pack()

    button_player1_2 = Button(player1_menu_window, text="Add new prompt", command=addPromptToFile)
    button_player1_2.pack()

    button_player1_3 = Button(player1_menu_window, text="Delete existing prompt by index", command=deletePromptFromFile)
    button_player1_3.pack()

    button_player1_4 = Button(player1_menu_window, text="Delete all existing prompts", command=deleteAllPromptsFromFile)
    button_player1_4.pack()

    button_player1_5 = Button(player1_menu_window, text="Back to Main Menu",
                              command=lambda: returnToMenu(player1_menu_window))
    button_player1_5.pack()

    button_player1_6 = Button(player1_menu_window, text="Pass to Player2",
                              command=lambda: create_player2_quiz(player1_menu_window))
    button_player1_6.pack()

    player1_menu_window.mainloop()


# -------------------------------------------------------------------------------- #
#
#
#
# -------------------Player 2 Menu ------------------------------------------------ #
def create_player2_quiz(current_window):
    current_window.destroy()

    player_quiz_window = Tk()
    player_quiz_window.geometry("800x800")
    player_quiz_window.title("Player Quiz")

    Label(player_quiz_window, text="Player 2 Quiz Interface").pack()

    button_quiz_0 = Button(player_quiz_window, text="Click to play",
                           command=lambda: play_game(player_quiz_window))
    button_quiz_0.pack()

    button_quiz_1 = Button(player_quiz_window, text="Back to Main Menu",
                           command=lambda: returnToMainFromQuiz(player_quiz_window))
    button_quiz_1.pack()

    player_quiz_window.mainloop()


# -------------------------------------------------------------------------------- #
#
#
#
# ----------------------Main Window Menu -------------------------------------------#
def create_main_window():
    global main_window
    main_window = Tk()
    main_window.title("Quiz Game")

    # Set window size
    window_width = 500
    window_height = 500
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()

    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    main_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Set window icon
    icon = PhotoImage(file="images/trivia_logo.png")
    main_window.iconphoto(True, icon)

    # Create buttons
    button = Button(main_window, text="Player1", width=20, height=20, command=create_player1_menu)
    button.pack(side=LEFT, padx=60, pady=10)

    button2 = Button(main_window, text="Player2", width=20, height=20, command=lambda: create_player2_quiz(main_window))
    button2.pack(side=RIGHT, padx=50, pady=30)

    main_window.mainloop()


# Run the application
create_main_window()

# -------------------------------------------------------------------------------- #
#
#
#

