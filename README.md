[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14592674&assignment_repo_type=AssignmentRepo)

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

Test Case 1: Player Interaction

Test Description: Confirm that the player can jump and aviod taxis successfully. 

Test Steps:
1. start the game.
2. Observe the character's inital position and the movement of the taxi.
3. Tap the screen at the right timing to avoid getting hit by the taxi.
4. Verify that the character jumps over the taxi.
5. Continue jumping over taxi's.
Expected Outcome: The character successfully jumps over taxis, earning points with each successful jump, until the player fails to jump in time and gets hit by a taxi.

Test Case 2: Score Increment

Test Description: Ensure that the player's score increases correctly upon successful jump.

Test Steps:
1. Start the game.
2. Observe the inital score, which should start at 0.
3. Successful jump over the taxi.
4. Verify that the score increases by 1.
5. Repeat the process of jumping over taxis multiple times.
Expected Outcome: The score increases by 1 with each successful jump.

Test Case 3: Game Over Detection

Test Description: Verify that the game correctly detects when the player fails to jump in time and gets hit by a taxi.

Test Steps:
1. Start the game.
2. Observe the character and taxi movement.
3. Fail to jump in time to avoid a taxi.
4. Verify that the game displays a "Game Over" message.
Expected Outcome:

Test Case 4: Difficulty Progression

Test Description: Ensure that the game's difficulty increases over time.

Test Steps:
1. Start the game.
2. Continue playing the game.
3. Verify as the player aquires more points increase the sped of the taxis.
Expected Outcome: As the game progresses, the taxis would move faster. This requires the player to have quicker reflexes to avoid collisions. 

Test Case 5: Menu Navigation

Test Description: Test the navigation through the game's main menu.

Test Steps:
1. Start the game
2. Navigate through the main menu options (Start Game, Options, Quit).
3. Verify that each option is selectable and leads to the expected actions.
Expected Outcome: The main menu should allow the player to navigate through options and select them.