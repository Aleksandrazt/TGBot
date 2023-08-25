from collections import namedtuple

Problem = namedtuple('Problem', 'user_means bot_solve')
Photo_answer = namedtuple('Photo_answer', 'text photos')
Doc_answer = namedtuple('Doc_answer', 'text doc name')

PROBLEMS = {
    "Привязать маршрут ВЕРТИКАЛЬ": Photo_answer('Смотри документ Word Привязать маршрут в папке '
                                                'Лоцман 2018.3 ОШИБКИ\n1. Что должно входить в ТПП. '
                                                '\n2. Проверить можно встав на ДСЕ, компоновку АРМ технолога '
                                                '\nВстать на маршрут – связь «по маршруту», встать на элемент '
                                                'маршрута – связь «по элементу маршрута» в каждой выбранной '
                                                'связи должен отображаться привязываемый ТП',
                                                ['photos_and_docs_for_answer/17_1.png',
                                                 'photos_and_docs_for_answer/17_2.png']),
    "Создать версию СТО (ЦАКТД)": "Поступила заявка от ЦАКТД Прошу создать 2 версию оснастки К7800-4034."
                                  "К7317-4007 создана зачем-то вторая версия, а первая аннулирована."
                                  "1-Необходимо запустить БП по созданию новой версии СТО, после чего "
                                  "ЦАКТД приложит обновленную КД."
                                  "\n2-Захару Потапову Написать, чтобы БП запустил",
    "Промежуточные листы в ТП ": "ак и должно быть, вы добавили в ТП дополнительную информацию, она не влезла "
                                 "на предыдущий лист, а так как менять нумерацию листов ТП нельзя, то "
                                 "создается новый лист со строчной буквой(ГОСТ 2.503-2013 п.п. 5.5 и 5.6), "
                                 "как у вас и получилось, просто в прошлые разы видимо на листах оставалось "
                                 "место для записи изменений и этого не происходило.",
    "Не появился файл Акта внедрения": Photo_answer('Смотри картинку', ['photos_and_docs_for_answer/23_1.png']),
    "Не возвращается ТП из Вертикали": Photo_answer('Открепилась лицензия. Необходимо "Отказаться"'
                                                    '. Если впервые разрабатываемый ТП, а не ТИИ, '
                                                    'то еще можно сохранить локально, затем '
                                                    'добавить файл и переименовать его согласно '
                                                    'буквенных обозначений: SBR, MEX и т.д. Ошибка'
                                                    ' прокси-это ошибка ЧПУ, так должно быть. ',
                                                    ['photos_and_docs_for_answer/24_1.png']),
    "Не вернулся ТП из Вертикали": 'Архив ТП\nЕсли файл "Архив ТП" не в состоянии '
                                   'проектирования, а по БП выполняется работа '
                                   '(редактирование), значит технолог сначала стал '
                                   'редактировать, а потом принял задание в работу. Необходимо'
                                   ': запустить на ТП БП "Администрирование"-"Смена состояний '
                                   'ТП"-"версии документа ТП" - "Создание версии ТП '
                                   'при ошибке".',
    "Обновление информации в требовании безопасности": Doc_answer('Смотри в документе',
                                                                  'photos_and_docs_for_answer/26_1.txt',
                                                                  'REG.000125 - Правила отражения и оформления '
                                                                  'требований безопасности труда в '
                                                                  'технологической документации.pdf'),
    "Папка не возвращается из работы": Photo_answer('Сбой в системе, Ване писать',
                                                    ['photos_and_docs_for_answer/27_1.png']),
    "Не запускается БП на согласование ТП": 'Добрый день! Вам необходимо взять Ваш ТП в работу через вертикаль'
                                            ', убрать фамилию ГС, нажать "сохранить ТП", после этих действий '
                                            'притянется должность ГС и тогда Вы сможете вписать фамилию '
                                            'обратно и вернуть ТП в лоцман. После этих действий в лоцман '
                                            'просто перезапустите Ваш БП.',
    "Прошу предоставить доступ для редактирования ТП": 'Нужно создать новую версию на основании протатипа. '
                                                       'Памятка "Редактирование ТП, созданного другим '
                                                       'пользователем" (папка на рабочем столе инструкции ТИИ)…'
                                                       'Только так, просто в Лоцман создать на основе протатипа'
                                                       ' нельзя, потому что раскрывать нужно все дерево и много'
                                                       ' операций выделять.  ',
    'Вторичное представление не соответствует содержанию файла ТП': Photo_answer('при локальном сохранении '
                                                                                 'файла, обозначение будет как '
                                                                                 'обозначение ДСЕ',
                                                                                 ['photos_and_docs_for_answer/'
                                                                                  '30_1.png',
                                                                                  'photos_and_docs_for_answer/'
                                                                                  '30_2.png']),
    'Выдать права для создания ТИИ': Photo_answer('Открыть Лоцман Конфигуратор, найти ФИО, Нажать правой '
                                                  'кнопкой мыши "Добавить" в графе должности. Посмотреть к '
                                                  'какому цеху относится. Выбрать "технолог бюро….280 цеха". '
                                                  'Далее, необходимо открыть редактирование (карандаш) и в '
                                                  'свойствах пользователя (служебные) добавить ПТЗ ТЕХНОЛОГ. '
                                                  'После этого сохранить и пользователю нужно перезапустить '
                                                  'Лоцман. ',
                                                  ['photos_and_docs_for_answer/31_1.png',
                                                   'photos_and_docs_for_answer/31_2.png',
                                                   'photos_and_docs_for_answer/31_3.png']),
    'Добавить фотографию профиля в outlook': Photo_answer('Смотри фото',
                                                          ['photos_and_docs_for_answer/32_1.png']),
    'НЕ открывается ЛОЦМАН и ВЕРТИКАЛЬ после перезагрузки ПК': 'Инструкция: \nПерезапустите компьютер, '
                                                               'НЕ открывайте лоцман и вертикаль, запустите '
                                                               'скрипт \\\\vm-asconapp\\ascon\\script'
                                                               '\\usersetting.cmd и перезагрузите пк, ещё раз.',
    'Просят обновить привязку или перепривязать ТП к техсборке': Photo_answer('Необходимо найти ТП по '
                                                                              'обозначению, перейти на ТП, '
                                                                              'посмотреть по какому ТИИ '
                                                                              'появляется новая версия ТП, '
                                                                              'перейти на ТИИ, если ТП был '
                                                                              'создан на ТС (технологическая '
                                                                              'сборка), тогда необходимо '
                                                                              'сравнить ТС из прошлой версии и '
                                                                              'ТС из актуальной, если отличаю'
                                                                              'тся, тогда взять в работу ТИИ, '
                                                                              'вырезать ТС из новой версии, а '
                                                                              'из прошлой версии ТП скопировать'
                                                                              ' ТС, маршрут и элемент маршрута '
                                                                              'чтобы выглядело как на рисунке.',
                                                                              ['photos_and_docs_for_answer'
                                                                               '/38_1.png']),
}

PHOTO_PROBLEMS = {
    (0, 0): ('Не удалось подключиться к базе данных "ptz_mockup". "17:[DBNETLIB](ConnectionOpen (Connect0).]SQL '
             'Server не существует, или доступ запрещен". Если ошибка будет повторяться, обратитесь к '
             'администратору.', 'Необходимо обновление Лоцман до версии 18.3'),

    (0, 1): ('Действие прервано обработчиком события после создания объекта в результате ошибки 100000:400004:'
             'Недостаточно прав для объекта [СТО K7347-4011 1] System.Runtime.InteropServices.COMException',
             'В ФАЙЛЕ НЕТ РЕШЕНИЯ'),

    (0, 2): ('Значение не может быть неопределенным. Имя параметра: source', 'В ФАЙЛЕ НЕТ РЕШЕНИЯ'),

    (0, 3): ('В процессе выполнения программы произошла ошибка. Сообщение об ошибке: Прослушивание на '
             'net.pipe://localhost/AppServerNativehost не выполняла ни одна конечная точка, которая могла бы принять '
             'сообщение. Среди прочих причин это могло быть вызвано неправильным адресом или действием SOAP. '
             'Подробнее см. в описании InnerException (если имеется) Вы можете сохранить отчет о проблеме и отправить '
             'его в службу технической поддержки компании АСКОН. Обязательно опишите порядок действий, приводящих к '
             'ошибке. Регистрация отчета о проблеме Просмотр данных, содержащихся в отчете При возникновении проблем '
             'с регистрацией запроса обратитесь в Центральную Службу технической поддержки ACKOH no e-mail: '
             'support@ascon.ru', 'Перезагрузить лоцман'),

    (0, 4): ('Ошибка работы прокси: [Значение не может быть неопределенным.]',
             '"прошу описать последовательность действий после которых произошла ошибка, для её воспроизведения и '
             'последующего устранения. Так же прошу попробовать воспроизвести у себя аналогичную последовательность '
             'действий и сообщить повторилась ли данная ошибка."'),

    (0, 5): ('Не удалось подключиться к серверу приложений: "ascon: He удалось подключиться к '
             'net.tcp://172.20.10.81:8076/SecurityModeTransport. Попытки подключения выполнялись в течение интервала '
             'времени 00:00:01.0084879. Код ошибки ТСР 10061: Подключение не установлено, т.к. конечный компьютер '
             'отверг запрос на подключение 172.20.10.81:8076"',
             'Необходима перезагрузка ПК, не установились настройки политики AD'),

    (0, 6): ('Сетевой диск W: не существует или не ассоциирован с ресурсом \\\\vm-asconapp\\Ascondatalptz_mockup'
             '\\Files\\SPTZ#BALABONO VRA#Files. Подключить сетевой ресурс \\\\vm-asconapp\\Ascondatalptz_mockup'
             '\\Files\\SPTZ#BALABONO VRA#Files как W:? В случае отказа, работа с изменяемыми объектами будет '
             'невозможна.', 'Не подключен диск W \n1.Перезагрузка ПК \n2.Запуск скрипта \\\\vm-asconapp\\ascon'
                            '\\usersetting.cmd '),

    (0, 7): ('ОЧЕНЬ НЕРАЗБОРИВЫЙ СКРИН', 'Перезагрузить ПК, если не поможет, проверить доступен ли путь '
                                         '\\\\vm-asconapp\\COD\\Settings\\LoodsmanVRTPlugin\\'),

    (0, 8): ('Ошибка подключения рабочего диска W: System Error. Code: 1202. Локальное имя устройства уже используется'
             ' для подключения к другому сетевому ресурсу', 'Не подключен диск W \n1.Перезагрузка ПК  '
                                                            '\n2.Запуск скрипта \\\\vm-asconapp\\ascon'
                                                            '\\usersetting.cmd '),

    (0, 9): ('К сожалению, файл не найден. Может, он был перемещен, переименован или удален? '
             '("W:\\TИИ-00064.22 1.docx")', 'Не подключен диск W \n1.Перезагрузка ПК \n2.Запуск скрипта '
                                            '\\\\vm-asconapp\\ascon\\usersetting.cmd '),

    (0, 10): ('Не удалось открыть файл \\\\vm-asconapp\\Ascondata\\ptz_mockup\\CheckOuts\\SPTZ#grin valdrk\\Temp'
              '\\735M-37.98.070-2CБ_37-0090.4.6-22ПИ.PDF', 'Не подключен диск W \n1.Перезагрузка ПК \n2.Запуск скрипта'
                                                           ' \\\\vm-asconapp\\ascon\\usersetting.cmd Если не помогло, '
                                                           'обращаться к Ивану для выдачи прав.'),

    (0, 11): ('Не удалось подключиться к серверу приложений: "ascon: Отказано в доступе"',
              'Необходимо обновление Лоцман до версии 18.3'),

    (0, 12): ('Ошибка создания объекта техпроцесса в ЛОЦМАН:PLM: Действие прервано обработчиком события '
              'после создания объекта в результате ошибки 100000:400004:Недостаточно прав для объекта '
              '[94326-88.01.1.000783 1].', 'В ФАЙЛЕ НЕТ РЕШЕНИЯ')
}

REAL_PHOTO_PROBLEM = {
    'Не удалось подключиться к базе данных "ptz_mockup". "17:[DBNETLIB](ConnectionOpen (Connect0).]SQL Server не '
    'существует, или доступ запрещен". Если ошибка будет повторяться, обратитесь к администратору.':
        'Необходимо обновление Лоцман до версии 18.3',

    'Не удалось подключиться к серверу приложений: "ascon: He удалось подключиться к '
    'net.tcp://172.20.10.81:8076/SecurityModeTransport. Попытки подключения выполнялись в течение интервала времени '
    '00:00:01.0084879. Код ошибки ТСР 10061: Подключение не установлено, т.к. конечный компьютер отверг запрос на '
    'подключение 172.20.10.81:8076"':
        'Необходима перезагрузка ПК, не установились настройки политики AD',

    'Сетевой диск W: не существует или не ассоциирован с ресурсом '
    '\\\\vm-asconapp\\Ascondatalptz_mockup\\Files\\SPTZ#BALABONO VRA#Files. Подключить сетевой ресурс '
    '\\\\vm-asconapp\\Ascondatalptz_mockup\\Files\\SPTZ#BALABONO VRA#Files как W:? В случае отказа, работа с '
    'изменяемыми объектами будет невозможна.':
        'Не подключен диск W \n1.Перезагрузка ПК \n2.Запуск скрипта \\\\vm-asconapp\\ascon\\usersetting.cmd ',

    'ОЧЕНЬ НЕРАЗБОРИВЫЙ СКРИН':
        'Перезагрузить ПК, если не поможет, '
        'проверить доступен ли путь \\\\vm-asconapp\\COD\\Settings\\LoodsmanVRTPlugin\\',

    'Ошибка подключения рабочего диска W: System Error. Code: 1202. Локальное имя устройства уже используется для '
    'подключения к другому сетевому ресурсу': 'Не подключен диск W \n1.Перезагрузка ПК '
                                              '\n2.Запуск скрипта \\\\vm-asconapp'
                                              '\\ascon\\usersetting.cmd ',

    'К сожалению, файл не найден. Может, он был перемещен, переименован или удален? ("W:\\TИИ-00064.22 1.docx")':
        'Не подключен диск W \n1.Перезагрузка ПК \n2.Запуск скрипта \\\\vm-asconapp\\ascon\\usersetting.cmd ',

    'Не удалось открыть файл \\\\vm-asconapp\\Ascondata\\ptz_mockup\\CheckOuts\\SPTZ#grin valdrk\\Temp\\735M-37.98.070'
    '-2CБ_37-0090.4.6-22ПИ.PDF':
        'Не подключен диск W \n1.Перезагрузка ПК '
        '\n2.Запуск скрипта \\\\vm-asconapp\\ascon\\usersetting.cmd '
        'Если не помогло, обращаться к Ивану для выдачи прав.',

    'Не удалось подключиться к серверу приложений: "ascon: Отказано в доступе"':
        'Необходимо обновление Лоцман до версии 18.3',

    'Ошибка создания объекта техпроцесса в ЛОЦМАН:PLM: Действие прервано обработчиком события после создания объекта '
    'в результате ошибки 100000:400004:Недостаточно прав для объекта [94326-88.01.1.000783 1].':
        'В ФАЙЛЕ НЕТ РЕШЕНИЯ',

    'Действие прервано обработчиком события после создания объекта в результате ошибки 100000:400004:Недостаточно '
    'прав для объекта [СТО K7347-4011 1] System.Runtime.InteropServices.COMException':
        'В ФАЙЛЕ НЕТ РЕШЕНИЯ',

    'Значение не может быть неопределенным. Имя параметра: source': 'В ФАЙЛЕ НЕТ РЕШЕНИЯ',

    'В процессе выполнения программы произошла ошибка. Сообщение об ошибке: Прослушивание на '
    'net.pipe://localhost/AppServerNativehost не выполняла ни одна конечная точка, которая могла бы принять сообщение. '
    'Среди прочих причин это могло быть вызвано неправильным адресом или действием SOAP. Подробнее см. в описании '
    'InnerException (если имеется) Вы можете сохранить отчет о проблеме и отправить его в службу технической '
    'поддержки компании АСКОН. Обязательно опишите порядок действий, приводящих к ошибке. Регистрация отчета о '
    'проблеме Просмотр данных, содержащихся в отчете При возникновении проблем с регистрацией запроса обратитесь в '
    'Центральную Службу технической поддержки ACKOH no e-mail: support@ascon.ru':
        'Перезагрузить лоцман',

    'Ошибка работы прокси: [Значение не может быть неопределенным.]':
        '"прошу описать последовательность действий после которых '
        'произошла ошибка, для её воспроизведения и последующего устранения. '
        'Так же прошу попробовать воспроизвести у себя аналогичную последовательность действий и '
        'сообщить повторилась ли данная ошибка."'

}
