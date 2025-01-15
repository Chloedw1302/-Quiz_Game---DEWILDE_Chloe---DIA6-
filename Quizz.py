import random

questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
    {"question": "What is the chemical symbol for water?", "options": ["O2", "H2O", "CO2", "HO"], "answer": "H2O"},
    {"question": "Who wrote 'Hamlet'?", "options": ["William Shakespeare", "Charles Dickens", "Mark Twain", "Leo Tolstoy"], "answer": "William Shakespeare"},
    {"question": "What is the largest mammal in the world?", "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "answer": "Blue Whale"},
    {"question": "Which continent is the Sahara Desert located in?", "options": ["Asia", "Africa", "South America", "Australia"], "answer": "Africa"},
    {"question": "What is the smallest prime number?", "options": ["0", "1", "2", "3"], "answer": "2"},
    {"question": "What is the hardest natural substance on Earth?", "options": ["Gold", "Diamond", "Iron", "Quartz"], "answer": "Diamond"},
    {"question": "Which country is known as the Land of the Rising Sun?", "options": ["China", "Japan", "Thailand", "South Korea"], "answer": "Japan"},
    {"question": "What is the freezing point of water in Celsius?", "options": ["0", "32", "100", "-10"], "answer": "0"}
]

def play_quiz():
    print("Welcome to the Quiz Game!\n")
    random.shuffle(questions)
    score = 0

    for idx, q in enumerate(questions):
        print(f"Question {idx + 1}: {q['question']}")
        for i, option in enumerate(q['options'], 1):
            print(f"{i}. {option}")

        try:
            answer = int(input("Your answer (type the number): "))
            if q['options'][answer - 1] == q['answer']:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {q['answer']}\n")
        except (ValueError, IndexError):
            print("Invalid input. Skipping question.\n")

    print(f"Game Over! Your final score is {score}/{len(questions)}.\n")

play_quiz()
