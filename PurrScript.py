import os
import sys
import shutil
import platform
import subprocess


def translate_purr(code):
    replacements = {
        "MR": "# program started",
        "PR": "# program finished",
        "treat": "True",
        "meow": "print",
        "beg": "input",
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
        "sniff_file": "read",
        "close_door": "close",
        "hiss_error": "try",
        "catch_mouse": "except",
        "finally_nap": "finally",
        "YES": "True",
        "NO": "False",
    }
    for old, new in replacements.items():
        code = code.replace(old, new)
    return code


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

    choice = input("Добавить в PATH? (y/n): ")
    if choice.lower() == 'y':
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
    input("\nНажми Enter для выхода...")


def show_help():
    print("PurrScript Interpreter")
    print("Использование: purr файл.purr")
    print("Пример: purr hello.purr")
    input("\nНажми Enter для выхода...")


def run_interpreter():
    if len(sys.argv) < 2:
        show_help()
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        sys.stderr.write(f"Файл не найден: {filename}\n")
        input("\nНажми Enter для выхода...")
        sys.exit(1)

    if "MR" not in content:
        sys.stderr.write("EntryThresholdNotFound\n")
        input("\nНажми Enter для выхода...")
        sys.exit(1)
    if "PR" not in content:
        sys.stderr.write("ExitDoorAjar\n")
        input("\nНажми Enter для выхода...")
        sys.exit(1)
    if "treat" not in content:
        sys.stderr.write("NoSnacksError\n")
        input("\nНажми Enter для выхода...")
        sys.exit(1)

    python_code = translate_purr(content)
    try:
        exec(python_code)
    except Exception as e:
        sys.stderr.write(f"{e}\n")
        input("\nНажми Enter для выхода...")
        sys.exit(1)

    input("\nНажми Enter для выхода...")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].endswith('.purr'):
        run_interpreter()
    elif len(sys.argv) > 1:
        install()
    elif is_installed():
        show_help()
    else:
        install()
