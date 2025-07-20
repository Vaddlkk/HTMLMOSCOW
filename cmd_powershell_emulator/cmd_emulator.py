import os
import subprocess

def run_command(command):
    try:
        if os.name == 'nt':  # For Windows
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, creationflags=subprocess.DETACHED_PROCESS)
        else:  # For Unix/Linux/macOS
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(e.stderr)
    except FileNotFoundError:
        print(f"Command not found: '{command.split()[0]}'")

def main():
    print("Python CMD/PowerShell Emulator (type 'exit' to quit)")
    while True:
        try:
            current_dir = os.getcwd()
            user_input = input(f"{current_dir}> ")
            if user_input.lower() == 'exit':
                break
            elif user_input.strip() == '':
                continue
            run_command(user_input)
        except KeyboardInterrupt:
            print("\nExiting emulator.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()