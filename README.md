Tireless Runner
===============

Tireless Runner is a small Python utility designed for simultaneously solving multiple test cases of the same algorithmic problem. The approach is very easy - You just have to implement 1 function solving the algorithmic problem and The Tireless Runner will spawn new thread for every test case.

Why threading is needed? Let me explain. Tireless Runner has been designed to help me with the qualifying round of Deadline24 (https://www.deadline24.pl). Deadline usually prepares optimization problems. It means that it's very hard to achieve the best possible solution for every test case. I always had been ending up with random numbers generator here and there in my solution, which had been run multiple times to find the best result.

This is where we need threads. Tireless Runner will spawn new thread for every test case and try to find the best possible solution by simply running prepared solving function multiple times.

Installation
------------
```
sudo pip install TirelessRunner
```

Example
-------

Let's consider a very trivial problem.

Assume that the task is to find `x` maximalizing the value of a function `f(x) = ax^2 + b` for given numbers `(a, b)` on a discrete interval `[-100, 100]`. (I told You that it is **very trivial** problem). The output should look like `x = ?` with `?` replaced by the number.

We have 3 input files, every file containing 2 numbers separated by single space: `a` and `b`. Solving function could look like this:

```python
from codingbuzz.tireless_runner import TirelessRunner
from random import randint


def solution(input_file_path):
    f = open(input_file_path, 'r')
    (a, b) = map(int, f.readline().split(' '))
    f.close
    x = randint(-100, 100)
    result = a * x**2 + b
    solution = "x = {}".format(x)
    return (result, solution)


TirelessRunner(solution).run()
```
The function simply reads `(a, b)` from `input_file_path`, generates random `x` and returns a touple `(result, solution)`, where:
*   `result` is a number indicating how good our solution is (Tireless Runner will use this number to compare different solutions),
*   `solution` is a text we should save as a actuall solution of the problem.

Then we have to put every test case in `in/` directory so the structure should look like this:
```
.
├── in
│   ├── test00.in
│   ├── test01.in
│   └── test02.in
└── solution.py
```

And run the Tireless Runner:
```
mskiba@example $ python solution.py 
2016-01-17 12:50:50,226 [INFO] [TirelessRunner] - Starting solution Thread for ./in/test02.in
2016-01-17 12:50:50,228 [INFO] [TirelessRunner] - ./in/test02.in has no previous result, starting from scratch
2016-01-17 12:50:50,227 [INFO] [TirelessRunner] - Starting solution Thread for ./in/test00.in
2016-01-17 12:50:50,227 [INFO] [TirelessRunner] - Starting solution Thread for ./in/test01.in
2016-01-17 12:50:50,228 [INFO] [TirelessRunner] - ./in/test01.in has no previous result, starting from scratch
2016-01-17 12:50:50,228 [INFO] [TirelessRunner] - ./in/test00.in has no previous result, starting from scratch
2016-01-17 12:50:50,228 [INFO] [TirelessRunner] - ./in/test02.in has found a better result: 0
2016-01-17 12:50:50,229 [INFO] [TirelessRunner] - ./in/test01.in has found a better result: 2035
2016-01-17 12:50:50,229 [INFO] [TirelessRunner] - ./in/test00.in has found a better result: -7569
2016-01-17 12:50:50,230 [INFO] [TirelessRunner] - ./in/test01.in has found a better result: 3491
2016-01-17 12:50:50,230 [INFO] [TirelessRunner] - ./in/test00.in has found a better result: 0
2016-01-17 12:50:50,231 [INFO] [TirelessRunner] - ./in/test01.in has found a better result: 6251
2016-01-17 12:50:50,232 [INFO] [TirelessRunner] - ./in/test01.in has found a better result: 9035
2016-01-17 12:50:50,239 [INFO] [TirelessRunner] - ./in/test01.in has found a better result: 9226
2016-01-17 12:50:50,244 [INFO] [TirelessRunner] - ./in/test01.in has found a better result: 9419
2016-01-17 12:50:50,248 [INFO] [TirelessRunner] - ./in/test01.in has found a better result: 10010
```

The Runner will create 2 directories:
*   `out/` containing solution files (`test00.ans`, `test01.ans`, `test02.ans`)
*   `storage/` contaning temporary files used by Tireless Runner.

File tree will look like this:
```
.
├── __init__.pyc
├── in
│   ├── test00.in
│   ├── test01.in
│   └── test02.in
├── out
│   ├── test00.ans
│   ├── test01.ans
│   └── test02.ans
├── solution.py
└── storage
    ├── test00.res
    ├── test01.res
    └── test02.res
```

This is very trivial problem so Tireless Runner will probably find the best solutions for given test cases.

You can find this example's source code under [this path](example/).

Requirements
------------

*   Solving function should accept 1 string argument: `input_file_path`.
*   Solving function should return a touple `(number, string)` - `(how good the solution is, the solution itself)`.
*   Subdirectory with input files `in/` should be placed in the same directory as the script using The Tireless Runner.
*   `in/` subdirectory should contain only input files with `.in` extension.
*   

Starting the Runner
-------------------
```python
from codingbuzz.tireless_runner import TirelessRunner

def solution(input_file_path):
    ...

TirelessRunner(solution).run()
```

To stop the runner press `CTRL + C`.

Starting over
-------------
Tireless Runner will cache results so You can rerun the script without worrying about the results. To start over (because, for example, Your solution was incorrect) You have to remove `storage/` and `out/` directories.
