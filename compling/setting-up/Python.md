# Installing Python and using Conda Environments

## Anaconda

Navigate to [Anaconda](https://www.anaconda.com/products/distribution) and install the 
relevant version for your OS (use python 3.9, which should be the default). 
Once the file has downloaded, run the file and 
follow the install prompts. To work with Anaconda on Windows use the "Anaconda Powershell Prompt". For Mac (following the defaults during installation), 
I believe you need to enter the following commands from the Terminal once the initial 
installation has completed:

```
source /opt/anaconda3/bin/activate
conda init zsh
```

In restarting Terminal, you should now see 

```
(base) name@Mac ~ %
```

For Linux, I think it is straightforward. 

## Setting up environment

It is critical that we all use the same version of packages. The autograder will expect 
these specific versions as well. To facilitate this, I have shared with you a 
yml file which you should use to create a python environment in conda. 

Ensure that you see in your terminal (base):

```
(base) ...
```

Navigate to where you have downloaded the yml file and run:

```
conda env create -n LIANN --file LIANN.yml
```

This will create a new environment. To activate it, run:

```
conda activate LIANN
```

N.B. This may not work with new Mac's because of their new chips. I am looking into 
how to do this, so let me know if you run into an issue.

When working on assignments make sure you see (LIANN) instead of (base). We may need 
to add additional packages as the course unfolds. I will provide instructions on how to do 
this when needed. 

## Interacting with python via the command line

Now that you have python installed, you can interact with python via the command line.
There are two main ways of doing this: 1) via python's interpreter and
2) via running python scripts. 

To initiate python's interpreter just run the command python: 

```
(LIANN) forrestdavis:~$ python
iPython 3.9.4 (default, Apr  9 2021, 16:34:09) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Within the interpreter you can interact with python dynamically, which is useful for 
typing out small things. For any larger project, however, you should write a 
separate script (we return to this momentarily). Within the interpreter, we might 
create variables and manipulate them: 

```
>>> x = 1
>>> x += 1
>>> x
2
>>> theBest = 'Noam Chomsky'
>>> theBest.split(' ')
['Noam', 'Chomsky']
>>> 8*8981
71848
```

Notice that variables persist within the body of the interpreter. There are still scopes,
for example I can make a function with takes a string and adds '!' to the end. The
variables referenced within this function are not accessible to operations outside the 
function.

```
>>> def addAH(aString):
...     newString = aString + "!"
...     return newString
... 
>>> addAH(theBest)
'Noam Chomsky!'
>>> newString
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'newString' is not defined
```

Finally, we can run python scripts by python SCRIPTNAME.py. For example, I might 
have a script which has addAH from above in a file called excite.py. That is, 
opening excite.py, I should see: 

```
(LIANN) forrestdavis:~$ cat excite.py
def addAH(aString):

    newString = aString + '!'
    return newString

print(addAH('Noam Chomsky'))
(LIANN) forrestdavis:~$ python excite.py
Noam Chomsky! 
```
