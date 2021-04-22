import re


def get_py_statements(filepath):
    # 获取文件的语句列表
    # 获取文件的有效语句数，#开头的行与空行去掉
    # 返回语句数量
    f = open(filepath, encoding='utf-8')
    statement_list = []
    for line in f:
        if re.search('^ {0,}#', line):
            # 如果是以#开头，则此行是注释，略过此行
            continue
        if re.search('^ {0,}$', line):
            # 如果是空行，则略过
            continue
        statement_list.append(formatstr(line))
    f.close()
    return statement_list


def formatstr(string):
    # 字符串格式化
    # if pm > 200     :
    # 以下操作符的两边去掉空格
    ops = ['\+', '-', '\*', '/', '\*\*', '=', '>', '<', '>=', '<=', '!=', '\+=', ':', '\(', '\)']
    op_str = '|'.join(ops)
    string = re.sub(r' {0,}(%s) {0,}' % op_str, r'\1', string)
    # 待改善的地方：需要判断是不在双引号或单引号中
    # 去掉字符串中的空格部分
    string = re.sub(r'(\'|")(.*)\1', strip_space, string)
    return string


def strip_space(match):
    # 正则表达式中匹配到的字符串中的空格去掉
    return match.group().replace(' ', '')


# 与正确的Python文件对比，用于批改学生的Python文件
class CorrectManager(object):
    def __init__(self):
        # correct_answer为正确答案，student_answer为学生答案,均为文件路径
        self.answer_path = ''
        self.paper_path = ''
        self.answer_statement_list = []

    def update_correctanswer(self, path):
        # 更新正确答案路径
        self.answer_path = path
        # 获取正确答案语句
        self.answer_statement_list = get_py_statements(self.answer_path)

    def update_paper(self, path):
        # 更新学生答案路径
        self.paper_path = path

    @staticmethod
    def split_sentence(string):
        # 按语句分割，暂时不用，先假设一行就是一条语句
        pass

    def compare(self):
        # 比较学生答案与标准答案，判断是否正确，正确返回True，否则返回False
        # 暂时以一行为一个语句比较
        # 首先判断语句数是否一致，不一致则判为程序错误
        # 获取学生的有效语句列表
        paper_statement_list = get_py_statements(self.paper_path)
        if len(paper_statement_list) != len(self.answer_statement_list):
            # 如果语句数不相同，则返回false
            return False
        else:
            # 逐个语句比较，如果语句均相同，则返回True，否则有一个语句不同，则返回False
            # 注意要判断缩进
            # 读取答案文件
            f = open(self.correct_answer, encoding='utf-8')
            temp = f.readlines()
            f.close()

    def com_files_lines(self):
        pass


# correctmanager = CorrectManager()
# correctmanager.update_correctanswer('correct_answer.py')
# correctmanager.compare()
# print(formatstr("if pm > 200:"))
# print(count_valid_statement('correct_answer.py'))
print(get_py_statements('correct_answer.py'))
