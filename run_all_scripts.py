import os
import subprocess
import ctypes

# Minimize the current Python window
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

scripts_dir = os.path.dirname(os.path.abspath(__file__)) + "/scripts"

for filename in os.listdir(scripts_dir):
    if filename.endswith('.py') and filename != os.path.basename(__file__):
        script_path = os.path.join(scripts_dir, filename)
        print(f"Exécution de {filename}...")
        subprocess.run(['python', script_path], creationflags=subprocess.CREATE_NO_WINDOW)