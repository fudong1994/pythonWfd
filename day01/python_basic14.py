"""
知识点1：注释、命名规则、保留字
"""

# 注释1：# 代表单行注释
# 注释2： 多行注释

'''
多行注释1
多行注释1
多行注释1
'''

"""
多行注释2
多行注释2
多行注释2
"""

# 快捷键 快速注释：Ctrl + /

# 多行注释3
# 多行注释3
# 多行注释3

# 命名规则
# 1、不能以数字开头
name = "小花"
# 6name = "小王"  该行代码错误，不能以数字开头
# 2、不能用保留字
# False = '小王'  该行代码错误，不能使用保留字
# 保留字有哪些？
import keyword  # 导入keyword 模块

print(keyword.kwlist)
'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''
