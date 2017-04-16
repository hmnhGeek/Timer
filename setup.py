import cx_Freeze

executables = [cx_Freeze.Executable('timer.py')]

cx_Freeze.setup(
    name='PyTimer',
    options={"build_exe": {"packages":["time", "winsound"]}},

    description="PyTimer",
    executables = executables
    )
