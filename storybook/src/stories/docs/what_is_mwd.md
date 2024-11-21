# What is Micro Wise Development?

Micro Wise Development (MWD) is a revolutionary software development methodology that breaks down complex systems into micro-level modules, making development more manageable, maintainable, and AI-friendly.

## Table Of Contents

## Motivation or History

MWD (Micro Wise Development) is a Methodology that I (crimson206) first started around May 2024, heavily inspired by the concept of components from [React](https://react.dev/) and [Storybook](https://storybook.js.org/).

In its early stages, the goal was to create and distribute easily installable and stable copies of AI examples and usage methods, which were often scattered and unreliable. These examples were restructured into clear and stable abstractions implemented and distributed at the component level.

This later evolved into Micro Wise Development, a Development Methodology where all module development is broken down into micro-level small units, each developed in exclusive repositories.

## Micro Wise Development

Let’s say we are developing a high-level module called A. Depending on the complexity of the service that module A is expected to provide, the number of scripts required to implement it often exceeds hundreds. Two of my favorite open-source projects can serve as examples:

- [OpenAI Python GitHub](https://github.com/openai/openai-python/tree/main)
- [Storybook GitHub](https://github.com/storybookjs/storybook)

MWD rejects such massive repositories. If our module A actually requires hundreds or thousands of scripts like the above examples, they are all implemented as small modules divided into dozens or hundreds of repositories. These modules are then integrated to implement higher-level modules, ultimately implementing the top-level module A.

MWD fundamentally rejects the concept of massive repositories like the ones often seen in such projects. If module A truly requires hundreds or thousands of scripts, MWD advocates dividing these into dozens or hundreds of smaller repositories, where each repository implements a small module. These smaller modules are then integrated step by step to form higher-level modules, eventually culminating in the implementation of the top-level module, A.

In theory, even a complex module like A can be implemented using just a few simple scripts. This makes it easier to understand what A does and how it is implemented.