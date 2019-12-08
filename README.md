# RL-Snake-Game
This is an implementation in Keras and Pygame of deep Q-learning applied to the classic Snake game. This approach gives the system parameters related to its state, and a reward based on its actions. Initially the Bot has no information about the rules of game and what it needs to do. The goal for the agent is to figure it out and maximize the reward. 

# Requirements
Refer to [requirements.txt](../master/requirements.txt).

# Implementation Details

### State

Tuple with 13 values. Each value if 0/1.
| S.no  |    Description  				|
|------	|:---------------------------:	|
| 0 	|danger above player 			| 
| 1  	|danger below player    		|  
| 2  	|danger to the left of player 	|  
| 3  	|danger to the right of player 	|  
| 4  	|player moving up 				|  
| 5  	|player moving down 			|  
| 6  	|player moving left 			|  
| 7  	|player moving right 			|  
| 8  	|food on player's left 			|  
| 9  	|food on player's right 		|  
| 10  	|food below player 				|  
| 11 	|food above player 				|  
| 12 	|player's direction 			|  

### Reward 
* Food eaten - 10
* Game over - -10
* Anything else - 0

### DL model
* 1 input, 1 output and 2 hidden layers.
* 