'''This is a simple physics quiz which has 25 questions with 4 options for each question. 
The questions are asked from a user in a randomized order and the options are also shuffled.
The user has to select the correct option for each question and the final score is printed at the end.'''

import random       #importing random module
import time         #importing time module
import csv          #importing csv module

questions = {           #dictionary of questions and their options
    "What is the name of the phenomenon where light interacts with matter to create charged particles?":["Photoelectric Effect", "Compton Effect", "Pair Production", "Annihilation"],
    "What is the mathematical relationship between wavelength and frequency?":["λ = 1/f","λ = f","λ = f^2","λf = c (where c is the speed of light)"],
    "An LED is a type of what electronic device?":["Diode","Transistor","Resistor","Capacitor"],
    "What is the name of the scientific theory that explains the wave-particle duality of matter?":["Quantum Mechanics","Special Relativity","General Relativity","String Theory"],
    "What is the name of the experiment that demonstrated the wave nature of electrons?":["Davisson-Germer experiment","Photoelectric effect experiment","Compton scattering experiment","Franck-Hertz experiment"],
    "What does the term “semiconductor” refer to?":["A material with electrical conductivity between that of a conductor and an insulator","A material with high electrical conductivity","A material with low electrical conductivity","A material with no electrical conductivity"],
    "What is the name of the region in a PN junction diode where the mobile charge carriers have been depleted?":["Depletion region","Conduction region","Valence region","Intrinsic region"],
    "How is a solar cell able to generate electricity?":["Through the photovoltaic effect","Through the photoelectric effect","Through the chemiluminescence","Through bioluminescence"],
    "What is the main function of a laser?":["Amplification of light","Absorption of light","Reflection of light","Refraction of light"],
    "What are the two main types of lasers?":["Solid-state and gas lasers","Solid-state and liquid lasers","Gas and liquid lasers","Gas and plasma lasers"],
    "What is the difference between spontaneous emission and stimulated emission?":["Spontaneous emission releases photons randomly, while stimulated emission releases photons in a specific direction.","Spontaneous emission releases photons in a specific direction, while stimulated emission releases photons randomly.","Spontaneous emission releases electrons, while stimulated emission releases photons.","Spontaneous emission releases photons, while stimulated emission releases electrons."],
    "What are the applications of holography?":["All of the above (Data storage, Three-dimensional imaging, Security features on identification cards)","Data storage","Three-dimensional imaging","Security features on identification cards"],
    "What are the different types of optical fibers based on their mode of propagation?":["Single-mode and multi-mode fibers","Monochromatic fibers and polychromatic fibers","Step-index fibers and graded-index fibers","Single-mode and triple-mode fibers"],
    "What is the significance of the acceptance angle in an optical fiber?":["It determines the maximum angle at which light can enter the fiber.","It determines the core diameter of the fiber.","It determines the refractive index of the fiber.","It determines the numerical aperture of the fiber."],
    "What is Gauss’s law in electromagnetism?":["It relates the electric field to the enclosed electric charge.","It relates the magnetic field to the enclosed electric charge.","It relates the electric field to the enclosed magnetic charge.","It relates the magnetic field to the enclosed magnetic charge."],
    "What is the difference between ampere (A) and ampere-hour (Ah)?":["Ampere is the unit of current, while ampere-hour is the unit of electrical energy.","Ampere is the unit of charge, while ampere-hour is the unit of voltage.","Ampere is the unit of voltage, while ampere-hour is the unit of current.","They are the same unit"],
    "What is the principle behind the operation of a transformer?":["Mutual induction","Self-induction","Capacitance","Resistance"],
    "What are the advantages of using alternating current (AC) over direct current (DC) for power transmission?":["AC experiences lower power loss over large distances","AC can be easily transformed to different voltage levels.","AC is safer to use in homes and appliances.","All of the above"],
    "What is the difference between a photovoltaic cell and a photodiode?":["A photovoltaic cell converts light energy into electrical energy, while a photodiode does not.","A photodiode is a type of photovoltaic cell with a specific design for light detection.","Photovoltaic cells are made from different materials than photodiodes.","Photovoltaic cells are used in solar panels, while photodiodes are used in optical sensors."],
    "In a laser cavity, which of the following conditions is necessary for population inversion to occur?":["All of the above (Higher energy level has a smaller population of electrons compared to the lower energy level, Light source pumps electrons to a higher energy level, Stimulated emission dominates over spontaneous emission).","Higher energy level has a smaller population of electrons compared to the lower energy level","Light source pumps electrons to a higher energy level","Stimulated emission dominates over spontaneous emission"],
    "A fiber optic sensor utilizes the principle of:":["Total internal reflection","Refraction","Diffraction","Interference"],
    "For a fixed length of optical fiber, which of the following statements regarding bandwidth is CORRECT?":["Higher bandwidth requires a shorter length of fiber.","Higher bandwidth requires a longer length of fiber.","Bandwidth is independent of the length of fiber.","Bandwidth is inversely proportional to the length of fiber."],
    "Quantum tunneling in a semiconductor device allows:":["All of the above (Electrons to overcome a potential energy barrier by borrowing energy, Holes to move freely through the valence band, Doping to create p-type and n-type regions).","Electrons to overcome a potential energy barrier by borrowing energy","Holes to move freely through the valence band","Doping to create p-type and n-type regions"],
    "The capacitance (C) of a parallel plate capacitor depends on the following factors:":["All of the above (Permittivity (ε) of the dielectric material between the plates, Area (A) of each plate, Distance (d) between the plates) (C = εA/d).","Permittivity (ε) of the dielectric material between the plates","Area (A) of each plate","Distance (d) between the plates"],
    "What is the function of a rectifier in an electrical circuit?":["To convert alternating current (AC) to direct current (DC)","To convert direct current (DC) to alternating current (AC)","To regulate the voltage in the circuit","To store electrical energy in a battery"],
    }

csv_file = "user_data.csv"       #csv file to store user data

def load_user_data():
    """Loads user data from the CSV file.

    Returns:
        A dictionary where keys are usernames and values are dictionaries containing
        password and score (None if user hasn't taken the test).
    """
    user_data = {}
    try:                                        #try block to check if csv file exists
        with open(csv_file, "r") as csvfile:                #opening csv file
            reader = csv.DictReader(csvfile)                #reading csv file
            for row in reader:                              #iterating through rows
                username = row["username"]                  
                user_data[username] = {"password": row["password"], "score": int(row["score"] if row["score"] else None)}
    except FileNotFoundError:                               #except block to create a new csv file if it does not exist
        print("CSV file not found. Creating a new one...")
        with open(csv_file, "w") as csvfile:                #opening csv file
            writer = csv.DictWriter(csvfile, fieldnames=["username", "password", "score"])
            writer.writeheader()                            #writing header
    return user_data

def save_user_data(user_data):  
    """Saves user data to the CSV file.

    Args:
        user_data: A dictionary containing user data (same format as returned by load_user_data).
    """
    with open(csv_file, "w") as csvfile:                    #opening csv file
        writer = csv.DictWriter(csvfile, fieldnames=["username", "password", "score"])          #writing header
        writer.writeheader()                                
        for username, data in user_data.items():                
            writer.writerow({"username": username, "password": data["password"], "score": data.get("score")})       #writing data to csv file

user_data = load_user_data()  # Load user data from CSV

def login():        #function to login user
    username = input("Enter username: ")      #taking username as input
    password = input("Enter password: ")      #taking password as input
    try:                                      #try block to check if username exists and password is correct
        if username in user_data and user_data[username]["password"] == password:       #checking if username exists and password is correct
            print(f"Welcome back, {username}!")
            return user_data[username]            #returning user data
        else:                                   #else block to raise exception if username does not exist or password is incorrect
            raise ValueError("Invalid login credentials.")         #raising exception
    except ValueError as e:                   #except block to catch exception
        print(e)
    return None




def register():                             #function to register user
    username = input("Enter desired username: ")
    if username in user_data:                     #checking if username already exists
        print("Username already exists. Please choose another.")
        return None
    password = input("Enter password: ")          
    user_data[username] = {"password": password, "score": None}       #storing user data in dictionary
    save_user_data(user_data)                                   # Save updated user data to CSV
    print(f"Registration successful, {username}!")           
    return user_data[username]                    #returning user data


def shuffle_questions(questions):            #function to shuffle questions
    question_list = list(questions.items())
    random.shuffle(question_list)
    return question_list


def shuffle_answers(question, answers):     #function to shuffle answers
    correct_answer = answers[0]
    random.shuffle(answers)
    answers.insert(answers.index(correct_answer), correct_answer)         #inserting correct answer at its original position
    return question, answers


def take_test(user):            #function to take test
    start_time = time.time()      #start time of test
    score = 0                     #initial score
    shuffled_questions = shuffle_questions(questions.copy())          #shuffling questions
    for question, options in shuffled_questions:                      #iterating through questions
        print(question)
        shuffled_options = shuffle_answers(question, options.copy())    #shuffling options
        for i, option in enumerate(shuffled_options[1]):                #iterating through options
            print(f"{i+1}. {option}")

        try:                                                            #try block to check if input is valid
            answer_index = int(input("Enter your answer (1-4): ")) - 1    
            if answer_index == shuffled_options[1].index(questions[question]):        #checking if answer is correct
                score += 1  
                print("Correct!")
            else:
                print("Incorrect.")
        except ValueError:                                              #except block to raise exception if input is invalid
            print("Invalid input. Please enter a number between 1 and 4.")

    # Check for time limit after each question
        if time.time() - start_time > 1200:  # 20 minutes in seconds
            print("Time limit exceeded!")
            break

    user["score"] = score                                                 #updating user score in the dictionary
    print(f"You scored {score} out of {len(questions)}.")                 #printing final score


print("Welcome to the Quiz!")

while True:               #infinite loop for menu
        print("\nMenu:")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":           #Login
            try:                      #try block to check if login is successful
                user = login()          #calling login function
                if user:                #checking if user is not None
                    if user["score"] is not None:             #checking if user has taken the test before
                        print(f"Your previous score was {user['score']}.")
                    else:                                     #else block to take test
                        take_test(user)
            except ValueError as e:                       #except block to catch exception
                print(e)
        elif choice == "2":                             #Register
            user = register()
        elif choice == "3":                             #Exit
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


