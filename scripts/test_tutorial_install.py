import os

commands = [
        'git --version',
        'python --version',
        'python -c "import flake8"',
        'python -c "import jupyter"',
        'python -c "import jupyter"',
        'python -c "import matplotlib"',
        'python -c "import numpy"',
        'python -c "import scipy"',
        'python -c "import pytest"',
        'python -c "import sphinx"',
        ]

# Check everything except conda
success_flag = True
for command in commands:
    if os.system(command) != 0:
        success_flag = False
        print("Failure!  %s failed" % command)

# # Check conda because its magic setup does not let us just run it.
# if not os.environ['CONDA_EXE'] or not os.environ['CONDA_PYTHON_EXE']:
#     print('Install check failed!  Conda is not installed correctly!')
#     success_flag = False
# else:
#     print('Conda installed and set in environment.')

# Final results
if success_flag is False:
    print('Install check failed!  Please see the above error messages. 🔥🔥🔥')
else:
    print('Success!  Everything has installed correctly. 😊😊😊')
