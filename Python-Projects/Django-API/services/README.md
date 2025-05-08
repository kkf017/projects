# Example of Django app

This app is an example of Django app (back-end) to manage Energy resources.

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
To fill the database, the following command can be used:
```python
poetry run python3 manage.py import_energy_data [filepath]
``` 

To clear the database, the following command can be used:
```python
poetry run python3 manage.py clear_data
``` 


## Examples of Requests

### Request GET

##### Display all Energy Resources
To display all Energy Ressources (in database), it is possible to go to http://127.0.0.1:8000/energy/ in your web browser, or use the following command in a terminal (Linux):
```sh
curl -X GET -H "Accept: application/json" http://127.0.0.1:8000/energy/
``` 
This command will return a json format with all the Energy Resources available in database.

##### Search request for Energy Resources
It is also possible to select Energy Resources, according to the following parameters:
- type: solar, wind, hydro, nuclear ...etc
- status: active, inactive, maintenance
- location: location of a ressource
- min, max: min and max value for capacity

These parameters can be combined in the url, as follows:
```sh
# Example of URL to select all the 'solar' ressources
curl -X GET -H "Accept: application/json" http://127.0.0.1:8000/energy/search?type=solar
``` 
```sh
# Example of URL to select all the 'solar' and 'active' ressources
curl -X GET -H "Accept: application/json" http://127.0.0.1:8000/energy/search?type=solar&status=active
```
```sh
# Example of URL to select all the ressources wiht capacity between 150 and 300
curl -X GET -H "Accept: application/json" http://127.0.0.1:8000/energy/search?min=150&max=300
```
```sh
# Example of URL to select all the 'active' ressources wiht capacity between 150 and 300
curl -X GET -H "Accept: application/json" http://127.0.0.1:8000/energy/search?status=active&min=150&max=300
```
It is also possible to go to the url with your web browser.

### Request POST
A new Energy ressource can be created with the following request:
```sh
# Example of URL to create a ressource called "Biomass place 1"
curl -X POST -H "Content-Type: application/json" -d '{"name": "Biomass place 1", "type": "biomass", "capacity": "175", "location": "Location I", "status": "active"}' http://127.0.0.1:8000/new/
``` 
Or it is also possible to go to http://127.0.0.1:8000/new/ in your web browser and use the interface.


### Request DELETE
Finally, an Energy ressource can be deleted (using its id in table - eid) with the command:
```sh
# Example of URL to delete ressource with eid 4c7a2745227fd92f5381d4dfce69468e5df1c348
curl -X DELETE http://127.0.0.1:8000/close?eid=4c7a2745227fd92f5381d4dfce69468e5df1c348
```



## Manage errors

In case of error, install Django:
```python
pip3 install Django
```

Install rest_framework:
```python
pip3 install djangorestframework
pip3 install markdown       
pip3 install django-filter 
```

Run the project with classical Django commands:
```python
python3 manage.py runserver
```


