# Dine Safe.ly
[![Build Status](https://travis-ci.com/gcivil-nyu-org/dine-safe-ly.svg?branch=develop)](https://travis-ci.com/gcivil-nyu-org/dine-safe-ly)
[![Coverage Status](https://coveralls.io/repos/github/gcivil-nyu-org/dine-safe-ly/badge.svg?branch=main)](https://coveralls.io/github/gcivil-nyu-org/dine-safe-ly?branch=main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

A dine-in app that leverages daily COVID-19 data to provide updated compliance status and hot spot notifications for reopened NYC restaurants.

https://dine-safe-ly.herokuapp.com/

# Assignment 1

## Introduction

>  I am running into issues deploying my code.
- I have followed this tutorial (https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true#introduction) in order to try to get my instance running, however I was running into issues when I was trying to run the command `heroku ps:scale web=1 `. This plagued me for the entirety of the assignment:

## Code Samples


```
 ➜ heroku ps:scale web=1
Scaling dynos... !
 ▸    Couldn't find that process type (web).
```
- To try to resolve this issue, I have looked to several stack overflow forums (https://stackoverflow.com/questions/48512013/couldnt-find-that-process-type-heroku) in which they suggested `deleting Procfile`, removing and reinstalling buildpacks. Nothing seemed to resolve the issue...
- I have installed the requisite heroku buildpacks,
```
Buildpack added. Next release on damp-headland-14639 will use:
  1. heroku/python
  2. heroku-community/apt
  3. https://github.com/heroku/heroku-geo-buildpack.git
```

