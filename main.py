from gym_derk.envs import DerkEnv, ConnectionLostError
from argparse import ArgumentParser
import logging
logging.basicConfig(level = logging.INFO)

parser = ArgumentParser()
parser.add_argument("-s", "--server", action="store_true", dest="server", default=False)
args = parser.parse_args()

env = DerkEnv(
  mode="server" if args.server else None
)

while True:
  try:
    observation_n = env.reset()
    while True:
      # env.render()
      action_n = [env.action_space.sample() for i in range(env.n_agents)]
      observation_n, reward_n, done_n, info = env.step(action_n)
      if all(done_n):
        print("Episode finished")
        break
  except ConnectionLostError:
    print('Episode reset')
env.close()
