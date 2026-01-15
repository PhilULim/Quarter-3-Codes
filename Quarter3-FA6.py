names = ["Me", "Lia", "Jake"]
column_add=[]
days= ["Monday","Teusday","Wednesday","Thursday","Friday"]
steps = [
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
  ]
rows = len(steps)
column = len(steps[0])
for i in range(column):
    total = 0
    for j in range(rows):
        total += steps[j][i]
    column_add.append(total)

for k in range (len(days)):
    print("The amount of steps on",days[k], "is", column_add[k])

highest_step_day_index = column_add.index(max(column_add))
highest_step_day = max(column_add)
print("The day with the highest amount of steps is", days[highest_step_day_index],"with",highest_step_day,"steps.")