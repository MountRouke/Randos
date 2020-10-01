from gym_derk.envs import DerkEnv, ConnectionLostError
from argparse import ArgumentParser
import logging
logging.basicConfig(level = logging.INFO)

def main(env_args={ "mode": "server" }):
  env = DerkEnv(**env_args)

  while True:
    observation_n = env.reset()
    while True:
      action_n = [env.action_space.sample() for i in range(env.n_agents)]
      observation_n, reward_n, done_n, info = env.step(action_n)
      if all(done_n):
        print("Episode finished")
        break
  env.close()

if __name__ == "__main__":
  parser = ArgumentParser()
  parser.add_argument("-s", "--server", action="store_true", dest="server", default=False)
  parser.add_argument("-c", "--connected", action="store_true", dest="connected", default=False)
  args = parser.parse_args()
  while True:
    try: main({ 'mode': "server" if args.server else ("connected" if args.connected else None) })
    except ConnectionLostError: print('Connection lost')
    if not args.server:
      break
