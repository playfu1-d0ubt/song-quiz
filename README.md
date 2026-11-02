# Song Quiz
![Tests](https://github.com/playfu1-d0ubt/song-quiz/actions/workflows/tests.yml/badge.svg)

A console game written in Python. Players log in, guess songs from the first letter of the title and the artist's name, and compete on a leaderboard.

I first wrote it for my GCSE Computer Science controlled assessment, then came back later to fix bugs and tidy it up.

## Features

- Login system with new accounts (username = first 4 letters of your name + your age)
- Passwords are hashed, but legacy plain text passwords still work
- Songs and artists loaded from a text file you can edit
- Shows the first letter of the title, with blanks for the rest
- Two guesses per song: 3 points for a first-time answer, 1 point for a second
- Total score and percentage at the end of the game
- Scores saved to a file, with a top 10 leaderboard

## How to run
 
You need Python 3.
 
```bash
git clone git@github.com:playfu1-d0ubt/song-quiz.git
cd song-quiz
python3 song_quiz.py
```
 
| File | What it does |
| --- | --- |
| `song_quiz.py` | The game |
| `Quiz.txt` | One song per line as `song:artist`. Swap in your own |
| `users.txt` | Created automatically when the first account is made (`name:username:password`) |
| `Score.txt` | Created automatically after the first game (`name:score:percent`) |
 
## Running the tests

```bash
pip install -r requirements.txt
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
```

The tests cover the hint maker, password hashing and checking, reading files, the menu choice checker and the leaderboard. They use small fake data and temporary files, so your real `users.txt` and `Score.txt` are never touched. The same tests run on GitHub on every push.

## Limitations
 
- Console only, with no graphical interface.
- Logins and scores are stored in plain text files, not a database or JSON.
- Legacy plain text passwords are still accepted for older accounts.
- One difficulty level and one song list, with a fixed number of rounds.
- The menus, `login`, `new_login` and `quiz` aren't covered by tests yet, because they depend on typed input.

## What I learned
 
### Testing
> This section is from my original manual testing

I planned tests for each input using normal, boundary and erroneous data:
 
| What I tested | Normal | Boundary | Erroneous |
| --- | --- | --- | --- |
| Username | Bon15 | james7 | karen |
| Password | Password | passwor | 4.80 |
| Menu choice | 1, -1 | -2, 3 | A, 7.4 |
| Name | Bon | james | 7 |
| Age | 12 | - | James |
| Guess | Half-life | - | 12 |
 
### Bugs I found and fixed
 
- A missing `int()` around menu input, so choices never matched
- An attribute error caused by a mistake with `strip`
- Pressing Enter twice kept repeating the last username
- Login only worked for a few lines of the user file, and retries failed

### What I'd do next
 
- Add more song categories or difficulty levels
- Let players pick how many rounds to play
- Move logins and the leaderboard to JSON
- Pull the scoring and the name, age and password checks out of `quiz` and `new_login` into small functions, so they can be tested