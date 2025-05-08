#!/bin/bash

# chmod u+x scipt


mkdir test_project
cd test_project

pipenv install


#pipenv install scipy
#pipenv install scikit-learn
#pipenv install gensim

#pipenv install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu




mkdir project
cd project
pipenv install
	pipenv shell
	exit
pipenv install [package]


pipenv uninstall package_name

pipenv --rm


