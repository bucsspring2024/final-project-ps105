[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14592674&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Block Jump (doodle jump knock off)
## CS110 Final Project  Spring , 2024

1 Team Member

Team member names: Selina

***

## Project Description

My project aims to replicate but simplify the already poipular game Doodle Jump. The player will be a square jumping on rectangles.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design > Classes

class Player:
    """
    Represents the player-controlled character in the game.
    """

    def __init__(self, x, y, img_file):
        """
        Initializes the player object.
        Args:
            - x : int - starting x coordinate
            - y : int - starting y coordinate
            - img_file : str - path to img file
        """

class Platform:
    """
    Represents the platforms in the game that the player must hop on to survive.
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

1. Player class: Represents the player character in the game.
2. Platform class: Represents the platforms that the player can jump on in the game.

## ATP

Test Case 1: Player Movement

Test Description: Confirm that the player track the user's mouse and move from side to side.

Test Steps:
1. Start the game.
2. Observe the character's inital position and the movement of the platoform.
3. Move the mouse to the right.
4. Verify that the player moves to the right.
5. Move the mouse to the leeft.
6. Verify that the player moves to the left.
Expected Outcome: The character successfully tracks the mouse and moves right if the mouse moves right and moves left if the mouse moves left.

Test Case 2: Score Increment

Test Description: Ensure that the player's score increases correctly upon successful jump.

Test Steps:
1. Start the game.
2. Observe the inital score, which should start at 0.
3. Successful jump on the platform.
4. Verify that the score increases by 1.
5. Repeat the process of jumping on platforms multiple times.
Expected Outcome: The score increases by 1 with each successful jump.

Test Case 3: Game Over Detection

Test Description: Verify that the game correctly detects when the player fails to jump in time and falls off the screen.

Test Steps:
1. Start the game.
2. Observe the character movement.
3. Fail to jump in time and falls of the screen.
4. Verify that the game displays a "Game Over" message.
Expected Outcome: When the character falls off the scsreen, a game over message is displayed.

Test Case 4: Collison Detection

Test Description: Ensure that collisions between the player and the platform are detected correctly.

Test Steps:
1. Start the game.
2. Continue playing the game.
3. Verify as the player aquires more points increase the sped of the taxis.
Expected Outcome: As the game progresses, the taxis would move faster. This requires the player to have quicker reflexes to avoid collisions. 

Test Case 5: Menu Navigation

Test Description: Test the navigation through the game over page.

Test Steps:
1. Start the game
2. Fall off the screen to display the game over message
3. Verify that each option (Play again, quit) is selectable and leads to the expected actions.
Press "Play Again"
4. Takes you back to the initial screen to play the game again.
5. Fall off the screen
6. Press quit
7. The game will exit
Expected Outcome: The menu should allow the player to navigate through options and select them. If the player chooses to play again, they will be taken back to the starting screen. If the player chooses to quit, the screen wil close.