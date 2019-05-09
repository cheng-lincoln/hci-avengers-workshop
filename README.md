# HCI Avengers Workshop

### About

This repository contains the source code that will be used to run an interest-garnering workshop for high school students who have absolutely no knowledge of programming or cybersecurity but are interested to find out more.

Students will be taught very basic programming skills in the first hour, before embarking on 3 exercises. Each exercise will require them to write a few lines of code in attempt to crack a given password.



### How To Use

The 3 exercises can be found in `/src/exercises`:

- `hulk.py`
- `strange.py`
- `thanos.py`

Inside each of these files is a function `crack(*args)` where students will write their code inside. The function comes with input parameters that provide them with their previous guess, as well as auxiliary parameters depending on the exercise.



To run the exercises, run the following command in the root folder:

```bash
python -m avenge
```

The code is compatible with `python 3`.

You will be prompted to choose which exercise, as well as what input mode.



### Exercise Details

1. For the purpose of simplicity, all passwords are 4 characters long, restricted to lower case alphabets.
2. The name of the avenger gives a clue as to how the exercise should be solved.



### Workshop Related Links

- [Have I been PWNED?!?!](https://haveibeenpwned.com/)



### Using an online IDE like *repl.it*

If stable internet access is readily available, consider using an online IDE like `repl.it` to run the exercise.

1. Go to https://repl.it/github

   1. Paste in the **Repository URL**: https://github.com/lincoln-ch/hci-avengers-workshop.git
   2. Select **Language**: `Python` (or any `Python 3 `equivalent, do not choose other versions)
   3. Click **Submit**

2. In `main.py`, replace everything with the following:

   ```python
   import os
   os.system('python -m avenge')
   ```

3. On the left tab, click the **settings** icon (wheel-like).
   1. Under **indent type**: choose `spaces`
   2. Under **indent size**: choose `4` 
4. You can write the exercise code in:
   1. `src/exercises/hulk.py`
   2. `src/exercises/strange.py`
   3. `src/exercises/thanos.py`

5. Press **Run** on the top-middle section to run the program.

