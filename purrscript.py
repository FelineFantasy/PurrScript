#!/usr/bin/env python3

"""
PurrScript - cat-themed Python interpreter for .purr files
"""

import argparse
import os
import sys
import shutil
import platform
import re

VERSION = "1.0.0"

REPLACEMENTS = {
    "MR": "# program started",
    "PR": "# program finished",
    "treat": "True",
    "meow": "print",
    "beg": "input",
    "sniff_file": "read",
    "hiss_error": "try",
    "sniff": "if",
    "peer": "elif",
    "other_paw": "else",
    "and_paw": "and",
    "or_paw": "or",
    "not_paw": "not",
    "nap": "def",
    "box": "class",
    "bring": "return",
    "hunt": "while",
    "zoom": "for",
    "hiss": "break",
    "gimme": "import",
    "out_of": "from",
    "with_blanket": "with",
    "as_paw": "as",
    "yowl": "raise",
    "purr": "str",
    "bite": "int",
    "lick": "float",
    "mood": "bool",
    "tail": "list",
    "basket": "tuple",
    "clowder": "set",
    "scent": "dict",
    "void_box": "None",
    "claw": "open",
    "scratch": "write",
    "close_door": "close",
    "catch_mouse": "except",
    "finally_nap": "finally",
    "YES": "True",
    "NO": "False",
}

_ORDERED = sorted(REPLACEMENTS.items(), key=lambda kv: -len(kv[0]))


def translate_purr(code):
    for old, new in _ORDERED:
        code = re.sub(rf'\b{re.escape(old)}\b', new, code)
    return code


def pause(message="\nНажми Enter для выхода..."):
    if not sys.stdin.isatty():
        return
    try:
        input(message)
    except (EOFError, KeyboardInterrupt):
        pass


def ask(question, default="n"):
    if not sys.stdin.isatty():
        return default
    try:
        return input(question)
    except (EOFError, KeyboardInterrupt):
        return default


def get_install_dir():
    system = platform.system()
    if system == "Windows":
        return os.path.join(os.environ.get("LOCALAPPDATA", os.path.expanduser("~")), "PurrScript")
    else:
        return os.path.join(os.path.expanduser("~"), ".local", "share", "purrscript")


def get_executable_name():
    system = platform.system()
    if system == "Windows":
        return "purr.exe"
    else:
        return "purr"


def is_installed():
    install_dir = get_install_dir()
    exe_name = get_executable_name()
    return os.path.exists(os.path.join(install_dir, exe_name))


def install():
    print("Установка PurrScript...")
    install_dir = get_install_dir()

    if not os.path.exists(install_dir):
        os.makedirs(install_dir)

    exe_name = get_executable_name()
    target = os.path.join(install_dir, exe_name)

    if os.path.abspath(sys.argv[0]) != os.path.abspath(target):
        shutil.copy(sys.argv[0], target)
        print(f"Скопирован {exe_name}")

        system = platform.system()
        if system != "Windows":
            os.chmod(target, 0o755)
    else:
        print("PurrScript уже установлен!")

    if platform.system() == "Windows":
        bat = f'''@echo off
"{install_dir}\\{exe_name}" %*
'''
        bat_path = os.path.join(install_dir, "purr.bat")
        if not os.path.exists(bat_path):
            with open(bat_path, "w") as f:
                f.write(bat)
            print("Создан purr.bat")

    if ask("Добавить в PATH? (y/n): ").lower() == 'y':
        system = platform.system()
        if system == "Windows":
            os.system(f'setx PATH "%PATH%;{install_dir}"')
            print("PATH обновлён!")
        else:
            shell_rc = os.path.expanduser("~/.bashrc")
            if os.path.exists(os.path.expanduser("~/.zshrc")):
                shell_rc = os.path.expanduser("~/.zshrc")

            with open(shell_rc, "a") as f:
                f.write(f'\nexport PATH="$PATH:{install_dir}"\n')
            print(f"PATH добавлен в {shell_rc}")

    print("\nУстановка завершена!")
    print("Перезапусти терминал")
    print("Теперь можно: purr hello.purr")
    pause()


def show_help():
    print("PurrScript Interpreter")
    print("Использование: purr файл.purr")
    print("Пример: purr hello.purr")
    pause()


def run_interpreter(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        sys.stderr.write(f"Файл не найден: {filename}\n")
        pause()
        sys.exit(1)

    if "MR" not in content:
        sys.stderr.write("EntryThresholdNotFound\n")
        pause()
        sys.exit(1)
    if "PR" not in content:
        sys.stderr.write("ExitDoorAjar\n")
        pause()
        sys.exit(1)
    if "treat" not in content:
        sys.stderr.write("NoSnacksError\n")
        pause()
        sys.exit(1)

    python_code = translate_purr(content)
    try:
        g = {"__name__": "__main__", "__file__": filename}
        exec(compile(python_code, filename, "exec"), g)
    except Exception as e:
        sys.stderr.write(f"{e}\n")
        pause()
        sys.exit(1)

    pause()


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="purr",
        description="PurrScript — cat-themed Python interpreter for .purr files",
    )
    parser.add_argument("file", nargs="?", help="путь к .purr файлу")
    parser.add_argument(
        "--install", action="store_true",
        help="установить PurrScript (копирование в каталог установки + PATH)",
    )
    parser.add_argument(
        "--version", action="version", version=f"PurrScript {VERSION}",
    )
    args = parser.parse_args(argv)

    if args.install:
        install()
        return

    if args.file:
        if not args.file.endswith(".purr"):
            sys.stderr.write(f"Не .purr файл: {args.file}\n")
            sys.exit(2)
        run_interpreter(args.file)
        return

    if is_installed():
        show_help()
    else:
        install()


if __name__ == "__main__":
    main()
