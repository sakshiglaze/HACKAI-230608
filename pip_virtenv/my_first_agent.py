from uagents import Agent, Context

alice = Agent(name="alice", seed="alice recovery phase")

@alice.on_interval(period=2.0)
async def saay_hello(ctx: Context):
    ctx.logger.info(f'Hello, my name is {ctx.name}')

if __name__ =="__main__":
    alice.run()   