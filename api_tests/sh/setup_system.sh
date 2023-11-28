#!/bin/bash

# Обновляем пакеты системы
apt-get update

# Устанавливаем java зависимости для запуска allure
yes | apt-get install openjdk-8-jdk

cd temp

# Устанавливаем allure из установочного файла
yes | dpkg -i allure_2.24.1-1_all.deb

# Устанавливаем pip
yes | apt install python3-pip

# Очищаем временные файлы
cd .. && rm -R temp
