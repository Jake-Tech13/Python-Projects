from typing import List, Dict, Optional
from abc import ABC, abstractmethod


class Command(ABC):
    """Base class for all game commands."""
    def __init__(self, name: str, aliases: List[str], help_text: str):
        self.name = name
        self.aliases = aliases
        self.help_text = help_text
    
    @abstractmethod
    def execute(self, game, args: List[str]) -> bool:
        """
        Execute the command.
        
        Args:
            game: The Game instance
            args: List of arguments passed to the command
            
        Returns:
            True if command executed successfully, False otherwise
        """
        pass
    
    def validate_args(self, args: List[str]) -> bool:
        """Validate command arguments. Override in subclasses if needed."""
        return True


# Command Registry and Dispatcher
class CommandRegistry:
    """Registry to store and manage all available commands."""
    def __init__(self):
        self._commands: Dict[str, Command] = {}
    
    def register(self, command: Command) -> None:
        """Register a command and all its aliases."""
        self._commands[command.name] = command
        for alias in command.aliases:
            self._commands[alias] = command
    
    def get_command(self, name: str) -> Optional[Command]:
        """Get a command by name or alias."""
        return self._commands.get(name.lower())
    
    def get_all_commands(self) -> Dict[str, Command]:
        """Get all registered commands (no duplicates)."""
        return {cmd.name: cmd for cmd in set(self._commands.values())}


class CommandDispatcher:
    """Dispatcher to execute commands based on user input."""
    def __init__(self):
        self.registry = CommandRegistry()
    
    def register(self, command: Command) -> None:
        """Register a new command."""
        self.registry.register(command)
    
    def dispatch(self, game, command_string: str) -> bool:
        """
        Parse and execute a command.
        
        Args:
            game: The Game instance
            command_string: Full command string from user input
            
        Returns:
            True if command executed successfully, False otherwise
        """
        parts = command_string.split()
        if not parts:
            return False
        
        command_name = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        command = self.registry.get_command(command_name)
        if not command:
            return False
        
        if not command.validate_args(args):
            return False
        
        try:
            return command.execute(game, args)
        except Exception as e:
            print(f"Error executing command: {e}")
            return False