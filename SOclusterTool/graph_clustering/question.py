from io import StringIO
from html.parser import HTMLParser

# Helper Class to parse HTML
class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()

# Question class for stackoverflow post
# Class instead of method is prefered for easy change to improve clustering process and for accessing meta information if requried
class Question:
    def __init__(self, obj, row_headers=None):
        if row_headers == None:
            self.question = obj
            self.setText(qflag=True)
        else:
            self.question = dict(zip(row_headers, obj))
            self.setText()

    def setText(self,qflag=False):
        if qflag == True:
            html = self.question
        else:
            html = self.question["Body"]
        s = MLStripper()
        s.feed(html)
        text = s.get_data()
        self.question_text = text

    def getText(self):
        return self.question_text