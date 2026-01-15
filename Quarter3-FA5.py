names = ["Me", "Lia", "Jake"]
total = []
steps = [
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
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