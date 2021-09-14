# Monte-Carlo Learning

Monte-Carlo (MC) Learning is a fundamental RL method used to estimate value functions and discover optimal policies for unknown MDPs. The project follows the game of Blackjack using an [OpenAI Gym environment](https://gym.openai.com/envs/Blackjack-v0/). Blackjack is a popular casino card game, where the user aims to obtain cards that sum as close to, or equal to, a numerical value of `21`, without exceeding it. Naturally, the game is formulated as an episodic finite MDP. Full details of the rules of the environment are highlighted below:

The player plays against a fixed dealer, where:

- Face cards (Jack, Queen, King) have the point value of `10`
- Aces can either count as `11` or `1`, and is called 'usable' at `11`
- The game uses an infinite deck (with card replacements), preventing card tracking
- The game starts with the player and dealer having one face up and one face down card

The player has two actions, hit and stick, where:

- `STICK = 0`: keep the hand they currently have and move to dealers turn
- `HIT = 1`: request additional cards until they decide to stop

The player busts if they exceed `21` (loses). After the player sticks, the dealer reveals their facedown card, and draws until their sum is `17` or greater. If the dealer goes bust the player wins. If neither the player nor the dealer busts, the outcome (win, lose, draw) is decided by whose sum is closest to `21`.

Reward scores:

- Win = `+1`
- Draw = `0`
- Lose = `-1`

The observation of the environment is a tuple of 3 items:

- The players current sum `(0, 1, ..., 31)`
- The dealer's one showing card `(1, ..., 10)`
- An indicator that determines the player holding a usable ace `(no=0, yes=1)`

The player makes decisions based on (total of 200 states):

- Their current sum when between 12 - 21
- The dealer's one showing card (ace - 10)
- Whether the dealer has a usable ace
