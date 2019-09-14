#Day 26
s = {1,3,5,7,8}
s.update([1,2,3])
print(s)
s.remove(8)
print(s)
s.clear()
print(s)

#############

d = {'name':'pigeon','type':'bird','skin cover':'feathers'}
print(d['type'])
d['skin cover'] = 'ubuntu'
print(d['skin cover'])