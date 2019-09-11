#Day 18
#1
class Language:
    group = []
    def add_group(self, student):
        self.group.extend(student)
        return self.group
    def add_to_position(self, position, student):
        self.group.insert(position, student)
        return self.group
    def delete_first(self, student):
        self.group.remove(student)
        return self.group
    def count_name(self, student):
        return self.group.count(student)     
code = Language()
code.add_group(('java', 'python', 'swift', 'dart', 'javascript', 'php'))
code.add_to_position(5, 'python')
code.delete_first('dart')
print(f"""The lis is {code.group}.
And there are {code.count_name('python')} python in the list.""")

#2
languages = ['java', 'python', 'swift']
[print('python is in the list') if language == 'python' else '' for language in languages]
