# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  It looked like a normal game site interface, fairly appealing, and not overwhelming, it was simple. 
- List at least two concrete bugs you noticed at the start
  (for example: "the hints were backwards").
  1. The hints do not work when you start a new game (so they only work on the first try), you have to refresh your screen and play it to work.
  2. The first bug I listed is most likely because the submit button does not work either, after your first try at the game.
  3. The "out of attempts..." message shows up when you have 1 attempt left, so it is too early.
  4. You can see the correct (secret) number being looked for in developer debug info, but the hint for the normal game asks the user to go higher when their number is already above the secret number. 
  5. When you change the difficulty of the game, the page doesn't appropriately the range you are suppose to be guessing within.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Copilot, and ChatGPT.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  An AI suggestion was to add resets for status, history, and use dynamic low/high for the secret, I verified the result by inputting that fix, then trying to start a new game to see if it worked. The suggestion was correct. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  Being completely honest, AI was an absolute beast with this. It didn't really mislead me on anything. A slight example Ihave for this would have to be when I tried addressing the guess count issue, and it said it was handled, but when I checked I was still expressing the same issue. So I gave a better description of the issue by saying "Why do i get a out of attempts message when it says I have 1 more attempt left" and it seemed to understand that better. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I would go back to the game and try to trigger ths specific function.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I tested the backward hints. For this I checked the secret code and so that it was 69, so I put 68 in as my guess, it then said that I had to go higher.
  Then I put 70 as my guess, then the hint prompted me to go lower.
- Did AI help you design or understand any tests? How?
  It helped me design the hint test, by telling me that the logic behind the code was in fact backwards, all I had to do was switch it around.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns mean that every time a user interacts with the app—like clicking a button or changing a slider—the entire Python script runs from top to bottom again, refreshing the page to show updates. Session state acts as a persistent memory bank that survives these reruns, storing data like scores or user inputs in a dictionary so the app remembers things across interactions, similar to a video game's save file that keeps your progress.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    I would say the patient it took to read through and work with the AI, this show walked me through a testing and debugging phase as if I was the one that created the code for the game. It also exposed me to new tools and technologies like streamlit, tools that I, as an IT major probably would never have seen so soon.
- What is one thing you would do differently next time you work with AI on a coding task?
  I would work with the AI for understanding of what I am doing, not just a way out.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project opened my eyes to the simple errors AI generated code can have. Yes, AI can build you a whole app, but it defintely still needs a hand to hold and steer it towards the right direction. Not to mention the need for human eyes to test and debug any errors/ bugs, it is not yet capabile to be autonomous. 
