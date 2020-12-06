if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a=student_marks[query_name]  
    b=sum(a)/3
    c=round(b,2)
    print("{0:.2f}".format(c))