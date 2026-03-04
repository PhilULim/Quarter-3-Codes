names = ["Me","Illidan","Xerxes"]
total = []
steps = [
  [5000,4000,2500,7000,6000],
  [7500,4050,6000,4800,5000],
  [9000,2000,5000,6000,7000]
]

all_names = len(names)
for i in range(all_names):
   steps_row=sum(steps[i])
   total.append(steps_row)
   print("The total steps of", names[i],"is", steps_row)
highest_steps=total.index(max(total))
highest_steps_for_difference = max(total)
lowest_steps=min(total)
Difference= highest_steps_for_difference-lowest_steps
print("The person with the highest total number of steps is", names[highest_steps],"with",max(total),"steps.")
print("The difference between the highest and the lowest amount of steps is:",Difference)