import pyperclip
import secrets
from random import sample
from string import  ascii_lowercase, ascii_uppercase, digits, punctuation


class PasswordError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class PasswordLengthError(PasswordError):
    pass


class PasswordCharacterError(PasswordError):
    pass


def make_password(*, length: int = 16, delete: str = '') -> str:
    if length < 8:
        raise PasswordLengthError('')


    def get_char(seq: str) -> str:
        return secrets.choice(seq)


    def remove_spaces(seq: str) -> str:
        return seq.replace(' ', '')


    def remove_chars(seq: str) -> list[str]:
        chars = f'{digits} {punctuation} {ascii_lowercase} {ascii_uppercase}'
        return ''.join(c for c in chars if c not in remove_spaces(seq)).split()


    chars: list[str] = remove_chars(delete)

    if len(chars) < 4:
        raise PasswordCharacterError('')

    password: list[str] = []

    count = 0

    for _ in range(length):
        if count < 4:
            password.append(get_char(chars[count]))
            count += 1
        else:
            password.append(
                get_char(
                    chars[secrets.randbelow(len(chars))]
                )
            )

    return ''.join(sample(password, k=len(password)))


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        prog='mkp',
        description='Strong password generator',
    )

    parser.add_argument(
        '-l',
        '--length',
        type=int,
        metavar='int',
        default=16,
        help='password length (default 16)',
    )

    parser.add_argument(
        '-d',
        '--delete',
        type=str,
        metavar='str',
        default='',
        help='characters that should not be included in the password',
    )

    parser.add_argument(
        '-c',
        '--copy',
        action='store_true',
        help='copy to clipboard',
    )

    parser.add_argument(
        '-s',
        '--silence',
        action='store_true',
        help='Does not print password in console'
    )

    args = parser.parse_args()

    try:
        password = make_password(length=args.length, delete=args.delete)
        if args.copy:
            pyperclip.copy(password)
    except Exception as e:
        print(f'mkp: error: \033[31m{type(e).__name__}\033[0m: {e}')
    else:
        if not args.silence:
            print(password)
