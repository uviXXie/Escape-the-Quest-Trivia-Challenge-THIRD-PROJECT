import pygame

class Screen:
    """Base class for all game screens.

    This class is designed to be inherited by other screen classes that represent
    different stages or sections of the game. It provides three essential methods:
    `handle_events`, `update`, and `render`, which can be customized in derived classes.
    """

    def handle_events(self, events):
        """
        Handles input events like key presses, mouse clicks, etc.

        Args:
            events (list): List of pygame events that need to be processed.
        """
        pass

    def update(self):
        """
        Updates the game logic for the current screen (e.g., player movement, enemy logic, etc.).
        """
        pass

    def render(self, screen):
        """
        Draws all the elements for the current screen (e.g., background, sprites, UI) onto the game screen.

        Args:
            screen (pygame.Surface): The surface where the screen elements are drawn.
        """
        pass


class ScreenManager:
    """Screen manager for handling transitions and flow between different screens.

    The `ScreenManager` class is responsible for managing multiple screens in the game.
    It allows you to register screens, set the current screen, and update and render the active screen.
    It helps manage the flow of the game by switching between screens like the main menu, gameplay, and game over screens.
    """

    def __init__(self):
        """
        Initializes the ScreenManager with an empty dictionary of screens and no current screen.
        """
        self.screens = {}  # Dictionary to store the registered screens
        self.current_screen = None  # Variable to hold the current active screen

    def register_screen(self, name, screen):
        """
        Registers a screen with a specified name.

        Args:
            name (str): The name of the screen to register.
            screen (Screen): The screen object to register.
        """
        self.screens[name] = screen

    def set_current_screen(self, name):
        """
        Sets the current screen to be displayed.

        Args:
            name (str): The name of the screen to set as the current screen.

        Raises:
            ValueError: If the screen with the given name is not registered.
        """
        if name in self.screens:
            self.current_screen = self.screens[name]
        else:
            raise ValueError(f"The screen '{name}' is not registered.")

    def handle_events(self, events):
        """
        Handles input events (like key presses) for the current screen.

        Args:
            events (list): List of pygame events that need to be processed.
        """
        if self.current_screen:
            self.current_screen.handle_events(events)

    def update(self):
        """
        Updates the game logic for the current screen.

        This method is called every frame to update the current screen's state (e.g., moving characters, updating scores).
        """
        if self.current_screen:
            self.current_screen.update()

    def render(self, screen):
        """
        Draws the current screen to the specified surface.

        Args:
            screen (pygame.Surface): The surface where the current screen elements are rendered.
        """
        if self.current_screen:
            self.current_screen.render(screen)

