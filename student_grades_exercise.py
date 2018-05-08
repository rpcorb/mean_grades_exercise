import statistics

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

GRADES = {
    "Bob": [10, 40, 70],
    "John": [20, 90, 50],
    "Joe": [88, 26, 90],
    "Mary": [40, 20, 76],
    "Anne": [90, 30, 80]
}

def drop_lowest(numbers):
    numbers_filtered = []
    if len(numbers) <= 1:
        return numbers
    lowest = numbers[0]
    for i in range(1,len(numbers)):
        if numbers[i] < lowest:
            numbers_filtered.append(lowest)
            lowest = numbers[i]
        else:
            numbers_filtered.append(numbers[i])
    return numbers_filtered


def mean_grades_drop_lowest(grades):
    grades_filtered = drop_lowest(grades)
    return str(mean(grades_filtered))


if __name__ == '__main__':
    for name in GRADES:
        print("Name: ", name, ", Mean Grade: ", mean_grades_drop_lowest(GRADES[name]))
    # stretch goal
    assignments_by_student = list(GRADES.values())
    NUMBER_STUDENTS = len(assignments_by_student)
    NUMBER_ASSIGNMENTS = len(assignments_by_student[0])
    grades_by_assignment = []
    for i in range(0,NUMBER_ASSIGNMENTS):
        grades_by_assignment.append([])
        for j in range(0, NUMBER_STUDENTS):
            grades_by_assignment[i].append(assignments_by_student[j][i])
    for assignment in grades_by_assignment:
        print("Min: ", min(assignment), ", Max: ", max(assignment), ", Std. Dev.: ", statistics.stdev(assignment))