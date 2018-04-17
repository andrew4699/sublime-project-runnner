# sublime-npm-project
A utility for running programs (i.e. starting a Node server) when switching Sublime Text projects.

## Prerequisites
Follow the instructions to install Sublime Text&#39;s [Package Control](https://packagecontrol.io/installation)

## Installation
1. Open the **Command Palette** (default key-combo is **Ctrl+Shift+P**)
2. Select **&quot;Package Control: Install Package&quot;**
3. Search for **sublime-npm-project** and hit enter

## Configuration
By default, this package won&#39;t do anything. Go to **Project > Edit Project** and add a section called **&quot;projectrunner&quot;** like below:

    {
        "projectrunner":
        {
            "path": ".",
            "start": true
        },
        "folders":
        [
            {
                "path": "."
            }
        ]
    }

This will ask you when you open a new project whether you want to perform the startup action, which unless explicitly specified is **&quot;npm start&quot;**. Note that by default, this is run from your project path.

### Change startup action
        "projectrunner":
        {
            "path": ".",
            "start": "node scripts/start.js"
        },

### Change (relative) path
        "projectrunner":
        {
            "path": "react/",
            "start": true
        },

### Disable startup action
        "projectrunner":
        {
            "path": ".",
            "start": false
        },