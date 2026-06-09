# Physics Quiz Application (sem2PyProject)

A robust, menu-driven command-line Physics Quiz Application written in Python. This project was developed as a Semester 2 Python programming project. It features user authentication, persistent data storage via CSV file handling, randomized question delivery, and input error handling.

---

## 🚀 Features

- **User Authentication System**:
  - **Register**: Create a new account with a unique username and password. User accounts are persistently saved.
  - **Login**: Secure login for existing users.
  - **Score Tracking**: Once logged in, the system retrieves and displays the user's previous attempt score. If they haven't taken the test, they can proceed to take it.
- **Dynamic Quiz Engine**:
  - **Question Randomization**: The pool of 25 physics questions is shuffled for each test attempt.
  - **Shuffled Options**: For each question, options are shuffled dynamically to prevent pattern memorization.
  - **Instant Feedback**: The app informs the user immediately if their selection is correct or incorrect.
- **Time Constraint**:
  - Built-in time limit of **20 minutes** (1,200 seconds). The test terminates automatically if the limit is exceeded.
- **Data Persistence**:
  - All user profiles, credentials, and high scores are saved persistently in a `user_data.csv` file.
- **Robust Error Handling**:
  - Validates user menu inputs.
  - Catches invalid formats (e.g., entering non-numeric characters for option selection).
  - Automatically initializes a clean `user_data.csv` with headers if the file is missing.

---

## 🛠️ Project Structure

```text
sem2PyProject/
│
├── main.py          # Core application logic containing the quiz loop and menus
├── user_data.csv    # CSV database file containing username, password, and score fields
└── README.md        # Comprehensive project documentation
```

---

## 📚 Topics Covered in the Quiz

The quiz consists of **25 conceptual physics questions** covering:
- **Quantum Mechanics & Modern Physics**: Photoelectric effect, wave-particle duality, Davisson-Germer experiment.
- **Electromagnetism**: Gauss's law, transformer principles (mutual induction), alternating current vs. direct current.
- **Optics & Lasers**: Spontaneous vs. stimulated emission, applications of holography, optical fibers (propagation modes, acceptance angle).
- **Semiconductors & Electronics**: PN junction diode depletion regions, rectifiers, solar cells (photovoltaic effect), LEDs, quantum tunneling.

---

## ⚙️ How It Works (Technical Breakdown)

### 1. Data Schema (`user_data.csv`)
The CSV file maintains database records with the following headers:
- `username`: A unique identifier for the user.
- `password`: The user's password.
- `score`: The user's highest score (integer from 0 to 25, or empty/None if not attempted).

### 2. Primary Functions
- **`load_user_data()`**: Reads `user_data.csv` and returns a dictionary. If the file is missing, it catches `FileNotFoundError` and creates a new CSV file with the required headers.
- **`save_user_data(user_data)`**: Serializes the dictionary memory structure back into `user_data.csv`.
- **`login()`**: Validates inputs against `user_data`. Returns the user profile if validation succeeds.
- **`register()`**: Validates uniqueness of the desired username, initializes a profile, updates the local dictionary, and saves it.
- **`shuffle_questions(questions)`**: Randomizes the order of questions.
- **`shuffle_answers(question, answers)`**: Shuffles options while preserving the tracking of the correct choice.
- **`take_test(user)`**: Loops through the randomized questions, calculates the score, enforces the 20-minute time limit, and updates the user record.

---

## 🏃 Run the Application

To run this application locally, ensure you have Python 3 installed.

1. Clone the repository:
   ```bash
   git clone https://github.com/HypnoticShield/sem2PyProject.git
   cd sem2PyProject
   ```

2. Run the main file:
   ```bash
   python main.py
   ```

---

## 👤 Developer Profile

- **Name**: Arnav Sharma
- **SAP**: 500120678
- **Roll**: R2142231538
- **Batch**: 46
