# Introduction

This repo contains the outline and demos for my brief talk "tools for constructing software."

My goal with this talk is to get us talking about our workflow, honestly, what we actually do. And by sharing and comparing notes, we'll gain new perspective, maybe some new ideas, or at minimum feel better about ourselves and our personal failings. 

# Outline

- general theme: strong programmers don't need tools--but the rest of us do, so ignore the strong programmers
  - Rob Pike: "Syntax highlighting is juvenile. When I was a child, I was taught arithmetic using colored rods. I grew up and today I use monochromatic numerals" - Rob Pike is very, very wrong - but correct in a vague, general sense 
- code-and-fix
- syntax highlighting
- linting
- logging
- tests
- REPL - vanilla REPL
- debugger - REPL in your text editor
- not discussed: strong type system. QED
- not discussed: without type safety, precondition checks (design by contract)
- not discussed: design techniques? How does one decide what to build?
- not discussed: GitHub Copilot
- not discussed: 'notebooks'

# I don't know Python - here are searches I have run while doing recent Python work

```
python check if file exists
python write string to file
python multiline string
python change directory
python create object
python create dictionary
python requirements.txt
python open file stream
python read file into a string
python if statement
python check if folder exists
python logging to console
python if else if
python set logging level
python test example
python return statement
python import local file same directory
python convert to string
```

# Detailed outline

- I'm Peter, I'm here to talk about building software, focusing on tools.
  - not covered: design (e.g. how to break down problems)
  - Good, unique perspective: constantly shifting technology stacks, lots of experience, not a naturally strong programmer, and I keep my ear to the streets
  - Not an expert (see python searches)
  - Set expectations: I have some good tips, and I will share them. I have good perspective, and I will share it. I will be very honest about my impure dev workflow.
  - Expectations for you: I seriously believe I am not the best person in the room to give perspective on any specific technique. Y'all jump in and share your experience.
  - Expectations for FP group: this is not a FP talk. This is a blue-collar programmer talk. This isn't state-of-the-art, it is state-of-the-industry
  - Takeaways: Ideally, we learn how to extract the maximum value out of each technique, and maybe even get exposed to new-to-us techniques.
- general theme: strong programmers don't need tools--but the rest of us do
  - I am not a naturally strong programmer - I make lots of easy mistakes and thus rely on every available tool to help. I am effective by mastering the tools and augmenting my weakness
  - Quote from a strong programmer: Rob Pike: "Syntax highlighting is juvenile. When I was a child, I was taught arithmetic using colored rods. I grew up and today I use monochromatic numerals" - Rob Pike is very, very wrong
  - He's totally wrong about syntax highlighting...HOWEVER...he has a valuable point. **What is his point? Good-faith explanation?**
  - HYPOTHESIS: strong programmers do not need tools like the rest of us
  - however, the rest of us can get very far with tools
  - **thus, lean on every tool possible**
  - **GROUP: when was the last time you programmed completely freehand--without syntax highlighting?**
  - **GROUP: do you have war stories about strong programmers you've worked with (or otherwise)? Follow-up: can you program like they do?**
- programmers at rest: code-and-fix
  - this is the bare minimum mental energy required to solve a problem
  - **GROUP: what major advantage does this have? cognitive load/survival**
  - **GROUP: when is this approach 100% appropriate? when you're a strong enough programmer (ignoring the value of having automated tests to catch regressions)**
  - **When was the last time someone did code-and-fix style development, and why?** No debugger, no console logging, no tests.
    - my answer: ; today (2022-06-15) in python; VBA/Excel;
- syntax highlighting
  - DEMO: open file 01 in notepad, tell them to figure out what is wrong. Wait a minute. Now open the file in VS Code.
  - syntax highlighting is an easy win
  - TAKEAWAY: agree that Rob Pike is wrong
- linting, autoformatters, IDE features like navigating to library source, autodoc contet menus, autocomplete

  - linting gives you early feedback when your program is invalid. It could be a check that runs in an automated build, or the squigglies you see in your editor, or a kind of linter that runs a format-on-save if your code is valid.
  - I have grouped autoformatter tools (prettier) with linters. They're not the same, but their functionality overlaps
  - DEMO: run `node 02-linting\fizzbuzz-format-on-save.js` - note it is a working program. Now open it in the text editor. Make sure everyone sees the horror. Now add a space and save (to run prettier)
  - Linters and autoformatters are great for sanity on a team
  - **QUESTION: Where are linters most useful for you? How do they help? Do they catch bugs?**
  - **QUESTION: Why don't you use a linter everywhere? There is a real, valid answer**

- logging
  - logging is defined here as: diagnostic logs in text form, either to the console, to a text file, or to a centralized Enterprise Log Aggregation System
  - DEMO: open `03-logging\fizzbuzz.py` and run `python 03-logging\fizzbuzz.py`
    - NOTE: to simulate an environment where you can't see the results immediately, I added logging
    - **GROUP: criticize these logs. Too noisy, definitely, right? What could you log differently? What can't you log sometimes (real data, pws)?**
    - **GROUP: how do logs help you? Do you leave the logs in after completing? Or do you follow the unix philosophy of zero-output == perfect run?**
- tests
  - DEMO: open `04-tests\main.py`, `04-tests\fizzbuzz.py` and run `pytest .\fizzbuzz.py -v` from terminal
  - **GROUP: Are these tests okay? Do your best to criticize them. I can handle it.**
  - **GROUP: May someone explain why tests are useful? I'll grade your response on the scale between D+ and F-**
  - **GROUP: May someone give a good-faith answer as to what it costs to write tests? Hint: strong programmers**
  - **GROUP: when are tests useful for you? When are tests definitely the wrong thing to do?**
- REPL - vanilla REPL
  - really important: I wrote a bug, roughly 4 times, in fizzbuzz, before finding the bug via the REPL
  - DEMO: `python -i` and run through the experience - follow `05-repl\repl-session.md` (open this in Markdown Preview)
  - **GROUP: Who builds software in the REPL? Please describe the experience. What do you like about a REPL? How do you 'productionalize' your REPL code?**
- debugger
  - my personal favorite crutch to lean on
  - DEMO: open `06-debugger\fizzbuzz.py` and step through the code
    - note that we step through one at a time
    - note the locals window
    - note the quickwatch
    - note the `Debug Console` in vscode - AKA an Immediate Window, AKA a REPL with context
  - **GROUP: tell me how the mindlessly running the debugger can be a trap. Talk about what to do if you find yourself mindlessly stepping through in the debugger. Take a literal walk?**
  - **GROUP: talk up how the debugger will NOT rot your mind.**
- conclusion: lean on every tool available to you; add them all to your toolbox
  - **GROUP: what is your takeaway, if anything? What new perspective do you have?**
- not discussed: strong type system. QED
- not discussed: without type safety, precondition checks (design by contract)
- not discussed: design techniques? How do you decide what to build?
