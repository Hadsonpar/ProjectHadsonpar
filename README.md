# Website Project Hadsonpar 2024
Hadsonpar website project, developed in Python and Flask
## 1. Creating base structure of project
### 1.1. Creating files and directories the project from git bash
- **[git bash]** touch index.py    
- **[git bash]** mkdir templates
    - Now, creating html file
        - **[git bash]** touch home.html
        - **[git bash]** touch about.html
        - **[git bash]** touch projects.html
        - **[git bash]** touch contact.html
- **[git bash]** mkdir static
    - Now, creating directories to files the project
        - **[git bash]** mkdir images
        - **[git bash]** mkdir css
            - **[git bash]** touch style.css
        - **[git bash]** mkdir js
            - **[git bash]** touch main.js
        - **[git bash]** mkdir fonts
### 1.2. Validating and installing Framework
#### Python version validation - Command
- **[cmd]** python --version
#### Pip version validation - Command
- **[cmd]** pip --version
#### Flask Install
- **[cmd]** pip install flask
### 1.3. Load the project from Python terminal
- **[python]** python index.py
### 1.4. Base structure of the project - v1.0.1
![Base structure of the project - v1.0.1](doc/images/v101base-structure-of-the-project.png)
## 2. Bootstrap integration in the base project
### 2.1. Creating files and directories the project from git bash
- mkdir static
    - Now, creating directories to files the project
        - **[git bash]** mkdir vendor
            - **[git bash]** mkdir bootstrap
### 2.2. Bootstrap v5.1.3 download the files css and js
[Link download of Bootstrap](https://getbootstrap.com/docs/5.1/getting-started/download/)
## 3. Icons Bootstrap integration in the base project
### 3.1. Creating files and directories the project from git bash
- mkdir static
    - Now, creating directories to files the project        
        - **[git bash]** mkdir bootstrap-icons
        - Unzip the **bootstrap-icons-1.11.3.zip** file, and paste the entire **fonts** directory into the new **bootstrap-icons** directory
### 3.2. Icon Bootstrap v1.11.3 download the files css and js
- [Link download of Icon Bootstrap](https://icons.getbootstrap.com/), clic in download latest ZIP.
- [Link download of Icon Bootstrap from github](https://github.com/twbs/icons/releases/tag/v1.11.3), clic in bootstrap-icons-1.11.3.zip.
- [Link CDN of Icon Bootstrap](https://cdnjs.com/libraries/bootstrap-icons), referenced link CDN of Icon Bootstrap in website.
## 4. Header, navigation and footer implement in the base project
### 4.1. Creating files and directories the project from git bash