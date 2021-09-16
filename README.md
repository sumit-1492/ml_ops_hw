step -1

```bash
create environment 
```

# commands for windows machine

goto annaconda prompt cell

```bash
cd <"go to the folder you awnt to work with">
```

```bash
code .
```

 code . will take you to the vs code with the required folder

step -2

In the vs code terminal

```bash
conda init
```

```bash
conda -n <"envname"> python=3.7 -y
```

```bash
conda activate <"envname">
```

step -3

```bash
create reqirements.txt file 
```

```bash
pip install -r requirements.txt
```

```bash
download the data set from the source
```

```bash
put it in data_given folder
```


```bash
git init
```

```bash
dvc init
```

```bash
dvc add data_given/<"name of data">.csv
```

All change we have made will store in git

```bash
git add .
```

```bash
git commit -m "msg"
```

tox command-
```bash
tox
```
for rebuilding -
```bash 
tox -r
```
pytest command -
```bash 
pytest -v
```

setup commands -
```bash
pip install -e .
```

bulid your own package command -
```bash
python setup.py sdist bdist wheel
```


create an artifacts folder


mlflow server command -

mlflow server
    --backend-store-uri sqlite:///mlflow.db
    --default-artifact-root ./artifacts
    --host 127.0.0.1 --port 5000
