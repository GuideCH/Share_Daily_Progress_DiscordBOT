# Share_Your_Daily_Progress_DiscordBOT
Bot to share your progress of anything in communities

A copy of Discord bot for conducting standups in "The Programming Hangout". But a (LOT) simpler
Take a look at https://github.com/the-programmers-hangout/standup

## Installation
```bash
# in terminal
pip install discord.py
```
Then Change Your Bot tokens in line 6

```python
tokens = 'TOKENS_HERE'
#look at line 62 for language changing
```
## for english user
Take a look at line 62 for language changing
```python
#change this line
template_msg = textwrap.dedent(template_msg)
#to
template_msg = textwrap.dedent(template_msg_eng)
```

## update your progress every day!
![alt text](https://i.imgur.com/TDRlz2F.png)

## Auto Delete & DM wrong format message!
![alt text](https://i.imgur.com/L6fZykA.png)
![alt text](https://i.imgur.com/oldHhmB.png)
