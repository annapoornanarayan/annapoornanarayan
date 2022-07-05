# Learning: Method to obtain 2 decimal places as a result
"""
Full question: The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    summ=0.0
    count=0.0
    for i in student_marks[query_name]:
        summ=summ+i
        count=count+1
    average=summ/count
    format_float = "{:.2f}".format(average)
    print(format_float) 