def timeProcess(line):
    x = line.split()
    timestamp = x[1]
    time = timestamp.split(':')

    if (int(time[0]) >= 5 and int(time[0]) <= 15): return 0
    if (int(time[0]) >= 16 and int(time[0]) <= 21): return 1
    return -1

def processResult(temp, cnt):
    if (cnt == 0): return 0
    ave = round(temp / cnt, 3)
    return ave

fhand = open("temp.txt", "r")
lines = fhand.readlines()

n = len(lines)
dailySum = 0
daySum = 0
nightSum = 0
cntDaily = 0
cntDay = 0
cntNight = 0
for i in range(1, n, 2):
    line = lines[i]
    line = line.strip()
    temperature = int(line)
    
    dailySum += temperature
    cntDaily += 1

    state = timeProcess(lines[i-1])
    if (state == 0):
        daySum += temperature
        cntDay += 1
    if (state == 1):
        nightSum += temperature
        cntNight += 1

aveDaily = processResult(dailySum, cntDaily)
aveDay = processResult(daySum, cntDay)
aveNight = processResult(nightSum, cntNight)

print("Average Daily Temperature:", aveDaily)
print("The average temperature in the range from 5h00 to 15h59'59':", aveDay)
print("The average temperature in the range from 16h00 to 21h59'59':", aveNight)

fhand.close()