FROM ubuntu:22.04

LABEL company="KPM_Ritm"
LABEL QA="Kana"

WORKDIR /test

# Копируем проект в рабочую директорию Docker
COPY . .

USER root

# Подготавливаем систему и устанвливаем нужные пакеты
RUN sh/setup_system.sh

# Устанавливаем необходимые для проекта python зависимости
RUN cd requirements && pip install -r requirements.txt

# Запускаем тесты и генирируем результат allure
CMD sh/start_tests.sh
