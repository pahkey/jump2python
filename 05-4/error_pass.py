# error_pass.py
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass
