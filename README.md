# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience
The game's purpose is to be a number-guessing game where players try to guess a secret number within a range based on difficulty, with hints, scoring, and attempt limits, built as a Streamlit web app to investigate and fix intentional glitches. Bugs found included backwards hint messages (e.g., saying "go higher" when the guess was too high), premature "out of attempts" messages, attempts incrementing on invalid guesses, session state not resetting on new games or difficulty changes, and incorrect range handling. Fixes applied involved correcting hint directions and arrows, adjusting attempt counting and loss checks to allow full attempt limits, ensuring session state resets properly, and updating range logic for dynamic difficulty changes.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
<img src="https://cdn.phototourl.com/uploads/2026-03-15-dfb26825-4c69-42cb-a04a-ee2bb2bebe49.png" width="80%" height="80%" alt="Winning Game"/>

## 🚀 Stretch Features

Challenge 4: 

<img src="https://cdn.phototourl.com/uploads/2026-03-15-dfb26825-4c69-42cb-a04a-ee2bb2bebe49.png" width="80%" height="80%" alt="Challenge 4"/>

