#!.ve/bin/python

from cookiecutter.main import cookiecutter
import sys
import os

# Defaults that can be used in this file
editor = 'code'
main = 'solution'
test = 'solution_test'
inputfilename = 'input'

if len(sys.argv) > 1:
    # Values from user input
    day = f"{sys.argv[1]:0>2}"
    part = sys.argv[2] if len(sys.argv) > 2 else 1
else:
    print("Please specify a start day. Exiting..")
    sys.exit(1)

foldername = f"{day}_{part}"

if os.path.isdir(f"./{foldername}"):
    print("Folder already exists. Exiting...")
    sys.exit(1)

# Generate template
cookiecutter(
    'template',
    extra_context={'part': part, 
        'day': day,
        'input': inputfilename,
        'main': main,
        'test': test,
    },
    no_input=True,
    skip_if_file_exists=True,
)


# Open editor to begin
os.system(f"{editor} ./{foldername}/{inputfilename}.txt ./{foldername}/{test}.py ./{foldername}/{main}.py")