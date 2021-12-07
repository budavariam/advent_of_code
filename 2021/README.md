# 2021

I use python 3.9 on mac.

```bash
python3 -m venv .ve
. ./.ve/bin/activate
pip install -r requirements.txt

./init.py 1 1
./test.sh
./start.sh

deactivate
```

| Type       | Code                        | Description                                                        |
| ---------- | --------------------------- | ------------------------------------------------------------------ |
| Inputfile  | `python3 solution.py`       | reads input.txt file from the current folder.                      |
| Unittest   | `python3 solution_test.py`  | runs the unit tests for the code                                   |
| Template   | `./init.py ${DAY} ${PART}`  | create a wireframe for the solution, and open the new files        |
| QuickStart | `./start.sh ${DAY}_${PART}` | start solution from 2021 root folder, the parameter can be omitted |
| QuickTest  | `./test.sh ${DAY}_${PART}`  | start test from 2021 root folder, the parameter can be omitted     |
