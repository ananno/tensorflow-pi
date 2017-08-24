# Tensorflow-Pi

## Introduction
Here is a very simple example of calculating pi using polynomial estimation. But the main point of this project is to use tensorflow to calculate the polynomial componenets in massive parallel session.

## Background
First, lets choose  a easy polynomial to estimate pi. Here is the formula:

```
Pi = 4 * ( 1 - (1/3) + (1/5) - (1/7) + (1/9) - ...)
```

It's one of the many polynomial that can be used for calculating pi. It is very simple one.

## Serial Code
The serial code _[polynomial-pi.py]_ is to give an idea straight forward how this works. It generates the polynomial components in for loop and make sum of them accordingly. Finaly calculate the pi.

## Parallel Code
This is the challenge. Do it yourself and push your code in this repo. Please follow the following rule.

1. Please put all your code in one file
2. File name should be like : parallel-pi-_[your name]_.py
3. You can create a seperate git branch and push your code there. _[Recommended]_

_Note_ : Please feel free to contact via email _[ananno@outlook.com]_ if you need any help.

-| HAVE FUN |-
