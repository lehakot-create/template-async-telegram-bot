FROM python

WORKDIR /my bot

COPY . .
RUN pip install -r requirements.txt

CMD ["python", "bot.py"]

#docker build -t bot .
#docker run --rm -d -v D:\Python project\Async TelegramBot\my bot:/my bot/  bot