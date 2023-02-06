class Bot:
    def init(self, name):
        self.name = name

    def say_name (self):
        print(self.name)

    def send_message (self, message):
        print(message)

class TelegramBot(Bot):

    def set_url(self, url = None):
        self.url = url

    def set_chat_id(self, chat_id = None):
        self.chat_id = chat_id

    def send_message(self, message = None):
        try:
            b= self.url
        except:
            self.set_url()

        try:
            a = self.chat_id
        except:
            self.set_chat_id()

        print(f'{message} today {self.url} and {self.chat_id}')


b = TelegramBot("Clinic")
b.say_name()
b.send_message("Symptoms")
b.send_message()


telegram_bot = TelegramBot("TG")
telegram_bot.say_name()
telegram_bot.send_message('Hello')
telegram_bot.set_chat_id(1)
telegram_bot.send_message('Hello')