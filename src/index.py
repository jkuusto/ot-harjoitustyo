from ui.console_io import ConsoleIO
from ui.ui import UI
from repositories.character_repository import character_repository
from repositories.counter_repository import counter_repository


def main():
    io = ConsoleIO()
    ui = UI(io, character_repository, counter_repository)
    ui.start()


if __name__ == "__main__":
    main()
