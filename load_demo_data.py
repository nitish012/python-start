import os, sys
sys.path.append('/demo/demo')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
 
import django
django.setup()
from quickstart.models import Student,Teacher,Department,Subject,ReportCard

def populate():
    python_teacher = add_teacher('gaurav','sharma','phy','NORM')
    python_department = add_department(python_teacher,'computer')
    python_student = add_student('rahul','gupta',12,15,'A',python_teacher,python_department)
    # python_subject = add_subject('sci',90)
    # python_reportcard = add_reportcard(python_student,'A',80,70,'Good',python_subject)   

    python_teacher = add_teacher('ankush','verma','math','CLST')
    python_department = add_department(python_teacher,'computer')
    add_student('mayank','gupta',15,19,'B',python_teacher,python_department)

    python_teacher = add_teacher('ayush','sharma','phy','NORM')
    add_department(python_teacher,'electrical')

    python_subject = add_subject('math',90) 
    python_subject = add_subject('phy',90)

    python_teacher = add_teacher('ram','sharma','eco','NORM')
    python_department = add_department(python_teacher,'electrical')
    python_student = add_student('mishu','gupta',12,15,'A',python_teacher,python_department)
    python_subject = add_subject('ms',90)
    python_report = add_reportcard(python_student,'A',80,70,'vGood') 
    # python_report.subjects.set(python_subject.subject_name,python_subject.marks, )
    python_report_subject = add_reportcard_subject(python_report,python_subject)
    
def add_teacher(fname,lname,sub,role):
    return Teacher.objects.get_or_create(first_name=fname, last_name=lname, subject=sub, role=role)[0]

def add_subject(sub,marks):
    s = Subject.objects.get_or_create(subject_name=sub, marks=marks)[0] 
    s.save()
    print("________________________",type(s))
    return s    
def add_department(teacher,branch):
    return Department.objects.get_or_create(head=teacher, branch_name=branch)[0]

def add_student(fname,lname,age,roll,sec,teacher,department):
    return Student.objects.get_or_create(first_name=fname,last_name=lname,age=age,roll_no=roll,
                                         sec=sec, teacher=teacher, department=department)[0]    

def add_reportcard(student, grade, total_marks, percentage, remarks):
    r = ReportCard.objects.get_or_create(student=student, grade=grade, total_marks=total_marks,
                                             percentage=percentage, remarks=remarks)[0]
    r.save()
    return r
    # r.subjects.add(subjects)  
    # r.save()     
    # return r                                  
def add_reportcard_subject(report,subjects):
    return ReportCard.objects.get_or_create(reportcard_id=report,subject_id=subjects)[0]

for teacher in Teacher.objects.all():
    print(teacher)

for sub in Subject.objects.all():
    print(sub)

for report in ReportCard.objects.all():
    print(report)    

populate()
