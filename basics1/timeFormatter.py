"""9. Exam Schedule Formatter

Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014"""


def display_exam_schedule():
    exam_st_date = (11, 12, 2014)
    # Format the date into a string
    formatted_date = f"{exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}"
    print("The examination will start from:", formatted_date)


if __name__ == "__main__":
    display_exam_schedule()
