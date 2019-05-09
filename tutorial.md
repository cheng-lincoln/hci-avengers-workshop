# HCI Avengers Workshop - Tutorial

### Objective

The purpose of this tutorial is to quickly introduce to non-programmers the basic python programming skills required to complete the workshop activity.  



### Setup

We will write all the code in a file named `main.py`. We will assume that you are already in the directory where `main.py` is.



#### Hello World

In `main.py`:

```python
print('Hello World!')
```

In the shell, type the following, followed by the `enter` key:

```bash
python main.py
```

In the output, you will see:

```
Hello World!
```



From here on, you type your code in `main.py`, and run the python script in your shell like above.



#### Code is sequential

Code is executed line after line.

In `main.py`:

```python
print('Hello World!')
print('Goodbye!')
```

In the output, you will see:

```
Hello World!
Goodbye!
```



#### Comments

Comments are denoted by a `#` in front, and are ignored in your code. Comments are used to convey messages from one developer to another or her/himself. 

In `main.py`:

```python
print('Hello World!')
# It is a sunny day!
# print('The sky is blue!')
print('Goodbye!')
```

In the output, you will see:

```
Hello World!
Goodbye!
```



#### Variables

Variables are used to store values in code.

In `main.py`:

```python
#In programming, = is the assignment operator. Whatever is on the right-hand-side is assigned to the left-hand-side.
x = 1 #x is a variable that is assigned the value 1
y = 'Hey!' #y is a variable that is assigned the string 'Hey!'
z = True #z is a boolean variable that is assigned to represent True
print(x) 
print(y)
```

In the output, you will see:

```
1
Hey!
```

Note that the apostrophes are missing from the printout `Hey!`. This is because the `y` is a `string` type. In python, you need to add apostrophes to "sentences" or "words".

```python
y = Hey! #Invalid - Hey is not a recognized python keyword.
y = 'Hey!' #Valid - Hey! here is recognized as a string
```



#### Operators

Variables are useless if they cannot interact with one another. In python, variables can interact with one another via operators.

In `main.py`:

```python
x = 2
y = x + 3 #y is 3
z = x * y #z is 10
print(z + x) #12 is printed
```

In the output:

```
12
```



#### Combining printouts

In `main.py`:

```python
name = 'Alice'
age = 15
print(name + 'is' + age + 'years old!')
#OR
print('{0} is {1} years old!'.format(name, age)) #name replaces {0}, age replaces {1}
```

In the output:

```
Alice is 15 years old!
Alice is 15 years old!
```



#### Conditions

We saw an example of a `boolean` variable above. That is, the variable represents whether something is `True` or `False` (note the capital `T` and `F`). We use it to make decisions.

In `main.py`:

```python
if (True):
    print('Alice is happy.')
else:
    print('Alice is sad.')
```

In the output:

```
Alice is happy.
```



We can use `boolean` variables to do more useful work.

In `main.py`:

```python
score = 56
PASSING_SCORE = 60
if (score >= PASSING_SCORE): #Here, (56 >= 60) evaluates to False, and thus the 'else' statement is executed
    print('You have passed! :)')
else:
    print('You have failed :(')
```

In the output:

```
You have failed :(
```



We can also use the `elif` (else if) statement to perform more conditional checks:

In `main.py`:

```python
score = 60
PASSING_SCORE = 60
if (score > PASSING_SCORE):
    print('You have passed!')
elif (score == PASSING_SCORE): #Note the double equal sign. To check equality, we use double equal sign. Single equal sign is used for assignment (see above)
	print('You have just passed. Phew! :/')
else:
    print('You have failed! :(')
```

In the output:

```
You have just passed. Phew! :/
```



Note that `boolean` variables can be assigned before passing into the `if()` statement:

```python
salary = 3000
dress = 1200
can_afford = (salary > (2 * dress)) #the variable 'can_afford' is assigned the boolean value of True, since salary is more than twice the price of a dress.
if (can_afford):
    print('Alice is happy!')
else:
    print('Do not meet Alice today.')
```

In the output:

```
Alice is happy!
```



#### Combining Conditions

Using the keywords `and`, `or` and `not`, we can combine conditions to make even more meaningful decisions.

In `main.py`:

```python
alice_likes_roses = True
if (not alice_likes_roses): #not True results in False. Else statement executed.
	print('Ask Alice what flowers she like.')
else:
    print('Buy Alice roses.')
```

In the output:

```
Buy Alice roses.
```

Here, we see that the `not` keyword **inverts** the condition.



In `main.py`

```python
salary = 3000
dress = 1200
can_afford = (salary > (2 * dress)) #i.e True
alice_likes_roses = False
if (can_afford or alice_likes_roses):
    print('Buy roses just in case.')
else:
    print('Switch off your phone for today.')
```

In the output:

```
Buy roses just in case.
```

Here, we see that `or` evaluates to `True` as long as **at least one** condition is `True`.



In `main.py`:

```python
students_are_naughty = True
weather_is_bad = True
if (students_are_naughty and weather_is_bad):
	print('Be nice to Alice.')
else:
    print('Be nice to Alice too.')
```

In the output:

```
Be nice to Alice.
```

Here, we see that `and` evaluates to `True` only if **all** the conditions are `True`



#### Nesting Conditions

In `main.py`:

```python
dress = 1200
salary = 2000

alice_can_afford = 3000 > 1200 * 2
alice_likes_roses = True
roses_are_in_stock = False

if (alice_can_afford):
    print('Alice is happy.')
else:
    if (alice_likes_roses):
        if (roses_are_in_stock):
            print('Buy roses for Alice.')
        else:
            print('Look for another shop that sells roses.')
    else:
        print('Switch off your phone for today.')
```

In the output:

```
Look for another shop that sells roses.
```



#### Using Functions

For this gentle introduction, we will not learn how to write functions. Instead, we will try to develop an intuition on how to use functions.

In `main.py`:

```python
#Assume we have a function round(), which takes in a decimal, and rounds it up.
x = 3.6
y = round(x) #y will be equals to 4.0
print(y)
```

In the output:

```
4.0
```

Here, we see that `round` is the name of the function. This is followed by braces `()` (alike a mouth), where you put in what the function expects as an input. In this case, `round` expects a decimal number to be "fed into" its mouth. The function then "spits" out the number `4.0`, which is then assigned to `y`.



In fact, `print` is also a function, and we have been using it since the start of this tutorial! Let us combine the use of functions.

In `main.py`:

```python
print(round(14.5))
```

In the output:

```
15.0
```

Here, we evaluate from the **inner most function** (i.e `round`). We see that `round` gobbles up `14.5` and spits out `15.0`. Then, `print` gobbles up `15.0` and writes the text `15.0` to the screen!



#### Remarks

If you understood all of the above, you should be equipped with the necessary skills to solve the workshop activity! Of course, this is a very simple introduction to Python. If you are interested, you can learn more yourself online!
