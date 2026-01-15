steps = [[5000,4000,2500,7000,6000],
         [7500,4050,6000,4800,5000],
         [9000,2000,5000,6000,7000]]
people = ["Me","Illidan","Xerxes"]
am_people=len(people)
for i in range(am_people):
    print(people[i], steps[i])

print("Illidan's steps on Thursday:",steps[1][3])
print("Updating Xerxes's steps on Monday by 1000 from 7500")
steps[1][0]= 8500
print("Xerxes's updated steps", steps[1])

# Each row represents a persons amount of steps.
# Each column represents the steps made by each person per weekday.

# Reflection:
"Using the mini data-set helped me compare the amount of steps me and my friends made per day"
"It is also easier to operate with our data using the dataset."
