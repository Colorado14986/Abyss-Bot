from urban import UrbanClient
client = UrbanClient()

defs = client.get_definition('twat')
n = []
d = []
e = []

for i in defs:
    d.append(i.definition)
    e.append(i.example)
print(d[0])
print(e[0])
