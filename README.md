# Bootcamp Begone

Python script for deleting old Github repos

## About / Why?

Back in 2020 I attended the Flatiron School coding bootcamp. It has nearly been 5 years since I went there.

As part of the program, we linked our public Github accounts and forked each lesson as a Git repo from the bootcamp's own Github account. In theory, this would demonstrate our programming abilities and act as a publicly verifiable check that we actually attended and completed the bootcamp. In reality, I had over 330 repos that contained dead code and only served to bury my actual projects. I never looked at or referenced these old bootcamp repos, and they only served as padding to my actual portfolio of projects.

In short, it was unaesthetic as hell and it made me unhappy.

This Python script uses Github's API to delete repos that match a specified regex.

## Usage

### Synopsis 

```
usage: cleanup.py [-h] [-p PATTERNS [PATTERNS ...]] [-l] [-f]

Delete Github repositories that match regex patterns

options:
  -h, --help            show this help message and exit
  -p PATTERNS [PATTERNS ...], --patterns PATTERNS [PATTERNS ...]
                        What regex patterns to match repos against. Required.
  -l, --list            List repos that would be deleted without deleting them
  -f, --force           Delete all repos without y/n confirmation
```

### Setting up the development environment

#### devenv

It's recommended that you use [devenv](https://devenv.sh) for a reproducible development environment. This should match exactly what I used locally to develop the script. Any usage outside of devenv is unsupported. 

If you want to create a venv with a requirements.txt, the only dependency is [PyGithub](https://github.com/PyGithub/PyGithub) 

#### .env file

`info on what env vars are required`

