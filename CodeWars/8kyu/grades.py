# Scores:
    # 90 <= score <= 100	'A'
    # 80 <= score < 90	'B'
    # 70 <= score < 80	'C'
    # 60 <= score < 70	'D'
    # 0 <= score < 60	'F'

def get_grade(s1, s2, s3):
    avg_score = sum([s1, s2, s3]) / len([s1, s2, s3])
    if avg_score >= 90 and avg_score <= 100:
        return "A"
    elif avg_score >= 80 and avg_score <= 90:
        return "B"
    elif avg_score >= 70 and avg_score <= 80:
        return "C"
    elif avg_score >= 60 and avg_score <= 70:
        return "D"
    elif avg_score >= 0 and avg_score <= 600:
        return "F"


get_grade(60, 82, 76)
print(get_grade(60, 82, 76))

