import subprocess
import sys

def execute_command(command):
    """
    Выполняет заданную команду и выводит ее стандартный вывод и ошибки.
    """
    try:
        # Для Windows, часто нужно использовать shell=True для команд cmd/powershell
        # Если команда не найдена без shell=True, или если это внутренняя команда shell,
        # то shell=True может помочь. Однако, это может быть менее безопасно.
        # Для простоты и гибкости для запроса пользователя, используем shell=True.
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True,
            encoding='cp866' # Для корректного отображения кириллицы на Windows
        )
        print("--- Standard Output ---")
        print(result.stdout)
        if result.stderr:
            print("--- Standard Error ---")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения команды '{command}': {e}")
        print(f"Код возврата: {e.returncode}")
        if e.stdout:
            print(f"Stdout при ошибке:
{e.stdout}")
        if e.stderr:
            print(f"Stderr при ошибке:
{e.stderr}")
    except FileNotFoundError:
        print(f"Команда '{command}' не найдена. Убедитесь, что она доступна в вашей системе PATH.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Если передан аргумент командной строки, используем его как команду
        command_to_execute = " ".join(sys.argv[1:])
        print(f"Выполнение команды: {command_to_execute}")
        execute_command(command_to_execute)
    else:
        # Если аргументов нет, запускаем ipconfig по умолчанию
        print("Не указана команда. Запускаю 'ipconfig' по умолчанию.")
        print("Использование: python your_script_name.py <ваша_команда>")
        execute_command("ipconfig")

        # Примеры других команд, которые можно попробовать:
        # execute_command("dir") # Для Windows
        # execute_command("ls -la") # Для Linux/macOS
        # execute_command("whoami")
        # execute_command("netstat -an")
        # execute_command("get-process | select -first 5") # Пример PowerShell команды