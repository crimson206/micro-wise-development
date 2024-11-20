## Motivation or History

MWD(Micro Wise Development)는 내가(crimson206) 2024년 5월 경 처음 시작한 Methodology로, [React](https://react.dev/)와 [Storybook](https://storybook.js.org/)의 component라는 개념에서 크게 영감을 받아 시작하게 되었다.

초기에는 여러 곳에 흩어져 있고 불안정한 AI 예제나 사용 방법들을 component 단위로 구현하고 배포하여, **적절한 추상화**와 **안정성**을 갖춘 상태로 쉽게 설치하고 사용할 수 있는 복사본을 만드는 것이 목표였다.

이러한 접근법은 이후 모든 모듈을 micro 수준의 작은 단위로 쪼개고, 각 단위가 독립적인 repository에서 개발되는 **Micro Wise Development**라는 새로운 개발 Methodology로 발전하게 되었다.


## What is Micro Wise Development?

우리가 A라는 High Level 모듈을 개발한다고 가정해보자.  
A라는 모듈이 제공해야 하는 서비스의 복잡성에 따라, 이를 구현하기 위해 작성되는 스크립트의 수가 수백 개를 넘어가는 경우가 흔하다. 내가 좋아하는 두 가지 오픈소스 프로젝트를 그 예로 들 수 있다.

- [OpenAI Python GitHub](https://github.com/openai/openai-python/tree/main)
- [Storybook GitHub](https://github.com/storybookjs/storybook)

MWD는 이러한 대규모 Repository를 거부한다. 만약 우리가 개발하려는 A가 위 예시처럼 수백, 혹은 수천 개의 스크립트를 필요로 한다면, MWD에서는 이를 **수십, 수백 개의 작은 repository로 나누어** 각각의 repository가 작은 모듈을 구현하도록 한다. 이후 이러한 작은 모듈들을 통합하여 상위 모듈을 구현하고, 최종적으로 최상위 모듈인 A를 완성하게 된다.

이론적으로, A와 같은 복잡한 모듈도 단 몇 개의 단순한 스크립트만으로 구현될 수 있다. 이러한 접근법은 A가 어떤 기능을 수행하는지, 그리고 그것이 어떻게 구현되었는지를 이해하기 훨씬 쉽게 만드는 것을 목표로 한다.
