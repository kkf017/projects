# Example of application development

This app is an example of Django app (back-end) to manage Users and Post-it.

## Prerequisites
Install poetry:
```python
curl -sSL https://install.python-poetry.org | python3 -
```

Open the ~/.bashrc file using nano:
```shell
nano ~/.bashrc
```
Add export PATH="/home/user/.local/bin:$PATH" to your shell configuration file.
```shell
. . .
export PATH="/home/user/.local/bin:$PATH"
```
Next, apply the changes:
```shell
source ~/.bashrc
```

Check your installation:
```python
poetry --version
```

## Run the project
Run the following command (in the /services/ directory):
```python
poetry run python3 manage.py runserver
```
In case of error with Poetry, run the command:
```python
poetry update package
```

## Home-made commands
To clear the User database, the following command can be used:
```python
poetry run python3 manage.py clear_database_user
```


