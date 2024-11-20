import React from 'react'
import { Talkative } from '@crimson206/talkative'
import { PrimeCodePlugin } from '@crimson206/markdown-prism-code-plugin';
import { BootstrapThemePlugin } from '@crimson206/bootstrap-theme-plugin';

export interface MDRenderProps {
    markdownString: string
}

export const MDRender: React.FC<MDRenderProps> = ({markdownString}) => {

  const codePlugin = new PrimeCodePlugin('tomorrow');
  const { CodeStyleSelector, codeExecute } = codePlugin.useComponent();

  const themePlugin = new BootstrapThemePlugin('cerulean');
  const { ThemeSelector } = themePlugin.useThemeComponent();

  const components = {
    code: codeExecute,
  }

  return (
    <div>
        <Talkative
          markdownString= {markdownString}
          components = {components}
          showExternalToggle={true}
          externalToggleLabel='Show Style Controls'
          externalReactComponents={[
            <ThemeSelector key="theme" />,
            <CodeStyleSelector key="code" />,
          ]}
        />
      </div>
    )
}

