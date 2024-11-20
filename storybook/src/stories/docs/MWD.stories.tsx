import React from 'react'
import { MDRender } from './MDRender'
import whatIsMWDString from './what_is_mwd.md?raw'
import visionString from './vision.md?raw'
import oldReadmeString from './old_readme.md?raw'

export default {
    title: 'Docs/Micro-Wise Development'
}

export const WhatIsMicroWiseDevelopment = {
    name: 'What is Micro-Wise Development?',
    render: () => (
      <div>
        <MDRender
          markdownString={whatIsMWDString}
        />
      </div>
    )
  };

export const Vision = {
render: () => (
    <div>
    <MDRender
        markdownString={visionString}
    />
    </div>
)
};

export const Advantages = {
render: () => (
    <div>
    <MDRender
        markdownString={oldReadmeString}
    />
    </div>
)
};