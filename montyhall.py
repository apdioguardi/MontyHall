# monty hall problem

import random
import time

start_time = time.time()
doors = [1, 2, 3]
nloops = 1000000
changed_correct_sum = 0
same_correct_sum = 0
number_changed = 0
number_same = 0
progress_bar = []
progress_resolution = 10

for j in range(1, progress_resolution + 1):
    progress_bar += [int(j*nloops/progress_resolution)]

for i in range(0, nloops):
    prize_door = random.choice(doors) 
    non_prize_doors = filter(lambda door: door != prize_door, doors)
    chosen_door = random.choice(doors)
    percent_complete = float(i)/float(nloops)
    if i in progress_bar:
        print str(int(100*float(i)/float(nloops))) + "% complete"

    if prize_door != chosen_door:
        leftover_doors = filter(lambda door: door == prize_door or 
                                             door == chosen_door, doors)
    else:
        removal_door = random.choice(non_prize_doors)
        leftover_doors = filter(lambda door: door == prize_door or 
                                             door == removal_door, doors)

    switch_choice = random.randint(0,1)    
    if switch_choice == 1:
        chosen_door = filter(lambda door: door != chosen_door, leftover_doors)[0]
        number_changed += 1
    else:
        number_same += 1

    if chosen_door == prize_door and switch_choice == 1:
        changed_correct_sum += 1
    if chosen_door == prize_door and switch_choice == 0:
        same_correct_sum += 1

print "100% complete!"

changed_percent_correct = round(100*float(changed_correct_sum)/float(number_changed), 2)
same_percent_correct = round(100*float(same_correct_sum)/float(number_same), 2)
run_time = round(time.time() - start_time,2)

print "I win " + str(changed_percent_correct) + " % of the time if I change."
print "I win " + str(same_percent_correct) + " % of the time if I DO NOT change."
print "I took " + str(run_time) + " seconds to run."

print "changed_correct_sum + same_correct_sum = " + str(float(changed_correct_sum) + float(same_correct_sum))
print "number_changed + number_same = " + str(float(number_changed) + float(number_same))
