import random

def print_question(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

def get_user_choice(options_count):
    while True:
        try:
            choice = int(input("Enter the number of your answer: "))
            if 1 <= choice <= options_count:
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def run_quiz(questions):
    score = 0
    for category, qna_list in questions.items():
        print(f"\nCategory: {category}")
        for qna in qna_list:
            question = qna['question']
            options = qna['options']
            correct_answer = qna['correct_answer']

            print_question(question, options)
            user_choice = get_user_choice(len(options))

            if options[user_choice - 1] == correct_answer:
                print("Correct! Well done!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {correct_answer}\n")

    print(f"Your final score is: {score}/{sum(len(qna_list) for qna_list in questions.values())}")

def main():
    print("Welcome to the Quiz Application!\n")

    questions = {
        'General Knowledge': [
            {'question': 'What is the capital of France?', 'options': ['Berlin', 'Madrid', 'Paris', 'Rome'], 'correct_answer': 'Paris'},
            {'question': 'Which planet is known as the Red Planet?', 'options': ['Mars', 'Jupiter', 'Venus', 'Saturn'], 'correct_answer': 'Mars'}
        ],
        'Science': [
            {'question': 'What is the chemical symbol for water?', 'options': ['H2O', 'CO2', 'O2', 'N2'], 'correct_answer': 'H2O'},
            {'question': 'Which gas do plants absorb from the atmosphere?', 'options': ['Oxygen', 'Carbon Dioxide', 'Nitrogen', 'Hydrogen'], 'correct_answer': 'Carbon Dioxide'}
        ],
        'History': [
            {'question': 'Who was the first President of the India?', 'options': ['Rajendra Prasad', 'Jawaharlal Nehru', 'Mahatma Gandhi', 'Indira Gandhi'], 'correct_answer': 'Rajendra Prasad'},
            {'question': 'In which year did World War II end?', 'options': ['1943', '1945', '1947', '1950'], 'correct_answer': '1945'}
        ]
    }

    run_quiz(questions)

if __name__ == "__main__":
    main()
