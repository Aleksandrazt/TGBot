import telebot
from pyjokes import get_joke
from keras.models import load_model

import error_handler
import problems_lib
from image_recognition import find_class
from problems_lib import Photo_answer

if __name__ == '__main__':
    pattern = load_model("C:\\Users\\stsar\\PycharmProjects\\TGBot\\first_model_weights_test_my")
    pattern.load_weights("C:\\Users\\stsar\\PycharmProjects\\TGBot\\first_model_weights_test.h5")
    my_bot = telebot.TeleBot("SECRET")


    @my_bot.message_handler(commands=['start'])
    def start(message):
        """
        If message is the command start it begins the dialog
        :param message: user message
        :return:
        """
        my_bot.send_message(message.from_user.id, 'Добрый день! Опишите Вашу проблему.')


    @my_bot.message_handler(commands=['joke'])
    def write_joke(message):
        """
        If message is the command joke it sends a joke
        :param message: user message
        :return:
        """
        my_bot.send_message(message.from_user.id, get_joke())


    @my_bot.message_handler(content_types=['text'])
    def text_handle(message):
        """
        If message is text it sends it to analyze and print possible solution
        :param message: user message
        :return:
        """
        solutions = error_handler.analyze_text_message(message.text,
                                                       problems_lib.PROBLEMS | problems_lib.REAL_PHOTO_PROBLEM)
        if solutions:
            for solution in solutions:
                print()
                if type(solution[1]) is str:
                    my_bot.send_message(message.from_user.id, f'Вы имели в виду?:\n{solution[0]}')
                    my_bot.send_message(message.from_user.id, f'Решение:\n{solution[1]}')
                elif isinstance(solution[1], Photo_answer):
                    my_bot.send_message(message.from_user.id, f'Вы имели в виду?:\n{solution[0]}')
                    my_bot.send_message(message.from_user.id, f'Решение:\n{solution[1].text}')
                    for path in solution[1].photos:
                        photo = open(path, 'rb')
                        my_bot.send_photo(message.from_user.id, photo)
                else:
                    my_bot.send_message(message.from_user.id, f'Вы имели в виду?:\n{solution[0]}')
                    my_bot.send_message(message.from_user.id, f'Решение:\n{solution[1].text}')
                    with open(solution[1].doc, 'rb') as file:
                        f = file.read()
                    my_bot.send_document(message.from_user.id, f, solution[1].name)
            my_bot.send_message(message.from_user.id, f'\nЕсли Ваша проблема есть среди перечисленные выше'
                                                      f'\nЕсли Вашей проблемы нет - свяжитесь с ...')
        else:
            my_bot.send_message(message.from_user.id,
                                'Проверьте корректность написанного или поставьте вопрос четче.'
                                'Попробуйте перезапустить/перезагрузить. Если после не зраработает обратитесь к ...')


    @my_bot.message_handler(content_types=['photo'])
    def image_handler(message):
        """
        If message is a photo it sends it to pre-learned nn to classify the mistake
        :param message: user message
        :return:
        """
        photo_id = message.photo[-1].file_id
        photo_file = my_bot.get_file(photo_id)
        photo_bytes = my_bot.download_file(photo_file.file_path)
        error_class = find_class(photo_bytes, pattern)
        error, problem = problems_lib.PHOTO_PROBLEMS[error_class]
        my_bot.send_message(message.from_user.id, f'Вы имели в виду?:\n{error}')
        my_bot.send_message(message.from_user.id, f'Решение:{problem}')
        my_bot.send_message(message.from_user.id, f'Если Вашей проблемы нет Выше либо пришлите более '
                                                  f'четкую фотографию, либо скопируйте текст ошибки и пришлите его')


    @my_bot.message_handler(content_types=['document', 'sticker', 'audio', 'voice', 'video', 'location', 'contact'])
    def incorrect_format(message):
        """
        If message is an unsupported format it requests send text or photo
        :param message: user message
        :return:
        """
        my_bot.send_message(message.from_user.id, 'Отправьте вопрос текстом или скриншот ошибки')


    my_bot.polling(none_stop=True, interval=0)
