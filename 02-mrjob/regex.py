import re

WORD_RE = re.compile(r'[\w]+')

words = WORD_RE.findall('big data, :hadoop,,; (hello @ world!), 007, 345__, _')
print(words)