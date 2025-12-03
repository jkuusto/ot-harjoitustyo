from ui.console_io import ConsoleIO
from ui.ui import UI
from repositories.character_repository import character_repository
from repositories.counter_repository import counter_repository
from services.counterpicker_service import CounterPickerService


def main():
    """Run the application.

    Initializes the console I/O, service layer, UI, and repositories, then starts
    the main application loop.
    """
    io = ConsoleIO()
    service = CounterPickerService(character_repository, counter_repository)
    ui = UI(io, service)
    ui.start()


if __name__ == "__main__":
    main()
