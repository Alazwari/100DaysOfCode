# Day 74
print('##############################')
python = open('day074/python.txt', 'r')
print(python.read())
python.close()
print('##############################')
python = open('day074/python.txt', 'a')
txt = "\nThe best way we learn anything is by practice and exercise questions"
python.write(txt)
python.close()
python = open('day074/python.txt', 'r')
print(python.read())
python.close()
print('##############################')


