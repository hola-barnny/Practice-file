# functions.py
import random
from business_management_quiz import questions

def run_quiz():
    print("Welcome to the Business Management Quiz!")
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (a/b/c/d): ").lower()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was '{q['answer']}'.")
    display_result(score, len(questions))

def display_result(score, total_questions):
    print("\nQuiz Completed!")
    print(f"Your score: {score}/{total_questions}")
    pass_mark = total_questions * 0.6
    if score >= pass_mark:
        print("Congratulations! You passed the quiz.")
    else:
        print("You failed. Better luck next time!")

def shuffle_questions():
    random.shuffle(questions)
