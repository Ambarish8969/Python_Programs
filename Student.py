class Student:

    school="Telusko University"

    def __init__(self,stu_name,stu_branch,stu_sem,stu_marks):
        self.stu_name=stu_name
        self.stu_branch=stu_branch
        self.stu_sem=stu_sem
        self.stu_marks=stu_marks
    
    def checkBranch(self):
        if(self.stu_branch=="CS"):
            print("IT Student.")
        else:
            print("Not IT Student.")

    @classmethod
    def getSchool(cls):
        print(f"School is : {cls.school}")

    @staticmethod
    def getInfo():
        print("He is a Good Student.")

obj=Student("Ambarish","EC",8,99)
obj.checkBranch()
obj.getSchool()
obj.getInfo()