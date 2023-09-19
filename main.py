import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from button import registr1, send_contact

DataBase = {
    'User_Id':[],
}

# Set up logging
logging.basicConfig(level=logging.INFO)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from BotFather
API_TOKEN = '6638931167:AAFnSiAjw5Q9UbH0uzdBxBL3BWyBgQHeHSU'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

class RegistrState(StatesGroup):
    name = State()
    age = State()
    numb = State()
    mail = State()

@dp.message_handler(commands='start')
async def starter(message: types.Message):
    await message.answer(message.from_user.id)
    await message.answer(f'''
<b>Assalom Alaykum, {message.from_user.first_name}!</b>
Bizning botimizga hush kelibsiz!
''', reply_markup=registr1)
    
@dp.message_handler(text="Ro`yxatdan O`tish!")
async def ish_joyI(message: types.Message, state=FSMContext):
    await message.answer('''
<b>Ro'yxatdan o'tish uchun ariza berish</b>

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
''')
    await message.answer('<b>Ism Familyangizni kiriting !</b>')
    await RegistrState.name.set()

@dp.message_handler(state=RegistrState.name, content_types=types.ContentType.TEXT)
async def naming_writer(message: types.Message, state=FSMContext):
    ismi = message.text
    DataBase[str(message.from_user.id)] = [ismi]
    await message.answer(f'''
<b>👦Yoshingizni kiriting! \nMasalan: 19 yosh.</b>
''')
    await state.finish()
    await RegistrState.numb.set()

@dp.message_handler(state=RegistrState.numb, content_types=types.ContentType.TEXT)
async def numb_writer(message: types.Message, state=FSMContext):
    numb_user = message.text
    wha = DataBase.get(str(message.from_user.id))
    wha.append(numb_user)
    await message.answer('''
📞Aloqa: 

Bog`lanish uchun raqamingizni kiriting.
Masalan, +998 90 123 45 67
''', reply_markup=send_contact)
    await state.finish()
    await RegistrState.mail.set()

@dp.message_handler(state=RegistrState.mail, content_types=types.ContentType.TEXT)
async def mail_write(message: types.Message, state = FSMContext):
    mail_user = message.text
    await message.answer('''
📧Po`chta
                         
O`zingizni elektron pochtadagi adresingizni yuboring. 
Masalan: elektron_pochta@gmail.com
''')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)