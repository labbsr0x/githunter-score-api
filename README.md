# GitHunter-Score-Api
The purpose of this tool is to collect * WS data related to repositories hosted on GitHub, Gitlab and other providers, perform a calculation using the users' open source activities and provision the value obtained through API.

## Install
After clone repository, write this command in terminal:
```bash
pip3 install -r requirements.txt
``` 

## Run
**First, make sure your python version is v3 or higher if not, upgrade to a newer version.**

```bash
python3 -m githunter.app
```

## Api Docs
**API documentation is generated automatically and made available via Swagger. If the application is running in the local environment, you can check the documentation at:**

```bash
http://localhost:3000
```

//TODO:
* pegar config das variáveis de ambiente
* dockerizar
* explicar o funcionamento do scheduler
* explicar o local das configuracoes locais
* explicar as variáveis de ambiente
* na verdade, o score tem que ter um atributo: schedule, contendo todas as informacoes
* explicar como usar via docker

## License
[MIT](https://choosealicense.com/licenses/mit/)