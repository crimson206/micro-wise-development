from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from typing import List, Literal, Optional, Dict
from crimson.intelli_type import IntelliType
from typing import Generic, TypeVar

T = TypeVar("T")


class Scripts_(IntelliType, Dict[str, str], Generic[T]):
    """
    A dictionary where:
    - key: the command name (what you type in the terminal)
    - value: the entry point (module:function) specifying which function to run
    """


class TomlConfig(BaseModel):
    name: str
    version: str = Field(default="0.1.0")
    description: str = Field(default="Write the description of your module")
    dependencies: List[str] = Field(default=[])
    scripts: Optional[Scripts_[Dict[str, str]]] = Field(
        default=None
    )  # Added scripts field


class SetuptoolsConfig(TomlConfig):
    entry_points: Optional[Dict[str, List[str]]] = Field(default=None)
    # Add any setuptools-specific fields here


class HatchlingConfig(TomlConfig):
    build_targets: Optional[List[str]] = Field(default=None)
    # Add any hatchling-specific fields here


class PyprojectProvider(ABC):
    @abstractmethod
    def generate_content(
        self,
        builder: Literal["setuptools", "hatchling", "poetry"],
        tomlconfig: TomlConfig,
    ) -> str:
        """
        Return the expected content of pyproject.toml file given tomlconfig.
        The `generate_function` for different builders should be respectively prepared, and they are merged here.
        """
        pass

    @abstractmethod
    def generate_setuptools_content(
        self,
        tomlconfig: SetuptoolsConfig,
    ) -> str:
        """
        Return the expected content of pyproject.toml file given tomlconfig in setuptools syntax.
        """
        pass

    @abstractmethod
    def generate_hatchling_content(
        self,
        tomlconfig: HatchlingConfig,
    ) -> str:
        """
        Return the expected content of pyproject.toml file given tomlconfig in hatchling syntax.
        """
        pass
