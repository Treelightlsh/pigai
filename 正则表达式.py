import re

s = 'if pm += 200:'
ops = ['\+', '-', '\*', '/', '\*\*', '=', '>', '<', '>=', '<=', '!=', '\+=']
op_str = '|'.join(ops)
# print(op_str)
res = re.search(r' {1,}(%s) {1,}' % op_str, s)
print(res)
