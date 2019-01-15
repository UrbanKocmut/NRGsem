import csv

with open('../GK1_520_125.xyz', 'r') as f:
  reader = csv.reader(f,delimiter=';')
  data = list(reader)

minX = float(min(data, key=lambda el: float(el[0]))[0])
minY = float(min(data, key=lambda el: float(el[1]))[1])
minZ = float(min(data, key=lambda el: float(el[2]))[2])
print(minX, minY, minZ)

transformed = list(map(lambda x: [str(int(round((float(x[0])-minX)))),str(int(round((float(x[1])-minY)))),str(int(round((float(x[2])-minZ))))],data))

f = open('../GK1_520_125_out.xyz','w')
for line in transformed:
    f.write(line[0]+","+line[1]+","+line[2]+"\n")
f.close()