import sys

N=int(sys.stdin.readline())

students_score = []

for _ in range(N):
    name,korea,english,math = list(sys.stdin.readline().split())
    students_score.append([name, int(korea), int(english), int(math)])

students_score.sort(key = lambda x: (-(x[1]), (x[2]), -(x[3]), x[0]))

for student in students_score:
    sys.stdout.write((student[0]) + '\n')