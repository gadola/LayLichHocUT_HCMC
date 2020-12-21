from cx_Freeze import setup, Executable
 
base = None    
 
executables = [Executable("bot.py", base=base)]
 
packages = ["idna","PIL","selenium", "requests", "pytesseract", "shutil", "webdriver_manager","pyautogui"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}
 
setup(
    name = "Login UT",
    options = options,
    version = '0.1.1',
    description = 'get schedule in college',
    executables = executables
)