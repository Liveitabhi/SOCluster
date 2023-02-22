import re

html = 'Hey I have doubt help <code> def foo(): print("Hello World") </code> \n <code> def bar(): print("Hello World") </code>'
code_snippets = re.findall(r'<code>(.*?)</code>', html, re.DOTALL)
question_text = re.sub(r'<code>.*?</code>', '', html, flags=re.DOTALL)
print(code_snippets)
print(question_text)