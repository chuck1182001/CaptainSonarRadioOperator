# CaptainSonarRadioOperator

This repository is made to take the role of the radio operator in captain sonar. Please don't use this to cheat.

When given the movements of the enemy, the bot will output a map of possible locations the enemy could be at.

This is just a working prototype right now with more work to be done. Any help is much appreciated so don't hesitate to make pull requests!


To use, input the map you are playing on within the CaptainSonar.py file. "o" means open tile, "i" means island
Also you will need to input the size and number of quadrants of the map. Size is the size of one side of the map.

Current working commands:

Enemy movements:  
    N - Enemy moves North  
    S - Enemy moves South  
    E - Enemy moves East  
    W - Enemy moves West  

Enemy actions:  
    ENEMY TORPEDO - will take in the position of the enemy torpedo and only show possbile positions 4 moves away  
    SURFACE - will take the quadrant the enemy appears in and filter out positions not in that quadrant  

Allied actions:  
    DRONE - Will take in the quadrant guess and result and filter out positions based on result  
    SONAR - Will filter out all possible positions that do not fit within either piece of given info  
    TORPEDO - Will take in torpedo location and filter out possible locations based on result of shot  
    MINE DETONATION - Same as TORPEDO  
  
Features to add:  
    Enemy Silent Running  
    Map of possible enemy mines  
    Retrace enemy position from detonated mine position  