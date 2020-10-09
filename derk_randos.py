from gym_derk import DerkSession, DerkAgentServer, DerkAppInstance
import asyncio
from argparse import ArgumentParser
import logging
logging.basicConfig(level = logging.INFO)

async def run_session(env: DerkSession):
  while True:
    await env.reset()
    while not env.done:
      action_n = [env.action_space.sample() for i in range(env.n_agents)]
      await env.step(action_n)

if __name__ == "__main__":
  parser = ArgumentParser()
  parser.add_argument("-s", "--server", action="store_true", dest="server", default=False)
  parser.add_argument("-c", "--connected", action="store_true", dest="connected", default=False)
  args = parser.parse_args()
  server = DerkAgentServer(run_session, port=8789 if args.server else 8788)
  asyncio.get_event_loop().run_until_complete(server.start())
  if args.server:
    asyncio.get_event_loop().run_forever()
  else:
    app = DerkAppInstance(browser_logs=True)
    asyncio.get_event_loop().run_until_complete(app.start())
    asyncio.get_event_loop().run_until_complete(
      app.run_session(agent_hosts='dual_local' if args.connected else 'single_local')
    )
