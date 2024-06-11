def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            user_input = int(input("Please enter the number of your answer: "))
            if 1 <= user_input <= len(options):
                break
            else:
                print("Invalid input. Please enter a number corresponding to one of the options.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if options[user_input - 1] == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"Incorrect. The correct answer was: {correct_answer}")
        return 0

def run_quiz():
    questions = [
        {
            "question": "What is known as a vibrant city?",
            "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
            "correct_answer": "Lisbon"
        },
        {
            "question": "Which is the largest planet in the solar system?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct_answer": "Jupiter"
        },
        {
            "question": "Who is the author of The Adventures of Tom Sawyer?",
            "options": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"],
            "correct_answer": "Mark Twain"
        }
    ]
    
    score = 0
    
    for question_data in questions:
        score += ask_question(question_data["question"], question_data["options"], question_data["correct_answer"])
        print()  # Print a newline for better readability between questions
    
    print(f"Your final score is {score} out of {len(questions)}")

if _name_ == "_main_":
    run_quiz()
