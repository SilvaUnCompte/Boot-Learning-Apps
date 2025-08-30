# Boot-Learning-Apps
Every time you start up your computer, launch quiz applications to learn through repetition.

I personnaly use it for vocabulary (In French). I also put a example with english basics.

If you happen to come across this Git repository and you create your own revision exercises, feel free to send them to me. It could be interesting to have a list of exercises to work on.

## Project Structure

```
Boot-Learning-Apps/
├── run_all_scripts.py              # Script to run all learning scripts.
├── scripts/
│   ├── english_basics.py           # Example: English basics.
│   ├── vocabulary.py               # Example: Tools to practice vocabulary (current in French)
│   ├── vocabulaire.xlsx            # Excel file containing vocabulary to study.
```

## Requirements

- Python 3.x
- Required library: `pandas` (to handle the Excel file)

To install dependencies:
```powershell
pip install pandas
```

## Usage
### Manual Use

1. Open a terminal and navigate to the project folder.
2. To run all learning scripts:
    ```powershell
    python run_all_scripts.py
    ```
3. To run a specific script:
    ```powershell
    python scripts/english_basics.py
    python scripts/vocabulary.py
    ```

### Run at Boot

To automatically launch the learning apps when your computer starts:

1. Create a shortcut to `run_all_scripts.py`.
   1. You have example for Windows [here](./put_me_in_boot_folder.lnk).
   2. Modify the shortcut properties to set the correct script and python path (look like `C:\Python313\python.exe "C:\Users\your\path\to\run_all_scripts.py"`).
2. Place the shortcut in your system's startup folder:
    - **Windows:** Press `Win + R`, type `shell:startup`, and place the shortcut in the opened folder.
    - **macOS/Linux:** Use system-specific startup application managers or add a command to your shell profile.
3. Ensure Python and required libraries are installed and accessible.

Now, your learning scripts will run automatically every time your computer boots up.

*Feel free to suggest improvements or add new exercises.*