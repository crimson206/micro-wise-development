This is a part of the Readme that was drafted during the initial stages of Micro-Wise Development.
The advantages and characteristics of MWD may be documented more elaborately in the future, but for now, this material will be used as a temporary resource.

## Table Of Contents

## Advantages

- **Extreme Dependency Freedom**: 
    Develop your packages as general-purpose tools, avoiding overly specific features for your other packages. This approach ensures that all your packages can remain free from dependencies.

- **Easy to Initiate, Easy to Abandon**: 
    Unlike modules in a large package, individual modules in micro packages are not as critical. Feel free to experiment with new ideas, and delete them if they don't work out, without significant consequences.

- **Dedicated Version Control**: 
    In a large package with multiple modules, you need to create a pull request for any update, making it difficult to track changes across versions. With MicroWise Development, you only need to update the repository of target modules, simplifying version control.

- **Learn Development Process**: 
    MicroWise Development involves frequently creating new repositories. This process encourages regular setup and publication of small packages. The small scale allows for more experimentation with less risk, making it an ideal environment for implementing CI/CD through trial and error.

- **Clean Repository Management**: 
    Large packages can be challenging to review in their entirety. In MicroWise development, you can refactor any package within an hour, keeping your repositories clean and manageable.

- **AI-Assisted Development**: 
    While autonomous agents may struggle with large projects, they are well-suited for smaller, focused tasks. MicroWise Development aligns with the strengths of current AI technologies, potentially paving the way for more effective AI-assisted programming in the future.

## Examples

### Programming with AI

I uploaded all the useful files from [AutoPydantic](https://github.com/crimson206/auto-pydantic) repository.

- src/
- test/
- pytest coverage htmls
- pyproject.toml
- auto-pydantic-dev/

The scope of the contents is limited so that AI is not confused and can help you with large parts of your entire module.

<img src="sonnet_projects.png" alt="sonnet_projects" style="width: 100%; height: auto;">