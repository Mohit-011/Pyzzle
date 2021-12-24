# Pyzzle
> ***A puzzle game coded entirely in Python.***

<p><em>This is a school project created by me, Mohit Singh.</em><br>

The .exe file, created from the main.py script, is a short puzzle game with a plethora of little features and details.</p>

<p>1. The moment you enter the game, it first checks if you are a returning player and displays a short tutorial accordingly. Even if the game has been played on your device once, it skips the tutorial.

![image](https://user-images.githubusercontent.com/83200950/147316557-9750f0f6-2eba-4bda-85ac-4e73b2b4dfec.png)</p>

<p>2. It then ask for your name. If you are a returning player, it then displays your highest score yet, else it skips to the main menu of the game.

Prompt for name: 
![image](https://user-images.githubusercontent.com/83200950/147316656-06a19db9-89a2-4e81-9a08-92cc53b198a4.png)

Displaying highest score of the player: 
![image](https://user-images.githubusercontent.com/83200950/147316739-e9c03be7-0e31-4c11-9d01-b7189bf2c0f9.png)</p>

<p>3. In the main menu, you can select one option from 'Play', 'Tutorial', 'Scoreboard', or 'Quit', to perform the respective actions. This selection can be performed by typing in the required command. I have also made sure that case doesn't matter anywhere in the game, making the experience just a bit better.

![image](https://user-images.githubusercontent.com/83200950/147316850-bc74224a-415e-4e5a-ac45-612af2a2e110.png)

 (a) Selecting 'Play' launches the main game. This consists of a series of questions which you have to answer correctly. Some of the questions also have certain time limits and you are given points on the basis of the time you take. The quicker you answer, greater points you score. If you answer incorrectly or take too much time, you lose the game. Here, I have created a short answer checking algorithm so that it is not necessary to enter all the words correctly. If even a part (single word) of the answer matches the corrcet answer, then full points are given. (For example, 'an egg' is treated to be same as 'egg' or 'the egg').
  
  ![image](https://user-images.githubusercontent.com/83200950/147317320-25e6eaa3-0b82-48a5-9961-d745da1c0945.png)
  
  (b) Selecting 'Tutorial' brings up the same short tutorial that is shown to new users.
  
  ![image](https://user-images.githubusercontent.com/83200950/147317418-6574af63-0efa-407b-805f-0c80d58031d7.png)
  
  (c) Selecting 'Scoreboard' brings up the scoreboard with a list of scores of all the players, arranged in descending order acoording to the respective scores. You are automatically returned to the main menu after 5 seconds.
  
  ![image](https://user-images.githubusercontent.com/83200950/147317642-c5bf1616-f559-4fb4-a385-6b80da17593c.png)
  
  (d) Selecting 'Quit' save the current progress and closes the game window.
  
  ![image](https://user-images.githubusercontent.com/83200950/147317724-de5e15a7-87c7-4bf1-87ee-5dae6198f0e5.png)</p>




## Troubleshooting Features:

<p>1. Right when the game starts and asks for your name, if you input 'reset' or 'restore', it will perforom the respective actions. 'Reset' renames the score.txt file to old_score.txt, thus creating a backup of the previous score as well as resetting the game to the fresh-install state. 'Restore' searches for the old_score.txt file and reverts it back to score.txt, thus bringing back the old scores. 

![image](https://user-images.githubusercontent.com/83200950/147319088-1c6f0d70-3b27-4a41-bf29-cea920348549.png)</p>

<p>2. While in the main menu, you can type 'reset' to perform the same action as in 1, except for the fact that in this case, the game also saves the current player's score in the backup and then closes the window.
  
  ![image](https://user-images.githubusercontent.com/83200950/147319224-4ac73db9-fb3b-40b6-b018-991ae1f98255.png)</p>

