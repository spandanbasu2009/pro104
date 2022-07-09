import csv
with open("data.csv") as f:
  reader = csv.reader(f)
  filedata = list(reader)

filedata.pop(0)
newdata = []
print(filedata)

for i in range(len(filedata)):
  num = filedata[i][1]
  newdata.append(float(num))

n = len(newdata)
total = 0

for j in newdata:
  total += j

mean = total/n
#print(newdata)

print(mean)
newdata = newdata.sort()

if(n % 2 == 0):
     median1 = float(newdata[n//2])
     median2 = float(newdata[n//2 - 1])
     median = (median1 + median2)/2
else:
  median = newdata[n//2]

print(median)