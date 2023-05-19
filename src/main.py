"""

digit recognition using raypyc

"""

from raypyc import *
import numpy as np
from src import number_recognizer


# ------------------------------------------------------------------------------------
# Program main entry point
# ------------------------------------------------------------------------------------
def main():
    # Initialization
    # ------------------------------------------------------------------------------------
    SCREEN_WIDTH: int = 28 * 20
    SCREEN_HEIGHT: int = 28 * 20

    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, b"Digit Recognition")

    array_image: np.ndarray = np.zeros((28, 28), dtype=np.float32)

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        # TODO: Update variables / Implement example logic at this point
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)
        draw_text(b"Congrats! You created your first window!", 190, 200, 20, LIGHTGRAY)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
