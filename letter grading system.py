def letter_grade(number_grade):

    if number_grade >=91:
        return "A"
    elif number_grade >=81 and number_grade <=90:
        return "B"
    elif number_grade >=71 and number_grade <=80:
        return "C"
    elif number_grade >=61 and number_grade <=70:
        return "D"
    else:
        return "F"

