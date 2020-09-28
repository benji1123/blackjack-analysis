# Blackjack Agent
This is a work in progress. Growing up, I played blackjack with my family. I didn't have a strategy and just used my instincts. A few years later, I learned about card-counting and [basic strategy](http://www.casinoguardian.co.uk/blackjack/blackjack-basic-strategy/). 
I'm interested in seeing  the performance of different blackjack strategies over hundreds of simulated games, which is what this is for.

### Blackjack
I'm using [OpenAI Gym's blackjack](https://github.com/openai/gym/blob/master/gym/envs/toy_text/blackjack.py). It doesn't support the below features, which I'll have to implement:
* double-down
* split
* specifying bet-sizes
* using a deck (currently, cards are taken from an *infinite* deck)
