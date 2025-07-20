import subprocess
import os

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print(result.stdout)
        print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.cmd}")
        print(f"Return code: {e.returncode}")
        print(f"Output: {e.stdout}")
        print(f"Error output: {e.stderr}")
    except FileNotFoundError:
        print(f"Command not found: '{command}'")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("Python Mini-Shell. Type 'exit' to quit.")
    while True:
        try:
            cmd = input(f"{os.getcwd()}> ")
            if cmd.lower() == 'exit':
                break
            if cmd.strip():
                # Handle 'cd' separately
                if cmd.lower().startswith('cd '):
                    try:
                        path = cmd[3:].strip()
                        os.chdir(path)
                    except FileNotFoundError:
                        print(f"Directory not found: '{path}'")
                    except Exception as e:
                        print(f"Error changing directory: {e}")
                else:
                    run_command(cmd)
        except KeyboardInterrupt:
            print("
Exiting shell.")
            break
        except Exception as e:
            print(f"An error occurred in the shell loop: {e}")
