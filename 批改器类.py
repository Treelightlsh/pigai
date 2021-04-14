import re


def strip_space(match):
    return match.group().replace(' ', '')


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

    @staticmethod
    def __formatstr(string):
        # 字符串格式化
        # if pm > 200     :
        # 以下操作符的两边去掉空格
        ops = ['+', '-', '*', '/', '**', '=', '>', '<', '>=', '<=', '!=', '+=', ':', '(', ')']
        op_str = '|'.join(ops)
        string = re.sub(r' {0,}(%s) {0,}' % op_str, r'\1', string)
        # 待改善的地方：需要判断是不在双引号或单引号中
        # 去掉字符串中的空格部分
        string = re.sub(r'(\'|")(.*)\1', strip_space, string)
