# select students with 2nd high score

def second_highest(students):
    if len(students) < 2:
        print("Need at least 2 students!")
    else:
        sorted_score = sorted([score[1] for score in students], reverse = True)
        second_score = sorted_score[1]
        for student in students:
            if student[1] == second_score:
                print(student[0])

list1 = [['Jerry', 100], ['Justin', 84], ['Tom', 90], ['Allen', 92], ['Harsh', 90]]
second_highest(list1)