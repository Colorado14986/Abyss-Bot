import json

f = open('./TextLogs/ActivityLog.txt', 'r')
d = dict()
lb = []
lb2 = {}
for line in f:
    line = line.strip()
    if line in d:
        d[line] = d[line] + 1
    else:
        d[line] = 1
sorted_dict = {}
sorted_keys = sorted(d, key=d.get)
for w in sorted_keys:
    sorted_dict[w] = d[w]
    limit = len(sorted_keys)
for key in reversed(sorted_dict.keys()):
    lb2[key] = d[key]

with open('./TextLogs/ActivityLog.json', 'w') as s2:
    s2.write(json.dumps(lb2, indent=1))
    s2.close()

with open('./TextLogs/ActivityLog.json', 'r+') as u:
    e = json.load(u)
    print(e)
