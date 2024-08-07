# Quiz Game Application

This project offers a step by step development of how a simple quiz game that is played on a terminal can be made into a GUI application that can be used as a simple game between two users.

## [main.py](https://github.com/Beltag-Paula/Quiz-Game-Application/blob/main/main.py)

### Features
This code defines a simple quiz game between two players: Player 1 (who can add questions) and Player 2 (who can answer them). The game involves saving and retrieving questions from a text file (which is created with the name of promptFile.txt if it doesn't exist) on the desktop. The code saves questions in a JSON format on a file called promptFile.txt on the desktop. Player 1 can input questions which are saved on that file, while Player 2 can answer questions from that file and see their score.

### How It Works
1. Initialize the Game: Create an instance of the QuizGame class.
2. Add Questions: Player 1 can input questions with multiple-choice options and a correct answer.
3. Save Questions: Questions are saved to promptFile.txt on the desktop.
4. Answer Questions: Player 2 answers the questions and gets a score based on their answers.

### Methods
- `__init__`: Initializes an empty list to store questions.
- `write_or_check_existing_file(question)`: Saves a new question to promptFile.txt on the desktop. If the file exists, it adds the question to the file.
- `read_questions_from_file(file_path)`: Loads questions from the specified file into self.questions.
- `player1_adds_question(prompt, options, answer)`: Adds a question to the game.
- `player2_answers_question()`: Player 2 answers the questions. The game prints each question and options, checks the answers, and prints the final score.

### Execution Flow on the terminal
1. An instance of `QuizGame()` called `game` is created.
2. We ask Player 1 if they want to add new questions to the file; if "yes", loop to add questions until "done" is entered. Each question is saved to the file and added into `self.question`.
3. Only after Player 1 hits "done" then player's 2 quiz starts.

## [main2shuffleprompt.py](https://github.com/Beltag-Paula/Quiz-Game-Application/blob/main/main2shuffleprompt.py)

### Features
This code is an updated version of main.py, offering new additions such as:
- Previewing All Prompts: The new method `print_all_prompts` allows Player 1 to preview all the questions stored in the file.
- Deleting Individual Prompts: The new method `delete_prompt_by_index` let's Player 1 delete specific questions by their index.
- Deleting All Prompts: The new method `delete_questions_from_file` allows for deleting all the prompts from the file.
- Shuffling the questions: When Player 2 answers questions, they are now presented in a random order due to `random.shuffle`.
- An Enhanced Menu: The main execution flow has a menu for Player 1 to preview, add, delete, or clear questions, and to pass control to Player 2.

### Methods
- `print_all_prompts`: Displays all questions stored in the promptFile2.txt file.
- `write_or_check_existing_file(question)`: Adds a new question to promptFile2.txt if it does not already exist.
- `read_questions_from_file(file_path)`: Loads questions from a specified file into `self.questions`.
- `delete_questions_from_file(file_path)`: Deletes all content from promptFile2.txt.
- `delete_prompt_by_index(index)`: Deletes a specific question by its index from promptFile2.txt.
- `player1_adds_question(prompt, options, answer)`: Adds a question to `self.questions`.
- `player2_answers_question()`: Player 2 answers the shuffled questions and gets a score.

### Execution Flow on the terminal
- Start: Player 1 is presented with a menu to manage questions or pass control to Player 2.
- Menu Options:
  - Preview: Display all questions.
  - Add: Input new questions.
  - Delete Specific: Remove a question by its index.
  - Delete All: Clear all questions from the file.
  - Exit: Quit the management menu.
  - Pass to Player 2: Player 2 starts answering the questions.

## [quizGameMain.py](https://github.com/Beltag-Paula/Quiz-Game-Application/blob/main/quizGameMain.py)

### Overview
This third version transforms the QuizGame into a graphical application using Tkinter, enhancing user interaction with graphical interfaces for various functionalities like viewing, adding, deleting prompts, and playing the quiz game. It introduces a window-based approach for both Player 1 and Player 2 functionalities.

### New Additions and Updates
- Graphical User Interface (GUI): The entire application now uses Tkinter to create a GUI, replacing the command-line interface.
- File Dialogs: Users can select files using a file dialog for more intuitive file handling.
- Prompt Management GUI: Separate windows are provided for viewing, adding, deleting specific prompts, and deleting all prompts.
- Quiz Game GUI: A dedicated interface for Player 2 to play the quiz with radio buttons for answer selection.
- Centralized Menu System: Main menu for navigation between Player 1 and Player 2 functionalities.

### Imports and Setup
- Tkinter Imports: Various Tkinter widgets and functions are imported.
- Standard Imports: Modules for file handling, JSON processing, and randomness.
- PIL: Imported for handling image functionalities (though not used extensively in this example).

### Code Explanation
- Centralized Menu System
  - `create_player1_menu()`: Creates the menu for Player 1 to manage prompts.
  - `create_player2_quiz()`: Creates the quiz interface for Player 2.
  - `create_main_window()`: Creates the main window with navigation options for Player 1 and Player 2.
    
- Commands used by Player's 1 buttons that are present in their menu `create_player1_menu()`:
  - `openFile()`: Opens a new window to input and save a new prompt to a file.
  - `deletePromptFromFile()`: Provides an interface for deleting a specific prompt by its index.
  - `deleteAllPromptsFromFile()`: Clears all content from the selected file.
  - `returnToMenu()`: Returns to the main menu from Player 1's menu.

- Commands used by Player's 2 buttons that present in their menu `create_player2_quiz()`:
  - `returnToMainFromQuiz()`: Returns to the main menu from the quiz window.
  - `load_questions_from_file()`: Loads questions from a selected file for the quiz.
  - `play_game()`: Handles the quiz gameplay for Player 2.


### Summary
The version of the QuizGame class significantly enhances user experience by providing a graphical interface for all interactions, including managing prompts and playing the quiz game. It leverages Tkinter for a windowed approach, making the application more user-friendly and visually appealing. Each feature from the earlier command-line version has been translated into corresponding GUI components for ease of use and better interactivity.

## [quizGame2.py](https://github.com/Beltag-Paula/Quiz-Game-Application/blob/main/quizGame2.py)

  ![Image1](images/img1.png)
  ![Image2](images/img2.png)
  ![Image3](images/img3.png)
  ![Image4](images/img4.png)
  ![Image5](images/img5.png)
  ![Image6](images/img6.png)
  ![Image7](images/img7.png)
  ![Image8](images/img8.png)
  ![Image9](images/img9.png)


### Differences with quizGameMain.py
The main difference between the two versions of the code lies in the organization and structure, as well as some minor implementation details. Let's break down the key differences:

#### User Interface Enhancements

1. **Background Images**: The second version incorporates background images for the main window and player menus, making the application more visually appealing.
2. **Canvas for Layout**: Using a `Canvas` for placing widgets allows for more flexible and sophisticated layouts.
3. **Consistent Button Styling**: Buttons have consistent styling, improving the overall look and feel of the application.

#### Functionality and Usability Improvements

1. **Error Handling**: The second version provides better user feedback using `messagebox` to display errors, ensuring users understand when and why something went wrong.
2. **Clear Field Function**: In the `addPromptToFile` function, a `clear_fields` function is added to reset input fields, enhancing usability.
3. **Centralized Window Positioning**: Windows are centered on the screen, offering a better user experience.

#### Code Organization and Readability

1. **Modular Functions**: Functions are clearly defined and separated by comments, making the code easier to understand and maintain.
2. **Consistent Naming Conventions**: Variable and function names follow consistent naming conventions, improving readability.
3. **Global Variable Management**: The main window context is managed using a global variable, ensuring it is appropriately destroyed and recreated when needed.

#### Additional Functionalities

1. **Update Text Widget After Deletion**: When a prompt is deleted, the text widget displaying the prompts is immediately updated, providing instant feedback to the user.

