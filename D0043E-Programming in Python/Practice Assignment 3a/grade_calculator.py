# Ask the user to input scores for 5 subjects.
score1 = float(input())
score2 = float(input())
score3 = float(input())
score4 = float(input())
score5 = float(input())

# Compute the average of the five subject scores
average = (score1 + score2 + score3 + score4 + score5) / 5


# Function for converting grade
def convertGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# Print the scores, average, and final grade
print("Grade Report")
print("----------------------")
print(f"Subject 1: {score1}")
print(f"Subject 2: {score2}")
print(f"Subject 3: {score3}")
print(f"Subject 4: {score4}")
print(f"Subject 5: {score5}")
print(f"Average Score: {average: .2f}")
grade = convertGrade(average)
print(f"Final Grade: {grade}")
