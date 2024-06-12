from tkinter import Tk, Button, Label, PhotoImage, filedialog, Entry, messagebox, StringVar, Radiobutton, Canvas, Frame, \
    CENTER, Scrollbar, Text
import os
import json
import random

from PIL import Image, ImageTk


# ----------------Buttons for player 1-------------------------------------------------------------- #
def openFile():
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

        # Create a new window for displaying file contents
        window = Tk()
        window.title("File Contents")

        # Create a Text widget for displaying contents
        text_area = Text(window, wrap="word")
        text_area.insert("end", file_contents)
        text_area.config(state="disabled")

        # Create a vertical scrollbar
        scroll = Scrollbar(window, command=text_area.yview)
        scroll.pack(side="right", fill="y")
        text_area.config(yscrollcommand=scroll.set)

        text_area.pack(expand=True, fill="both")
        window.mainloop()


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

        Label(prompt_window, text="Enter correct option:").pack()
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
        delete_window.title("Delete Prompt by Index")

        # Create a Text widget for displaying contents
        text_area = Text(delete_window, wrap="word", height=15, width=40)
        text_area.insert("end", file_contents)
        text_area.config(state="disabled")

        # Create a vertical scrollbar
        scroll = Scrollbar(delete_window, command=text_area.yview)
        scroll.pack(side="right", fill="y")
        text_area.config(yscrollcommand=scroll.set)

        text_area.pack(side="top", fill="both", expand=True)

        # Entry field for index
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
                        # Update the content of the Text widget
                        text_area.config(state="normal")
                        text_area.delete(1.0, "end")
                        updated_content = ""
                        for i, prompt in enumerate(existing_prompts):
                            updated_content += f"{i + 1}. {prompt['prompt']}\n"
                            for j, option in enumerate(prompt['options']):
                                updated_content += f"   {chr(65 + j)}. {option}\n"
                            updated_content += f"   Answer: {prompt['answer']}\n\n"
                        text_area.insert("end", updated_content)
                        text_area.config(state="disabled")
                        # Clear the entry field
                        index_entry.delete(0, 'end')
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


def start_game(player_quiz_window):
    player_quiz_window.destroy()
    play_game()


# Actual quiz game
def play_game():
    quiz_window = Tk()
    quiz_window.geometry("800x800")
    quiz_window.title("Quiz Game")

    # Center the window on the screen
    window_width = 800
    window_height = 800
    screen_width = quiz_window.winfo_screenwidth()
    screen_height = quiz_window.winfo_screenheight()
    position_top = int((screen_height - window_height) / 2)
    position_right = int((screen_width - window_width) / 2)
    quiz_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # Load and display the background image
    bg_image_path = "images/yeet2.jpg"  # Replace with the path to your background image
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((800, 800), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create canvas and add background image
    canvas = Canvas(quiz_window, width=800, height=800)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Load questions
    questions = load_questions_from_file()
    if questions is None:
        quiz_window.destroy()
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
                option_buttons[x].config(text=f"{option}")

            player_answer.set("")  # Clear previous answer
        else:
            # All questions answered, display final score
            messagebox.showinfo("Game Over", f"Your final score is {score}/{len(questions)}")
            quiz_window.destroy()
            create_main_window()

    def check_answer():
        nonlocal score, question_index
        question = questions[question_index]
        if player_answer.get().upper() == question["answer"]:
            score += 1

        question_index += 1
        display_question()

    # Create the quiz interface, overlaid on the canvas
    question_label = Label(quiz_window, text="", wraplength=700, bg="white", font=("Helvetica", 16, "bold"))
    question_label.place(x=180, y=230)  # Adjust x, y based on your image layout

    option_buttons = []
    positions = [(100, 385), (510, 385), (100, 505), (510, 505)]

    # (x, y) positions for options A, B, C, D
    for i in range(4):
        option_button = Radiobutton(quiz_window, text="", variable=player_answer, value=chr(65 + i),
                                    wraplength=400, indicatoron=False, bg="white", activebackground="orange", font=("Helvetica", 14))
        option_button.place(x=positions[i][0], y=positions[i][1], width=230,
                            height=50)  # Adjust width, height as needed
        option_buttons.append(option_button)

    submit_button = Button(quiz_window, text="Submit Answer", command=check_answer, font=("Helvetica", 14))
    submit_button.place(x=400, y=600)  # Adjust x, y based on your image layout

    # Start the game by displaying the first question
    display_question()
    quiz_window.mainloop()


# -------------------------------------------------------------------------------- #
#
#
#
# ------------------Player 1 Menu --------------------------------------------------#

def create_player1_menu():
    global main_window
    main_window.destroy()

    player1_menu_window = Tk()
    player1_menu_window.title("Player 1 Menu")

    # Set window size
    window_width = 800
    window_height = 800
    screen_width = player1_menu_window.winfo_screenwidth()
    screen_height = player1_menu_window.winfo_screenheight()

    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    player1_menu_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Load and display the background image
    bg_image_path = "images/p1_bg.jpg"  # Change to the correct path of your image
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((800, 800), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = Canvas(player1_menu_window, width=800, height=800)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Button properties
    button_width = 23
    button_height = 2
    button_bg = 'white'
    button_fg = 'black'
    button_active_bg = 'white'
    button_active_fg = 'black'
    button_borderwidth = 0

    # Calculate x position to center buttons
    button_x = (window_width - 200) // 2

    # Create buttons on the canvas
    button_player1_1 = Button(player1_menu_window, text="View prompts", command=openFile,
                              width=button_width, height=button_height,
                              bg=button_bg, fg=button_fg, activebackground=button_active_bg,
                              activeforeground=button_active_fg, borderwidth=button_borderwidth)
    canvas.create_window(button_x, 150, anchor="nw", window=button_player1_1)

    button_player1_2 = Button(player1_menu_window, text="Add new prompt", command=addPromptToFile,
                              width=button_width, height=button_height,
                              bg=button_bg, fg=button_fg, activebackground=button_active_bg,
                              activeforeground=button_active_fg, borderwidth=button_borderwidth)
    canvas.create_window(button_x, 200, anchor="nw", window=button_player1_2)

    button_player1_3 = Button(player1_menu_window, text="Delete existing prompt by index", command=deletePromptFromFile,
                              width=button_width, height=button_height,
                              bg=button_bg, fg=button_fg, activebackground=button_active_bg,
                              activeforeground=button_active_fg, borderwidth=button_borderwidth)
    canvas.create_window(button_x, 250, anchor="nw", window=button_player1_3)

    button_player1_4 = Button(player1_menu_window, text="Delete all existing prompts", command=deleteAllPromptsFromFile,
                              width=button_width, height=button_height,
                              bg=button_bg, fg=button_fg, activebackground=button_active_bg,
                              activeforeground=button_active_fg, borderwidth=button_borderwidth)
    canvas.create_window(button_x, 300, anchor="nw", window=button_player1_4)

    button_player1_5 = Button(player1_menu_window, text="Back to Main Menu",
                              command=lambda: returnToMenu(player1_menu_window),
                              width=button_width, height=button_height,
                              bg=button_bg, fg=button_fg, activebackground=button_active_bg,
                              activeforeground=button_active_fg, borderwidth=button_borderwidth)
    canvas.create_window(button_x, 350, anchor="nw", window=button_player1_5)

    button_player1_6 = Button(player1_menu_window, text="Pass to Player2",
                              command=lambda: create_player2_quiz(player1_menu_window),
                              width=button_width, height=button_height,
                              bg=button_bg, fg=button_fg, activebackground=button_active_bg,
                              activeforeground=button_active_fg, borderwidth=button_borderwidth)
    canvas.create_window(button_x, 400, anchor="nw", window=button_player1_6)

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

    # Get screen width and height
    screen_width = player_quiz_window.winfo_screenwidth()
    screen_height = player_quiz_window.winfo_screenheight()

    # Calculate the position to center the window
    position_x = int((screen_width / 2) - (800 / 2))
    position_y = int((screen_height / 2) - (800 / 2))

    # Set the geometry to center the window
    player_quiz_window.geometry(f"800x800+{position_x}+{position_y}")

    # Set background color to black
    player_quiz_window.configure(bg='black')

    # Create a frame to center the contents
    center_frame = Frame(player_quiz_window, bg='black')
    center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    button_width = 20
    button_height = 2
    button_bg = 'white'
    button_fg = 'black'
    button_active_bg = 'lightgrey'
    button_active_fg = 'black'
    button_borderwidth = 0

    button_quiz_0 = Button(center_frame, text="Click to play",
                           command=lambda: start_game(player_quiz_window),
                           width=button_width, height=button_height,
                           bg=button_bg, fg=button_fg, activebackground=button_active_bg,
                           activeforeground=button_active_fg, borderwidth=button_borderwidth)
    button_quiz_0.pack(pady=10)

    button_quiz_1 = Button(center_frame, text="Back to Main Menu",
                           command=lambda: returnToMainFromQuiz(player_quiz_window),
                           width=button_width, height=button_height,
                           bg=button_bg, fg=button_fg, activebackground=button_active_bg,
                           activeforeground=button_active_fg, borderwidth=button_borderwidth)
    button_quiz_1.pack(pady=10)

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
    window_width = 800
    window_height = 800
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()

    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    main_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Load and display the background image
    bg_image_path = "images/menu.jpg"
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((window_width, window_height), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = Canvas(main_window, width=window_width, height=window_height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Create buttons with transparent backgrounds
    button = Button(main_window, text="Player1", width=20, height=2, command=create_player1_menu,
                    bg='white', fg='black', activebackground='white', activeforeground='black', borderwidth=0)
    canvas.create_window(125, 250, anchor="nw", window=button)

    button2 = Button(main_window, text="Player2", width=20, height=2, command=lambda: create_player2_quiz(main_window),
                     bg='white', fg='black', activebackground='white', activeforeground='black', borderwidth=0)
    canvas.create_window(510, 250, anchor="nw", window=button2)

    main_window.mainloop()


# Run the application
create_main_window()

# -------------------------------------------------------------------------------- #
#
#
#
