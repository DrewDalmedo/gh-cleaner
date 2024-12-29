# Repo Reaper

Python script for deleting old Github repos

## About

### Background

Back in 2020 I attended the Flatiron School coding bootcamp. At the time I'm writing this, it has been nearly 5 years since I went there.

As part of the program, we linked our public Github accounts and forked each lesson as a Git repo from the bootcamp's own Github account. In theory, this would demonstrate our programming abilities and act as a publicly verifiable check that we actually attended and completed the bootcamp. 

In reality, I had over 330 repos that contained dead code and buried my actual projects. I never looked at or referenced these old bootcamp repos, and they only served as padding to my actual portfolio.

In other words, it looked ugly and it was too much work to manually go through and delete each and every repo. Github doesn't provide a way to mass-delete repositories using its web interface, so a script was required to make the task viable.

### About the Script 

This Python script uses Github's API via `PyGithub` to delete repos that match a user-specified regex. This allows for the relatively quick mass-deletion of repos that match a particular pattern. 

Deletion based on date was considered, but was too impercise as it could unintentionally delete non-bootcamp repos that were within the same date range. Pattern-matching with the ability to print the matched repos prior to deletion was considered a more optimal solution.

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

It's recommended that you use [devenv](https://devenv.sh) for a reproducible development environment. This should match exactly what I used locally to develop the script. Any usage of the script outside of devenv is unsupported. 

If you want to create a venv with a requirements.txt, the only dependency is [PyGithub](https://github.com/PyGithub/PyGithub). 

#### Personal Access Token

You'll be required to provide a [classic Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic) to use the script. Follow the guide linked to create one. 

Additionally, make sure the following required scopes are checked:

- `repo`
- `delete_repo`

If you have repos that are a part of `orgs`, `enterprises`, or `projects` that you'd want to delete, make sure you enable those as well.

#### .env file

Once you have your [Personal Access Token](#personal-access-token), create a .env file at the root of the project directory.

Add the following to the .env file:

```
GITHUB_TOKEN=your-token-here
```

Additionally, if you're testing the script and want to avoid accidentally deleting repos, you can set the `SAFE_MODE` variable like so:

```
SAFE_MODE=1
```

If `SAFE_MODE` is set to anything, it will be considered enabled. To disable `SAFE_MODE`, remove the variable from your .env file.

#### Using .env outside of devenv

If you're not using [devenv](#devenv), you'll need to manually source the .env file before running the script.

Simply run the following:

```
source .env
```

This will save the variables you've defined in your .env until you exit your current shell session.

Alternatively, you could export the variables without making a .env like so:

```
export GITHUB_TOKEN=your-token-here
```

This will have the same effect as sourcing your .env file.

#### Running the script

To enter the [devenv](#devenv) development environment, simply run the following command:

```
devenv shell
```

Then, run the Python script:

```
python3 cleanup.py ...
```

Replace `...` with the arguments you'd like to use.

Alternatively, you could do this all in one line:

```
devenv shell -- python3 cleanup.py ...
```
