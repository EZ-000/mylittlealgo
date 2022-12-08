import re

def solution(files):
    p = re.compile(r'(?P<HEAD>\D+)(?P<NUMBER>\d+)')
    files.sort(key = lambda x: (p.match(x).group("HEAD").upper(), int(p.match(x).group("NUMBER"))))
    return files
