from Blackjack import BlackjackEnv
import Strategies

bj_env = BlackjackEnv()
STRATEGIES = {
    "1": Strategies.basic,
    "2": Strategies.rand,
}
WIN = True
LOSS = False


def generate_episode_from_limit_stochastic(
        env, strategy=Strategies.basic):
    episode = []
    state = env.reset()
    while True:
        action = strategy(state)
        next_state, reward, done, info = env.step(action)
        episode.append((state, action, reward))
        state = next_state
        if done:
            break
    return episode


def play(strategy):
    ep = generate_episode_from_limit_stochastic(
        bj_env, strategy=strategy)
    if ep[-1][-1] == 1:
        return WIN
    return LOSS


def main():
    iterations = int(input("how many games should we play?\n"))
    strat_index = input(f"\nWhat strategy should we use?"
                     f"\n[1] basic"
                     f"\n[2] random\n")
    strategy = STRATEGIES.get(strat_index, Strategies.basic)
    wins = 0
    for i in range(iterations):
        result = play(strategy)
        if result:
            wins += 1
    print(f"\n{wins} wins out of {iterations} games")


if __name__ == "__main__":
    main()
