#Exercise 04

# Ask the user for the capital of France
answer = input("What is the capital of France? ")

# Check if the answer is correct and give feedback
if answer.lower() == "paris":
    print("Correct! The capital of France is indeed Paris.")
else:
    print("Sorry, that's wrong. The capital of France is Paris.")


#Advanced Requirement

    # Dictionary of European countries and their capitals
quiz = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Greece": "Athens",
    "Poland": "Warsaw",
    "Austria": "Vienna"
}

# Initialize a score to track correct answers
score = 0
total_questions = len(quiz)

# Loop through each country in the quiz
for country, correct_answer in quiz.items():
    # Ask the user for the capital
    user_answer = input(f"What is the capital of {country}? ")
    
    # Check if the answer is correct (case-insensitive)
    if user_answer.lower() == correct_answer.lower():
        print(f"Correct! The capital of {country} is {correct_answer}.")
        score += 1  # Increment score for correct answer
    else:
        print(f"Sorry, that's wrong. The capital of {country} is {correct_answer}.")

# Provide final feedback
print(f"\nQuiz completed! You got {score} out of {total_questions} correct.")
percentage = (score / total_questions) * 100
print(f"Your score: {percentage}%")