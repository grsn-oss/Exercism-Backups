"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    round_student_scores = []
    for index in range(0,len(student_scores)):
      round_student_scores.append(round(student_scores[index]))  

    return round_student_scores

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    failed_counter = 0
    for index2 in range(0,len(student_scores)):
        if student_scores[index2] <= 40:
            failed_counter += 1

    return failed_counter


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    thr_students = []
    for index3 in range(0,len(student_scores)):
        if student_scores[index3] >= threshold:
            thr_students.append(student_scores[index3])

    return thr_students


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55  14
            56 <= "C" <= 70  14
            71 <= "B" <= 85  14
            86 <= "A" <= 100
    """
    offset = round((highest - 41)/4)
    lower_rungs =[41]
    for index4 in range(0,3):
        lower_rungs.append(lower_rungs[index4] + offset)

    return lower_rungs
        


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    ranking = []
    rank = 1
    for index5 in range(0,len(student_names)):
        string = f'{rank}. {student_names[index5]}: {student_scores[index5]}'
        ranking.append(string)
        rank += 1

    return ranking


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for index6 in range(0,len(student_info)):
        if 100 in student_info[index6]:
            return student_info[index6]

    return []
