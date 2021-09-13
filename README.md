step -1

'''
create environment 

'''

# windows machine

goto annaconda prompt cell

cd <go to the folder you awnt to work with>

code .

''' code . will take you to the vs code with the required folder'''

step -2

in the vs code terminal

type "conda init"

"conda -n <envname> python=3.7 -y"

"conda activate <envname>"

step -3

create "reqirements.txt" file 

"pip install -r requirements.txt"

download the data set from the source

"put it in data_given folder"


git init

dvc init

dvc add data_given/<name of data>.csv

All change we have made will store in git

git add .

git commit -m "msg"