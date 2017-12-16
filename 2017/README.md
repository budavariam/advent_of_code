# 2017

I use python3 on windows.

```batch
virtualenv -p c:\Python36\python.exe .ve
.ve\Scripts\activate

deactivate
```

Type | Code | Description
---- | ---- | ----
Inputfile | `python code.py --input` | reads input.txt file from the current folder.
Testargument | `python code.py --test value` | reads the value into the solution function
Unittest | `python code.test.py` | runs the unit tests for the code
Debug | `python code.py` | runs the program with a MAGIC debug data for quick debugging.