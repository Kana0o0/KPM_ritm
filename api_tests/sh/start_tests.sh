#!/bin/bash

# Генерируем allure_result в корне проекта
pytest -s -v src/main.py --alluredir=allure_result

# Запускаем allure server на порту 7777, если порт занят используйте другой
allure serve allure_result -p 7777
