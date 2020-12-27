import sys
import os
import re


filenames = []
maximum = 0
dr =  os.getcwd()

files = [file for r, d, f in os.walk(dr) for file in f if file[0] != '.']

print(files)
# for x in files:
# 	num = re.findall(r'(\d+)', x)
# 	if num:
# 		maximum = max(int(num[0]), maximum)
# 		filenames.append((x, num[0]))

# l = len(str(maximum))

# for x in filenames:
# 	s = x[0].replace(x[1], x[1].rjust(l, '0'))
# 	# os.rename(x[0], s)
# 	print(x[0], s)
