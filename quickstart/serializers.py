from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import Student, Teacher, Department,ReportCard, Subject

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields =  ('first_name','last_name','age','roll_no')
        #exclude = ['teacher']
    

class TeacherSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)
    class Meta:
        model = Teacher
        fields = ('first_name','last_name','subject','role','students')
    

    def create(self, validated_data):
        print(validated_data)
        students_list = validated_data.pop("students")        
        teacher_qs = Teacher.objects.filter(
            last_name = validated_data.get('last_name', None),
            first_name = validated_data.get('first_name', None),
            subject = validated_data.get('subject',None)
        )
        if not teacher_qs:
            result = super(TeacherSerializer,self).create(validated_data)
           
        else:
            result = teacher_qs.first() 
    
        for students_data in students_list:
            student_qs = Student.objects.filter(
                last_name = students_data.get('last_name', None),
                first_name = students_data.get('first_name', None)  
            )
  
            if not student_qs:
                student = Student.objects.create(last_name = students_data.get('last_name', None),
                                             first_name = students_data.get('first_name', None),
                                             age = students_data.get('age',None),
                                             roll_no = students_data.get('roll_no',None),
                                             teacher = result,

                                            )
            else:
                student = student_qs.first()
                student.save()
            validated_data["student"] = student

        return result   
        
    def update(self, instance, validated_data):
        students_list = validated_data.get("students")
        for students_data in students_list:
            student_qs = Student.objects.filter(
                last_name = students_data.get('last_name', None),
                first_name = students_data.get('first_name', None),
            )
            if not student_qs:
                student = Student.objects.create(last_name = students_data.get('last_name', None),
                                            first_name = students_data.get('first_name', None),
                                            age = students_data.get('age',None),
                                            roll_no = students_data.get('roll_no',None),
                                            teacher=instance)
            else:
            
                student = student_qs.first()
                student.age = students_data.get('age', None)
                student.roll_no = students_data.get('roll_no', None)
                student.save()

        instance.student = student
        instance.save() 
        return instance


class DepartmentSerilaizer(serializers.ModelSerializer):
    head = TeacherSerializer()
    students = StudentSerializer(many=True)
    class Meta:
        model = Department
        fields = ('head','branch_name','students')
        

    def create(self, validated_data):
        print(validated_data)
        heads_list = validated_data.pop("head")        
    
        for heads_data in heads_list:
            head_qs = Teacher.objects.filter(
                last_name = heads_data.get('last_name', None),
                first_name = heads_data.get('first_name', None),  
            )
  
            if not head_qs:
                head = Teacher.objects.create(last_name = heads_data.get('last_name', None),
                                            first_name = heads_data.get('first_name', None),
                                            subject = heads_data.get('subject',None),
                                            role = heads_data.get('role',None),
                                            
                                        )
            else:
                head = head_qs.first()
                head.save()
            validated_data["head"] = head
        return super(DepartmentSerializer,self).create(validated_data)     


    def update(self, instance, validated_data):
        print(validated_data)
        heads_data = validated_data.get("head")
        head_qs = Teacher.objects.filter(
            last_name = heads_data.get('last_name', None),
            first_name = heads_data.get('first_name', None),
            )
        if not head_qs:
                head = Teacher.objects.create(last_name = heads_data.get('last_name', None),
                                            first_name = heads_data.get('first_name', None),
                                            subject = heads_data.get('subject',None),
                                            role = heads_data.get('role',None),
                                            department = instance
                                        )
        else:
            
            head = head_qs.first()
            head.subject = heads_data.get('subject', None)
            head.role = heads_data.get('role', None)
            head.save()

        instance.head = head
        instance.save() 
        return 

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'

class ReportCardSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    subjects = SubjectSerializer()

    class Meta:
        model = ReportCard
        fields = ('student','grade','total_marks','percentage','remarks','subjects')
