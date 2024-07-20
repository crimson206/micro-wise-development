from abc import ABC, abstractmethod
from typing import List


class RequirementProvider(ABC):
    @abstractmethod
    def register(self, path: str, dependencies: List[str]) -> str:
        """
        Register dependencies with a specified path.
        It must return the expected content of the file.
        """
        pass

    @abstractmethod
    def generate_files(self) -> None:
        """
        Generate the requirement files based on the registered dependencies.
        """
        pass

    @abstractmethod
    def generate_content(self, dependencies: List[str]) -> str:
        """
        Return the expected content of the requirements.txt file given dependencies.
        """
        pass
