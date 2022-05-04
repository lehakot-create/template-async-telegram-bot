Шаблон асинхронного телеграм бота


Как запустить:
1. клонируем репозиторий gitclone https://github.com/lehakot-create/template-async-telegram-bot.git
2. создаем в корневой папке файле .env и кладем туда API_TOKEN="ваш токен"
3. устанавливаем зависимости pip install -r requirements.txt
4. запускаем python bot.py


Запустить в контейнере
docker build -t bot .

docker run --rm -d bot


docker run --rm -d -v pwd:/my_bot/ bot