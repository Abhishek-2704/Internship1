quiz_data_pc = [
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Central Processor Unit"],
        "answer": "B"
    },
    {
        "question": "Which component is responsible for rendering graphics in a PC?",
        "options": ["A. CPU", "B. RAM", "C. GPU", "D. SSD"],
        "answer": "C"
    },
    {
        "question": "What type of memory is used for temporary storage while the computer is running?",
        "options": ["A. SSD", "B. HDD", "C. RAM", "D. ROM"],
        "answer": "C"
    },
    {
        "question": "Which company is known for developing the Windows operating system?",
        "options": ["A. Apple", "B. Google", "C. Microsoft", "D. IBM"],
        "answer": "C"
    },
    {
        "question": "Which port is commonly used to connect monitors to a PC?",
        "options": ["A. USB", "B. Ethernet", "C. HDMI", "D. Audio Jack"],
        "answer": "C"
    },
    {
        "question": "What is the primary function of an SSD in a computer?",
        "options": ["A. To store data", "B. To process data", "C. To render graphics", "D. To connect peripherals"],
        "answer": "A"
    }
]

def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    user_answer = input("Enter the letter of your answer: ").strip().upper()
    return user_answer == question_data["answer"]

def run_quiz(quiz_data):
    print("Welcome to the PC Quiz Game by Abhishek Bhujbal!")
    print("Let's test your knowledge about PCs.")
    print()

    score = 0
    for question_data in quiz_data:
        if ask_question(question_data):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question_data['answer']}.")
        print()  # Print a newline for better readability

    print(f"Your final score is {score}/{len(quiz_data)}.")

if __name__ == "__main__":
    run_quiz(quiz_data_pc)
