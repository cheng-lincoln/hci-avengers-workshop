# HCI Avengers Workshop

### About

This repository contains the source code that will be used to run an interest-garnering workshop for high school students who have absolutely no knowledge of programming or cybersecurity but are interested to find out more.

Students will be taught very basic programming skills in the first hour, before embarking on 3 exercises. Each exercise will require them to write a few lines of code in attempt to crack a given password.



### Environment Setup 

If the students are bringing their personal laptops, it is recommended for course administrators to use the following tools for easier setup of the required environment.

- [Portable Python](https://portablepython.com/)
- [Visual Studio Code Portable Mode](https://code.visualstudio.com/docs/editor/portable)



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

The code is written in `python 2.7.15` and is forward compatible with any later python versions.

You will be prompted to choose which exercise, as well as what input mode.



### Exercise Details

1. For the purpose of simplicity, all passwords are 4 characters long, restricted to lower case alphabets.
2. The name of the avenger gives a clue as to how the exercise should be solved.



### Workshop Related Links

- [Have I been PWNED?!?!](https://haveibeenpwned.com/)
