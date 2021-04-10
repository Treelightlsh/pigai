import re

s = 'if pm < 200 and pm > 30:'
ops = ['\+', '-', '\*', '/', '\*\*', '=', '>', '<', '>=', '<=', '!=', '\+=']
op_str = '|'.join(ops)
# print(op_str)
res = re.sub(r' {1,}(%s) {1,}' % op_str, r'\1', s)
print(res)
