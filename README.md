# Digit Recognition using Raypyc

This project is a digit recognition system implemented using the Raypyc graphic library in Python. It utilizes machine
learning techniques to identify and classify handwritten digits.

## Features

- Graphic User Interface (GUI): The system provides a user-friendly interface for users to interact with the
  application.
- Digit Recognition: The application uses a machine learning model to recognize and classify handwritten digits.
- Real-Time Prediction: Users can draw digits directly on the GUI, and the system will provide real-time predictions for
  the drawn digit.
- Accuracy Evaluation: The project includes methods to evaluate the accuracy of the digit recognition model.

## Dependencies

- Python 3.x: Ensure you have Python 3.x installed on your system.
- Other dependencies: The other dependencies are listed in the [requirements.txt](src/requirements.txt) file.

## Usage

1. Clone the repository:
   ```
   git clone https://github.com/your-username/digit-recognition-raypyc.git
   ```

2. Change to the project directory:
   ```
   cd digit-recognition-raypyc
   ```

3. Install the project dependencies:
   ```
   pip install -r src/requirements.txt
   ```

4. Run the application:
   ```
   python src/main.py
   ```
5. While the GUI will open, the digit recognition model will be trained in the background. The training process may take
   a few minutes to complete (note that in this time the GUI will not respond).

6. After the network training, allowing you will be able to interact with the digit recognition system. You can draw a
   digit on the canvas,
   and the application will provide a prediction for the drawn digit.

## Acknowledgements

The machine learning model used for digit recognition is based on
the work in the [number-recognizer](https://github.com/mauro-balades/number-recognizer/tree/main) repository. I
extend my sincere thanks for providing the network architecture and inspiration for this project.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code for
personal and commercial purposes.