subject_and_score = []
total_score = 0

while True:
    subject = input("Please enter your name or enter q to quit ")
    if subject == "q":
        avg = total_score / len(subject_and_score)
        print(f"Total Score: {total_score}\nAverage    : {avg}")
        break
    score = float(input("Please enter score "))
    subject_and_score.append({"subject": subject, "score": score})
    total_score += score 
    print(f"Subject: {subject}\nScore  : {score}")