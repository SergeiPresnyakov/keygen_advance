# генерирует указанное количество паролей
# указанной длины
import random


uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowers = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
punctuation = '!#$%&*+-=?@^_'
hard_to_recognize_symbols = 'il1Lo0O'

generation_params = {
    'количество паролей': 0,
    'длина пароля': 0,
    'включать цифры': {'flag': True, 'symbols': digits},
    'включать прописные буквы': {'flag': True, 'symbols': uppers},
    'включать строчные буквы': {'flag': True, 'symbols': lowers},
    'включать символы пунктуации': {'flag': True, 'symbols': punctuation},
    'исключить неоднозначные символы': {'flag': False, 'symbols': hard_to_recognize_symbols},
}


def input_generation_params() -> None:
    """Ввод параметров генерации паролей"""
    for key in generation_params:
        print(key, end=': ')
        if key in ('количество паролей', 'длина пароля'):
            generation_params[key] = int(input())
        else:
            generation_params[key]['flag'] = False if input() == '0' else True


def char_assemble() -> str:
    """Сборка всех символов для пароля в одну строку"""
    chars = []
    for key in generation_params:
        if key not in ('количество паролей', 'длина пароля', 'исключить неоднозначные символы'):
            chars.extend(i for i in generation_params[key]['symbols'] if generation_params[key]['flag'])

    if generation_params['исключить неоднозначные символы']['flag']:
        for i in hard_to_recognize_symbols:
            while i in chars:
                chars.remove(i)

    return ''.join(chars)


def generate_passwords(chars: str) -> None:
    """Генерирует пароли, используя символы из chars"""
    for _ in range(generation_params['количество паролей']):
        for _ in range(generation_params['длина пароля']):
            print(random.choice(chars), end='')
        print()


def main():
    input_generation_params()
    chars = char_assemble()
    generate_passwords(chars)


if __name__ == '__main__':
    main()