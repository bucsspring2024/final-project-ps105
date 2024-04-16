
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Flying Pigeon
## CS110 Final Project  Spring , 2024

1 Team Member

Team member names: Selina

***

## Project Description

My project aims to combine Flappy Bird and Crossy Road. Esentially it is like Crossy Road expect it will have a pigeon flying across the sky and the cars will be replaced with airplanes or other birds and helecopters and such.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design > Classes

class Pigeon:
    """
    Represents the player-controlled character in the game.
    """

    def __init__(self, x, y, img_file):
        """
        Initializes the pigeon object.
        Args:
            - x : int - starting x coordinate
            - y : int - starting y coordinate
            - img_file : str - path to img file
        """

class Obstacle:
    """
    Represents the obstacles in the game that the pigeon must avoid.
    """

    def __init__(self, x, y, img_file):
        """
        Initializes the obstacle object.
        Args:
            - x : int - starting x coordinate
            - y : int - starting y coordinate
            - img_file : str - path to img file
        """

    def update_position(self, x, y):
        """
        Updates the position of the obstacle.
        Args:
            - x : int - new x coordinate
            - y : int - new y coordinate
        Returns:
            None
        """

    def detect_collision(self):
        """
        Detects collision with the pigeon.
        Args:
            None
        Returns:
            None
        """

### Features

1. Click to start tab
2. Moveable character
3. Obsticle collison
4. Moving background
5. Game over screen

### Classes

- << You should have a list of each of your classes with a description >>

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
