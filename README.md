# Anonim REST Quiz
Анонимный **REST API** опросник на **Django**

## Установка и настройка
Для разработки я использовал **python3** версии **3.8.10**, поэтому во избежание каких-либо проблем, советую вам использовать именно эту версию.

Установим зависимости командой: 
```bash
pip3 install requirements.txt
``` 

Для выполнения миграций, перейдите в корневую папку проекта и пропишите: 

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Если все миграции накатились без ошибок, то двигаемся дальше, и нам надо создать суперпользователя (поля **username** и **password** обязательные, *email* можно пропустить):

```bash
python3 manage.py createsuperuser
```

Если все создалось без ошибок, то можно уже запускать сервер. Запустим его командой:

```bash
python3 manage.py runserver
```

Если вы сделали все правильно, то вы увидите примерно такой текст
```
Django version 2.2.10, using settings 'restapi.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Теперь вы можете перейти в админ панель в вашем браузере и добавить там нужные вам опросы и вопросы к ним. Чтобы зайти в админку, вставьте в браузер следующий адрес: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) 

Введя пароль, вы увидите две колонки сверху (их вы можете оставить, они нам не понадобятся) и три колонки снизу (**Quizs, Questions, Answers**). Чтобы добавить опрос - нажмите на кнопку "**Add**" напротив колонки **Quizs**, укажите название опроса, дату завершения и описание. После того как вы все ввели нажмите на кнопку "**SAVE**" и теперь можем перейти к добавлению вопросов.

Чтобы добавить вопросы вернитесь на предыдущую страницу с тремя колонками снизу и нажмите на "**Add**" напротив **Questions**. Теперь укажите айди опроса (айди отсчитывается по порядку от 1. Но если вы хотите посмотреть полный список своих опросов и айди к ним, промотайте инструкцию чуть ниже и посмотрите раздел, где описывается API и взаимодействие с ним). 

Укажите текст вопроса и тип вопроса (**1** - ответ текстом, **2** - ответ с выбором одного варианта, **3** - ответ с выбором нескольких вариантов). Нажмите на "**SAVE**" или "**Save and add another**", если вы хотите продолжить добавление новых вопросов.

## REST API
> **Получить все опросы**
>> **URL**: */quizes/*
>>
>> **Method**: *GET*
>>
>> **Required**: *-* 
>> 
> **Получить все вопросы в одном опросе**
>> **URL**: */questions/*
>>
>> **Method**: *GET*
>>
>> **Required**: *quiz_id* 
>> 
> **Получить все ответы пользователя**
>> **URL**: */get_answers/*
>>
>> **Method**: *GET*
>>
>> **Required**: *user_id, quiz_id* 
>> 
> **Отправить ответ**
>> **URL**: */send_answer/*
>>
>> **Method**: *POST*
>>
>> **Required**: *user_id, question_id, text* 

## Зависимости
- **django v2.2.10**
- **djangorestframework v3.12.4**

## Автор
**Blazzerrr**

Связь со мной через Telegram
[@blazzzerrr](https://t.me/blazzzerrr) 