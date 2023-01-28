from dotenv import load_dotenv
import os
import warnings

from bot import Bot

# warnings.filterwarnings(
#     "ignore",
#     message="The localize method is no longer necessary, as this time zone supports the fold attribute",
# )

load_dotenv()
TOKEN = os.getenv("TOKEN")
MyBot = Bot(TOKEN)

if __name__ == "__main__":
    MyBot.run()
