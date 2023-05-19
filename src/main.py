"""

digit recognition using raypyc

"""

from raypyc import *
import numpy as np
from src import number_recognizer


def update_array_image_circle(array_image: np.ndarray, circle: Vector2, brush_size: int, left_down: bool):
    for y_update in range(
            int(circle.y - brush_size) // 20,
            int(circle.y + brush_size) // 20 + 1
    ):
        for x_update in range(
                int(circle.x - brush_size) // 20,
                int(circle.x + brush_size) // 20 + 1
        ):
            if not 0 <= x_update < 28 or not 0 <= y_update < 28:
                continue

            if left_down:
                array_image[y_update, x_update] = 1.0
            else:
                array_image[y_update, x_update] = 0.0


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
    brush_size: int = 5
    network_guess: int = 0

    # set up number recognizer network
    NN: number_recognizer.NumberRecognizer = number_recognizer.NumberRecognizer()

    NN.init()  # create a model
    NN.load()  # load the model

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # ------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        mouse_pos: Vector2 = get_mouse_position()
        mouse_wheel_move: int = get_mouse_wheel_move()

        # update brush size
        brush_size += mouse_wheel_move
        brush_size = max(brush_size, 1)

        if is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT):
            update_array_image_circle(array_image, mouse_pos, brush_size, True)
            network_guess = NN.recognize(array_image)
        elif is_mouse_button_down(MouseButton.MOUSE_BUTTON_RIGHT):
            update_array_image_circle(array_image, mouse_pos, brush_size, False)
            network_guess = NN.recognize(array_image)
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        begin_drawing()

        clear_background(BLACK)

        # draw grid
        for i in range(28):
            for j in range(28):
                draw_rectangle(j * 20, i * 20, 20, 20, fade(WHITE, array_image[i, j]))

        # draw brush
        draw_circle_lines(int(mouse_pos.x), int(mouse_pos.y), brush_size, GREEN)

        # draw network guess
        draw_text(f"The network guess the number: {network_guess}".encode(), 0, 0, 20, GREEN)

        end_drawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # ----------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # ----------------------------------------------------------------------------------


# Execute the main function
if __name__ == '__main__':
    main()
