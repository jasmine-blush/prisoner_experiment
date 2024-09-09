# Prisoner Experiment
A simple python script that tests the Prisoner Experiment as seen in this [Veritasium video](https://www.youtube.com/watch?v=iSNsgj1OCLA).

## Concept ##
* There are 100 prisoners numbered 1-100 ...
* and 100 boxes numbered 1-100 in a room.
* Labels with the prisoners' numbers are randomly placed in the boxes, one per box
* Each prisoner enters the room one at a time and checks 50 boxes
* They must leave the room exactly as they found it and can't communicate with the others after
* If all 100 prisoners find their number during their turn in the room, they will all be freed. But even if one fails, they all lose.
* What is their best strategy?

## Strategies ##
1. a random pick strategy, where prisoners pick 50 random boxes
2. a circular pick strategy, where prisoners first pick the box with their own number on it, check the label in it and then pick the box with the number of the label on it; repeat

## Result ##
The result of the script correctly shows that, even though the success chance of each individual prisoner stays at 50% for both strategies, the circular pick strategy has a higher overall chance for ALL prisoners to find their number.
