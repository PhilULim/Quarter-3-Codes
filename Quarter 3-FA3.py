steps = [[5000,4000,2500,7000,6000],
         [7500,4050,6000,4800,5000],
         [9000,2000,5000,6000,7000]]
people = ["Me","Illidan","Xerxes"]
am_people=len(people)
for i in range(am_people):
    print(people[i], steps[i])

max_steps_row1 = max(steps[0])
max_steps_row2= max(steps[1])
max_steps_row3=max(steps[2])

print("The max steps for row 1 is:",max_steps_row1,"\n The max steps for row 2 is:",max_steps_row2,"\n The max steps for row 3 is:", max_steps_row3)
avr_steps_1 = sum(steps[0])/len(steps[0])
avr_steps_2 = sum(steps[1])/len(steps[1])
avr_steps_3 = sum(steps[2])/len(steps[2])
print("The average steps for row 1 is:",avr_steps_1,"\n The average steps for row 2 is:",avr_steps_2,"\n The average steps for row 3 is:", avr_steps_3)