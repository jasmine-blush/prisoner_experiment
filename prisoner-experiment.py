import random


number_of_prisoners = 100
runs_amount = 1000

#represents a single box with a label on it and a number inside
class Box:
    def __init__(self, label, number):
        self.label = label
        self.number = number

    def __str__(self):
        return str(self.label) + ":" + str(self.number)
        

#returns X boxes with sorted labels and one number inside, chosen randomly
#X = number of prisoners
def populateBoxes():
    boxes = []
    
    labels = []
    for i in range(number_of_prisoners):
        labels.append(i + 1)
    numbers = labels.copy()
    for x in range(5): #shuffles numbers 5 times (chosen arbitrarily)
        random.shuffle(numbers)

    for i in range(number_of_prisoners):
        boxes.append(Box(labels[i], numbers[i]))

    return boxes


def circularPickStrategy(boxes):
    successes = 0
    succeeded = True
    
    for prisoner in range(number_of_prisoners):
        found_own_number = False
        picks = 0
        pick_index = prisoner
        while (picks < number_of_prisoners/2) and not found_own_number:
            pick_number = boxes[pick_index].number
            if pick_number == (prisoner+1):
                found_own_number = True
                break
            pick_index = pick_number-1
            picks += 1
        if found_own_number:
            successes += 1
        else:
            succeeded = False
            
    return (succeeded, successes)


def randomPickStrategy(boxes):
    successes = 0
    succeeded = True
    
    for prisoner in range(number_of_prisoners):
        found_own_number = False
        picks = 0
        opened_boxes = []
        while (picks < number_of_prisoners/2) and not found_own_number:
            pick_index = random.randint(0, number_of_prisoners-1)
            while(pick_index in opened_boxes):
                pick_index = random.randint(0, number_of_prisoners-1)
            pick_number = boxes[pick_index].number
            if pick_number == (prisoner+1):
                found_own_number = True
                break
            opened_boxes.append(pick_index)
            picks += 1
        if found_own_number:
            successes += 1
        else:
            succeeded = False
            
    return (succeeded, successes)

def main():
    #perform runs
    prisoners_succeeded = 0
    runs_succeeded = 0
    for x in range(runs_amount):
        boxes = populateBoxes()
        #succeeded, successes = circularPickStrategy(boxes)
        succeeded, successes = randomPickStrategy(boxes)
        prisoners_succeeded += successes
        runs_succeeded += int(succeeded)

    #output results
    success_chance = (runs_succeeded / runs_amount) * 100
    prisoner_chance = (prisoners_succeeded / (runs_amount * number_of_prisoners)) * 100
    print("Runs: " + str(runs_amount)
          + "; Succeeded Runs: "
          + str(runs_succeeded)
          + "; Success Chance: "
          + str(success_chance)
          + "%; Prisoners Success Chance: "
          + str(prisoner_chance) + "%")
    


if __name__ == "__main__":
    main()
