"""
Skill: Loops, rounding, counting, filtering, grading logic
"""

def round_scores(student_scores):
    """Return list of scores rounded to nearest integer."""
    rounded_scores = []
    for score in student_scores:
        rounded_scores.append(round(score))
    return rounded_scores

def count_failed_students(student_scores):
    """Return count of students with scores <= 40."""
    count = 0
    for score in student_scores:
        if score <= 40:
            count += 1
    return count

def above_threshold(student_scores, threshold):
    """Return scores that are >= threshold."""
    result = []
    for score in student_scores:
        if score >= threshold:
            result.append(score)
    return result

def letter_grades(highest):
    """Return list of letter grade thresholds based on highest score."""
    interval = (highest - 40) // 4
    
    d_threshold = 41
    c_threshold = d_threshold + interval
    b_threshold = c_threshold + interval
    a_threshold = b_threshold + interval
    
    return [d_threshold, c_threshold, b_threshold, a_threshold]

def student_ranking(student_scores, student_names):
    """Return formatted rankings with scores."""
    finals = []
    for index, score in enumerate(student_scores):
        name = student_names[index]
        rank = index + 1
        entry = f"{rank}. {name}: {score}"
        finals.append(entry)
    return finals

def perfect_score(student_info):
    """Return first student with perfect score 100, or empty list."""
    for student in student_info:
        name = student[0]
        score = student[1]
        if score == 100:
            return [name, score]
    return []
