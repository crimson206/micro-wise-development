# Orchestration

A comprehensive documentation summarizing the establishment of the framework.

While I am developing in the `Micro-wise Development` style, it doesn't mean that I am developing using the `Micro-wise Development framework`. Though the style offers many advantages, it also has shortcomings. To overcome these, we need to develop the framework, and this document is to track the process.

## Modules

Modules without an underscore are in development.
Modules with an underscore are planned ideas and abstractions.

### Dependency Manager

1. Currently used to analyze dependencies between micro modules.
2. Uses toml files from cloned repositories locally.
3. [2] is not ideal because we don't always have all the repository files.
4. It is uncertain if using the toml file is the best approach. Dependency management must be controlled in a more detailed manner.

### Git Loader

1. Downloads a file or files in a directory from a repository.
2. Can support the `dependency-manager`.

### Test Loader

1. Helps modules by uploading test.zip files and extracting them.
2. Usage:
    - Influence Test:
        - When a module is updated, it can download all the user modules' tests and run them.
        - Serves as an integration test.
        - If it doesn't pass tests from user modules:
            - If the change is justified, we update the high-level version numbers.
            - If it is considered a bug, we don't publish the new version and proceed with debugging.
    - Dependency Test:
        - When unit tests of the current module fail, we can download the tests from dependencies.
        - If the tests of dependencies fail, we should debug the dependencies first, or change the versions of dependencies.
3. Naming is somewhat problematic. A folder starting with "test" is not ideal as a module.

### Versioning

1. Collects available versions of modules.
2. Future:
    - It would be beneficial if it could control post-management tasks, such as yanking, and so on.
    - These functionalities could be divided into different micro modules.

### _Template Manager

1. We are currently using a fixed template repository, which is not ideal (not flexible).
2. We need a dynamic template manager capable of updating outdated templates and offering a variety of template options.

### _Git Controller

1. We may need to update multiple repositories at once.
2. Would it be a good idea to automatically edit the `main` branch?

### _Spec Loader

1. It is currently difficult to know:
    - What modules I have
    - What modules are useful
    - What modules are abandoned
    - What modules are active
    - What modules are stable
    - The coverage of modules
2. We need a module to collect this information.

### _Tagger

Some modules might be developed for a specific purpose. This micro-wise development is a good example. It would be better to tag specific modules with their target projects. For this purpose, we will need a tagging manager.

## To-Do

- Enable 'User test (integration test)' and 'Dependency test'.
- Make the linear comb, dependency range test possible.
