class ConsoleIO:
    """Handles console input and output operations.

    Provides a simple interface for writing to and reading from the console,
    abstracting the standard print and input functions.
    """

    def write(self, text):
        """Write text to the console.

        Args:
            text: The text to display.
        """
        print(text)

    def read(self, prompt):
        """Read user input from the console.

        Args:
            prompt: The prompt text to display to the user.

        Returns:
            The user's input as a string.
        """
        return input(prompt)
