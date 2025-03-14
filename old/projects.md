# User Generated Data
## General web scrapping
- https://osintframework.com/
- [structured scrapping](https://webscraper.io/web-scraper-first-time-install)
- [apify, general solution](https://apify.com/)
- [reddit webscraping sub](https://www.reddit.com/r/webscraping/)

## Site Specific 
### Discord
https://github.com/Tyrrrz/DiscordChatExporter

### X
auth
- editthiscookie is used to get cookie

pkg
- [twikit: discord support, up to date, no API](https://github.com/d60/twikit?tab=readme-ov-file)
- https://github.com/Owen3H/twittxr?tab=readme-ov-file
- https://www.youtube.com/watch?v=6D6fVyFQD5A
- [tweepy: enterprise solution, need API](https://github.com/tweepy/tweepy/)
- [tweety: less function, up to date](https://github.com/mahrtayyab/tweety?tab=readme-ov-file)


Apify
### Telegram
types of chat: https://core.telegram.org/api/channel
- Individual Chats: one-on-one conversations between two Telegram users
- Group and Supergroup Chats; functions: Roles and Permissions; Pinned Messages; Mentions
- Channel
- Bots
- Voice Chats
- Discussion Groups: linked to Channels, enabling subscribers to engage in conversations related to the channel's content. 
- Folders

get app id
- https://my.telegram.org/apps
- if it shows error, use phone to register for the app
- test: 26591579, 44acd3beb9e4acdc90a778f43e58cc21

Telethon
- [doc](https://docs.telethon.dev/en/stable/basic/installation.html)
- [on entity](https://docs.telethon.dev/en/stable/concepts/entities.html)
- [on session](https://docs.telethon.dev/en/stable/concepts/sessions.html)

# Security
## Encryption

## Proxy
use shadowrocket api endpoint and setup the socks5


# Project Notes
## Stoic
### General Info


### Info about Affaan Mustafa
typical Pakistanian with his middle eastern/indian gang. need to verify his codes
- [blog](https://medium.com/@afmustafa/unveiling-market-manipulation-in-cryptocurrencies-through-sentiment-analysis-b1fc5a32ca9)

## CROY
- https://x.com/MCAssassin02/status/1877372158059622856
- 

stated goal:
- Scams & Rug Pulls: Dev wallets dumping tokens after attracting initial liquidity.
- Copycat Tokens: Quick clones of more popular meme or AI-based coins.
- Psychological Pitfalls: Fear of missing out on the next 100x gem, leading to irrational buying decisions.
- Sparse Data: Because these are micro-cap or newly migrated coins, traditional analytics on major platforms may be sparse or delayed.

## Sol Hackathon
https://www.solanaaihackathon.com/projects




# Log
format: what's done, what should be noted, what problems were encountered and how were they solved, problems/potential improvements,
### 1.9
- 3 x accounts: zhw is the official; respice_finem_c is for self use; illuvatar is for testing (can be sacrificed since it's registered with google account, which i have many)
- set up x reply scrapping using twikit (no X API needed so it's free); using username and password triggered bot detection, used cookie directly
- reply returns the top 10 just like how the app works; a discord thread shows max is 200, need to test this limit
- setting up openai
- setup telegram app id and hash

### 1.10
- bertopic. need to understand how it works

### 1.16
- don't use bertopic. Just use o1 or deepseek. Deepseek is much cheaper and performance on par. Reply summary looks very good. 


# Plan
## Any website
- [ ] one click summary current webpage and (maybe) search

## X
### X reply
- [ ] test reply limit
- [x] test emoji in text. unicode
- [o] setup openai. openai is paid.
- [x] test chatGPT o1 and deepseek. works well
- [ ] integrate a pipeline: setup database with psycopg2. setup temporary server with node. build a chrome extention at every x post that queries the server. 

### X user
- [ ] track celebrities and get relavant posts
- [ ] once reply summary is ok, do post summary too, start by analyzing those ai agents and remove shit posts
- [ ] get first posts
- [] post summary should include: big summary, recent summary, go to first tweet, summary by week/month/year





## Telegram
### Data
- [ ] start testing telegram group, seems like message limit could be a problem 
- [ ] get pined message
- [ ] get admin message
- [ ] get all message of relevance (no slash slogans, transaction notice)
- [ ] get messages about raid

### Analysis
- [ ] find potentially important story
- [ ] check if dev is active
- [ ] check if a debated topic is true (sentiment wise)

## Coin Price
- [ ] start getting coin data, use cmc first, store some meme and btc eth data to test some simple ideas: 
    - come back strength (CBS) and relative CBS, and fall velocity (FV) and relative FV. Both are measured as: first segment chart with 2 kinds of conditions: falling meme price FOLLOWING falling btc price; rising  meme price FOLLOWING rising btc price (this is come back). Hypothesis is if rCBS is low, it will keep low and rFV will be high. 

## Onchain
- [ ] wallet analysis


## Others
- [ ] think about how to search for anything. For example, posts about price movement. This could potentially require building a google like index set with llm. But the difficult part is make it real time. Maybe start by selecting a few accounts and only focus on them. 

- [ ] check for how long can those smart guys' predictions be right. 

- [ ] if you have many people who happen to know things, then you can always have your questions answered. Maybe that's how swarm should really be used. The current problem is many things require "hands on" experience and sometimes physical interactions.

- [ ] !!!find the right people!!!