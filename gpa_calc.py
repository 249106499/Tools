from _pydecimal import Decimal, Context, ROUND_HALF_UP


course_record = []
primary_courses = """
90 5
91 5

74 5

83 4
85 5

74 3.5
73 3.5
72 3.5

78 3.5

89 3.5
""".split()

last2year_courses="""
76 4
85 1
85 2
83 4
90 4.5
85 5

91 2
94 2
84 3.5
74 3.5
73 3.5
87 0.5
72 3.5
74 2.5

76 3.5
78 3.5
98 2
78 2.5
73 2.5
90 2
77 2.5
91 2

87 0.5
90 3
89 3.5
74 2.5
83 3.5
""".split()

knowledge="""98 4
97 4
94 3.9
92 3.9
91 3.8
90 3.8
89 3.8
87 3.7
85 3.6
84 3.5
83 3.5
80 3.3
79 3.2
78 3.1
77 3
76 2.9
75 2.8
74 2.7
73 2.6
72 2.5
71 2.4"""
full_knowledge="""
80 2
90 2
85 2
90 5

"""
a=knowledge.split('\n')
scores = [Decimal(i.split()[0]) for i in a]
marks = [Decimal(i.split()[1]) for i in a]
score2mark = lambda score:Decimal(4-3*(100-score)*(100-score)/1600).quantize(Decimal('1.0'),ROUND_HALF_UP)

marks_test = [score2mark(i) for i in scores]
print(a,scores,marks,marks_test,marks==marks_test)



def weighted_gpa(course_list):
    sumed_weight = Decimal(0)
    sumed_value = Decimal(0)
    for i in range(int(len(course_list)/2)):
        weight = Decimal(course_list[2*i+1])
        sumed_weight = sumed_weight + weight
        mark = score2mark(Decimal(course_list[2*i]))
        sumed_value = sumed_value + weight * mark
        
    print(sumed_value/sumed_weight)

weighted_gpa(primary_courses)
weighted_gpa(last2year_courses)