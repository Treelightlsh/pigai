import re


def strip_space(match):
    return match.group().replace(' ', '')


s = '"if pm               < 200 and pm > 30:"'
# ops = ['\+', '-', '\*', '/', '\*\*', '=', '>', '<', '>=', '<=', '!=', '\+=']
# op_str = '|'.join(ops)
# print(op_str)
res = re.sub(r'(\'|")(.*)\1', strip_space, s)
print(res)
