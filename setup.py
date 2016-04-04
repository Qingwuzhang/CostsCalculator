import sys

from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes":["re"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
        name = "CostsCalculator",
        version = "2.0",
        description = "CostsCalculator",
        options = {"build_exe": build_exe_options},
        executables = [Executable("CostsCalculator2.py", base = base, icon="CostsCalculator.ico")])
