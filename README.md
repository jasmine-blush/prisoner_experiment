# Prisoner Experiment
Implementation of the Prisoner Experiment as seen in Veritasium video: https://www.youtube.com/watch?v=iSNsgj1OCLA

### Concept ###
* 100 prisoners numbered 1-100
* 100 boxes numbered 1-100 in a room
* Labels with the prisoners' numbers are randomly placed in the boxes, one per box
* Each prisoner may enter the room one at a time and check 50 boxes
* They must leave the room exactly as they found it and can't communicate with the others after
* If all 100 prisoners find their number during their turn in the room, they will all be freed. But even if one fails, they all lose.
* What is their best strategy?

### Implements ###
1. a random pick function, where prisoners pick 50 random boxes
2. a circular pick function, where prisoners first pick the box with the label corresponding to their number and then repeatedly the box with the label of the number contained in the previous box

### Inputs ###
Number of runs and number of prisoners. (default 100 for both)

### Outputs ###
* The number of successful runs (Runs where ALL prisoners managed to find their number)
* The success chance relating to the number of runs performed
* The success chance of the individual prisoners


### Result ###
Even though the success chance of each individual prisoner stays at 50% for both strategies, the circular pick strategy has a higher overall chance for ALL prisoners to find their number.