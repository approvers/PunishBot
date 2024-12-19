from config import PunishBotConfig
from src.main import PunishBot


def main():
    # noinspection PyArgumentList
    config = PunishBotConfig()
    bot = PunishBot(config)

    bot.launch()


if __name__ == "__main__":
    main()
