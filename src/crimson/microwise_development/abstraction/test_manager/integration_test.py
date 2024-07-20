from abc import abstractmethod
from typing import List
from types import ModuleType


@abstractmethod
def extract_user_modules(target_module: str, entire_modules: List[str]) -> List[str]:
    """
    Returns modules, that are dependent on the target_module.
    """
    pass


@abstractmethod
def load_unittest_folder(target_module: str, output_dir: str) -> None:
    """
    Load the unittest folder of the target_module.
    """
    pass


@abstractmethod
def load_unittest_folders(target_modules: List[str], output_dir: str) -> None:
    """
    Load the unittest folders of the target_modules.
    It is preferred to be implemented by based on `load_unittest_folder`.
    """
    pass


@abstractmethod
def _load_unittest_folder_by_module(target_module: ModuleType, output_dir: str) -> None:
    """
    Load the unittest folder of the target_module.
    One of the methodologies for unittest share is to publish modules with their test.zip file.
    We can extract the test files to test the module as a user.

    Advantage:
        In this case, the exact unittests used for the version of module will be stored together.

    Disadvantage:
        Modules must be developed with the additional setup for the test uploading.
        For the purpose, the `test_loader` module is on development.
    """
    pass


@abstractmethod
def _load_unittest_folder_by_repository(
    repo_url: str, test_dir: str, output_dir: str
) -> None:
    """
    Load the unittest folder of the target_module.
    One of the methodologies for unittest share is to download the unittests directly from the repository for the module.

    Advantage:
        If the `test_loader` setting is missing, we can use this method,
        so that we can test the module without modifying it.

    Disadvantage:
        It is really difficult to generalize the tag of different versions of repositories.
        Therefore, it would be ideal to use this only for the resent unittests of the module.

    The `git_loader' module can be used for this purpose.
    """
    pass
