# 与正确的Python文件对比，用于批改学生的Python文件
class CorrectManager(object):
    def __init__(self):
        # correct_answer为正确答案，student_answer为学生答案,均为文件路径
        self.correct_answer = ''
        self.student_answer = ''

    def update_correctanswer(self, path):
        # 更新正确答案路径
        self.correct_answer = path

    def update_studentanswer(self, path):
        # 更新学生答案路径
        self.student_answer = path
