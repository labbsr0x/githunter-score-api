# GitHunter-Score-Api
The purpose of this tool is to collect * WS data related to repositories hosted on GitHub, Gitlab and other providers, perform a calculation using the users' open source activities and provision the value obtained through API.

## Install
After clone repository, write this command in terminal:
```bash
pip3 install -r requirements.txt
``` 

## Configuration
To run the application in a local environment, all configurations are retrieved from the **.local.env** file (when there is no data in SCORE_ENVIRONMENT). 

But it is also possible to load the data directly from the environment variables:

```bash
// the environment that is being executed, ex: DEV, PROD
SCORE_ENVIRONMENT= 

// uri of the connection to the bank, ex: mongodb://u:p@host:27017/db?authSource=dbauth
DB_MONGO_URI=

// url of Gihunter-Bind-Agrows, ex: http://githunter-bind-starws.labbs.com.br/metrics
BIND_URL=

// log level, eg INFO, WARN, ERROR
APP_LOG_LEVEL=

// port the application will listen on
APP_PORT=
```

## Scheduler

An example of running the application without creating a schedule (run at the moment):
```
curl -X POST "http://host:port/schedule/" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"provider\": \"gitfeed\", \"node\": \"userStatsV3\", \"interval_type\": \"hourly\", \"interval_value\": 0}"
```
Parameters:

1. **interval_type:** can be __hourly__ or __monthly__
2. **interval_value:** the related interval __interval_type__, eg: if you enter type: monthly and value: 1, will run 1x per month.


## Run
First, make sure your python version is v3 or higher if not, upgrade to a newer version.

```bash
python3 -m githunter.app
```

## Docker
The project can be carried out using the docker. If you already have Docker and Docker Compose installed, run:

```bash
docker-compose up --build
```


## Api Docs
API documentation is generated automatically and made available via Swagger. If the application is running in the local environment, you can check the documentation at:

```bash
http://localhost:3000
```

## License
[MIT](https://choosealicense.com/licenses/mit/)