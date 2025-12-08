# 2025

I use python 3.11 on mac with pyenv.

```bash
pyenv shell 3.11.4
python3 -m venv .ve
. ./.ve/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

./init.py 1 1
./test.sh 01_1
./start.sh 01_1

deactivate
```

| Type       | Code                        | Description                                                        |
| ---------- | --------------------------- | ------------------------------------------------------------------ |
| Inputfile  | `python3 solution.py`       | reads input.txt file from the current folder.                      |
| Unittest   | `python3 solution_test.py`  | runs the unit tests for the code                                   |
| Template   | `./init.py ${DAY} ${PART}`  | create a wireframe for the solution, and open the new files        |
| QuickStart | `./start.sh ${DAY}_${PART}` | start solution from 2021 root folder, the parameter can be omitted |
| QuickTest  | `./test.sh ${DAY}_${PART}`  | start test from 2021 root folder, the parameter can be omitted     |
