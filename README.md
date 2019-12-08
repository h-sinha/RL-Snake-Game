# RL-Snake-Game
This is an implementation in Keras and Pygame of deep Q-learning applied to the classic Snake game. This approach gives the system parameters related to its state, and a reward based on its actions. Initially the Bot has no information about the rules of game and what it needs to do. The goal for the agent is to figure it out and maximize the reward. 

# Requirements
Refer to [requirements.txt](../master/requirements.txt).

# Instructions
* Set game speed in line 16 of game.py.
* The agent uses pretrained model [weights.hdf5](../master/weights.hdf5). For training the model from scratch comment line 78 in DQN.py and set epsilong in line 17 of game.py to 80.
* Start the game using 
``` 
python game.py
```

# Implementation Details

### State

Tuple with 13 values. Each value if 0/1. 

| index |    Description  			    	  |
|-------|:-----------------------------:|
| 0 	  |danger above player 			      | 
| 1   	|danger below player    		    |  
| 2   	|danger to the left of player 	|  
| 3   	|danger to the right of player 	|  
| 4  	  |player moving up 				      |  
| 5   	|player moving down 			      |  
| 6   	|player moving left 			      |  
| 7   	|player moving right 			      |  
| 8  	  |food on player's left 		      |  
| 9  	  |food on player's right 	      |  
| 10    |food below player 			      	|  
| 11 	  |food above player 			      	|  
| 12 	  |player's direction 		      	|  

### Reward 
|Action        | Reward |
|--------------|:------:|
|Food eaten    |  10   |
|Game over     | -10    |
|Anything else |  0     |

### DL model
* 1 input layer with 13 neurons.
* 2 hidden layers each with 120 neurons.
* 1 output layer with 5 neurons. 5 output neurons as there are 5 possible actions - No change, move up, move down, move left, move right.

Initially the player performs random moves for exploration. Later the action to be taken is decided using the deep learning network.

# Results

<p align="center"> 
    <img src="../master/images/game1.gif">
    <br/>
  <b>1st game</b>
 </p>
 <p align="center"> 
    <img src="../master/images/game201.gif">
    <br/>
    <b>201st game</b>
 </p>


* After 100 games the agent consistently scores 15+ points.
* After 150 games the agent scores 25+ points.
* After 175 games the agent scores 35+ points
