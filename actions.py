general_info=[]

def validating(courses):
    while True:
        try:
            score=float(input(courses))
            if 0<=score<=100:
                return score
            else:
                print('the score should be between 0 to 100')
        except ValueError:
            print('invalid entrance')

        
        
def entering_information():
    global general_info
    try:
        amount=int(input('Enter the amount of students'))
    except:
        print('It is not valid')
        return
    for apprentices in range(amount):
        print(f"/n Student number {apprentices+1}")
        while True:
            full=input("Enter full name").strip()
            if full and all(l.isalpha() or l.isspace() for l in full):
                full=" ".join(full.split()).title()
                break
            print("Please not enter numbers o something like that")

        section=input("Enter the section").strip()
        
        spanish=validating('Spanish score')
        english=validating('English score')
        social=validating('Social score')
        science=validating('Science score')
        
        
        student_list={
            "name": full,
            "section": section,
            "spanish": spanish,
            "english": english,
            "social": social,
            "science": science,
            "average": (spanish+english+social+science)/4
        }
        general_info.append(student_list)
        print("student entered successfully")


def general_information():
    if not general_info:
        print('The student was not registered')
        return
    print("\ Students list")
    for i, student_list in enumerate(general_info, start=1):
        print(f'\ Student#{i}')
        print(f'Name: {student_list["name"]}')
        print(f'Section: {student_list["section"]}')
        print(f'Spanish: {student_list["spanish"]}')
        print(f'English: {student_list["english"]}')
        print(f'Social: {student_list["social"]}')
        print(f'Science: {student_list["science"]}')
        print(f'Average: {student_list["average"]:.2f}')
    
def top3():
    if len(general_info)<1:
        print("There are not registered students")
    three=sorted(general_info, key=lambda x:x['average'], reverse=True)[:3]


    print("\n Students Top 3!")
    for s,student_list in enumerate(three,start=1):
        print(f"\n #{s}-{student_list["name"]}")
        print(f"Section-{student_list["section"]}")
        print(f"Average-{student_list["average"]:.2f}")
def average_score():
    if not general_info:
        print("No students registered")
        return
    total_average= sum(student_list["average"] for student_list in general_info)
    form= total_average/len(general_info)
    print(f"the overall average is: {form:.2f}")
