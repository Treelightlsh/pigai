import re
import os


def get_py_statements(filepath):
    # 获取文件的语句列表
    # 获取文件的有效语句数，#开头的行与空行去掉
    # 返回语句数量
    f = open(filepath, encoding='utf-8')
    # 记录有效的语句数
    statement_list = []
    # 记录有效语句
    statement_no = 0
    # 缩进层级对应的语句
    indent_to_statement = {}
    # 存放按缩进空格数排序的语句
    indent_to_statement_list = []
    for line in f:
        if re.search('^ {0,}#', line):
            # 如果是以#开头，则此行是注释，略过此行
            continue
        if re.search('^ {0,}$', line):
            # 如果是空行，则略过
            continue
        # 获取每行开头的缩进空格数，先用正则匹配从开头到第一个非空字符，然后计算空格个数
        statement_no += 1
        start_space_count = re.search('^ {0,}\S', line).group().count(' ')
        if start_space_count not in indent_to_statement.keys():
            # 如果之前没有添加此缩进层级，则需要创建
            indent_to_statement[start_space_count] = [statement_no, ]
        else:
            # 已经添加过此层级缩进
            indent_to_statement[start_space_count].append(statement_no)
        statement_list.append(formatstr(line))
    # 根据key的值进行排序
    new_key_list = sorted(indent_to_statement.keys())
    # 按照key的值按顺序放进列表中
    for key in new_key_list:
        indent_to_statement_list.append(indent_to_statement[key])
    f.close()
    return statement_list, indent_to_statement_list


def formatstr(string):
    # 字符串格式化
    # if pm > 200     :
    # 以下操作符的两边去掉空格
    ops = ['\+', '-', '\*', '/', '\*\*', '=', '>', '<', '>=', '<=', '!=', '\+=', ':', '\(', '\)',
           '\[', '\]']
    op_str = '|'.join(ops)
    string = re.sub(r' {0,}(%s) {0,}' % op_str, r'\1', string)
    # 待改善的地方：需要判断是不在双引号或单引号中
    # 去掉字符串中的空格部分
    string = re.sub(r'(\'|")(.*)\1', strip_space, string).strip()
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
        self.answer_statement_info = None

    def update_answer(self, path):
        # 更新正确答案路径
        self.answer_path = path
        # 获取正确答案语句
        self.answer_statement_info = get_py_statements(self.answer_path)

    def update_paper(self, path):
        # 更新学生答案路径
        self.paper_path = path

    @staticmethod
    def split_sentence(string):
        # 按语句分割，暂时不用，先假设一行就是一条语句
        pass

    def compare(self):
        # 比较两个文件，如果不同则返回False，否则返回True
        if self.answer_statement_info != get_py_statements(self.paper_path):
            return False
        else:
            return True

    def com_files_lines(self):
        pass


correctmanager = CorrectManager()
correctmanager.update_answer('answer.py')
for root, dirs, files in os.walk('paper'):
    for file in files:
        if re.search('.py$', file):
            correctmanager.update_paper(os.path.join(root, file))
print(correctmanager.compare())
