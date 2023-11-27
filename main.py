import time
import logging

from aiogram import Bot, Dispatcher, executor, types

token = "5866268119:AAF7dgvd4Qdh6_J2GhxfnAp-u6WcBS8jjYQ"
msg = "Программировал ли ты сегодня, {}?"

bot = Bot(token=token)
dp = Dispatcher(bot = bot)


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.INFO(f'{user_id=} {user_full_name=}, {time.asctime()}')

    await message.reply(f"Привет, {user_full_name}!")

    for i in range(10):
        time.sleep(2)
        await bot.send_message(user_id, msg.format())

if __name__ == '__main__':
    executor.start_polling(dp)