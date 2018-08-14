### Island: O'Reilly. Problem: Text Editor

import copy

class Text:
    def __init__(self):
        self._state = ""

    def write(self, text):
        if (self._state.startswith('[')):
            close_brac = self._state.find(']')
            self._state = self._state[ :-(close_brac + 1)] + text + self._state[-(close_brac + 1):]
        else:
            self._state += text
        
    def set_font(self, font_name):
        if (self._state.startswith('[')):
            close_brac = self._state.find(']')
            self._state = '[' + font_name + self._state[close_brac : -(close_brac)] + font_name + ']'
        else:
            self._state = '[' + font_name + ']' + self._state + '[' + font_name + ']'
        
    def show(self):
        return self._state
        
    def restore(self, text):
        self._state = text
        return self._state
        

class SavedText:
    def __init__(self):    
        self.versions = []

    def save_text(self, Text):
        text = copy.deepcopy(Text)
        self.versions.append(text)

    def get_version(self, ver_num):
        return self.versions[ver_num]._state




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()
    
    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"
    
    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "


