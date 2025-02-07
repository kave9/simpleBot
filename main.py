import asyncio
import telegram
import os
from dotenv import load_dotenv

load_dotenv()



TOKEN = os.getenv('TOKEN')

async def main():
    bot = telegram.Bot(TOKEN)
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())