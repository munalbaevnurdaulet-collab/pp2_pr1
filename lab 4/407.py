#a = input()
#print(a[::-1])
import json
a = '{"age":"30","name":"nurdaulet"}'
b = json.loads(a)
print(b["age"])
