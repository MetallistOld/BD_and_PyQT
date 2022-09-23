import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["common", "logs", "client", "unit_tests"],
}
setup(
    name="mess_server",
    version="0.1",
    description="mess_server",
    options={
        "build_exe": build_exe_options
    },
    executables=[Executable('server_.py',
                            base='Win32GUI',
                            targetName='client.exe',
                            )]
)
