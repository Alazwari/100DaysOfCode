#Day 14
class Student:
    group = []
    def add_one(self, student):
        self.group.append(student)
        return self.group
    def add_group(self, student):
        self.group.extend(student)
        return self.group
    def add_to_position(self, student, position):
        self.group.insert(student, position)
        return self.group
    def delete_first(self):
        self.group.remove()
        return self.group
    def delete_position(self, position):
        self.group.pop(position)
        return self.group
    def delete_all(self):
        self.group.clear()
        return self.group
    def count_name(self, student):
        self.group.count(student)
        return self.group
    def check_name(self, student):
        if student in self.group:
            print(f'{student} is in the group')
        else:
            print(f'{student} is not in the group')
    def divide_group(self, position_1, position_2):
        new_group = self.group[position_1:position_2]
        return new_group
    def group_length(self):
        g_l = len(self.group)
        return g_l
    def change_name(self, new_studetn,position):
        self.group[position] = new_studetn
        return self.group

school_1 = Student()
school_1.add_group(['Abdulrahman','Ahmed', 'Khalid'])
school_1.add_one('Mohammed')
print(school_1.group_length())
print(school_1.group)
school_1.check_name('Mohammed')