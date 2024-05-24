# Setup Chrome driver 🔧

## Run the following commands 🚀
##
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
##
    brew install chromedriver --cask  
##
    xattr -d com.apple.quarantine $(which chromedriver)


## Install pipenv 💻 : 

##
     pip install pipenv --user
##
    pipenv install
##
    pipenv run python3 scrappingCarvana2.0.py 

 ### Don't forget to setup the python virtual environment on vscode. 💭 

> `Cmd + Shift + P` Search for  `python: select interpreter` and choose the one with your `repo name-` eg `"carListingScrape-..."`