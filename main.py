import os
import openai


openai.api_key = os.environ['openai_key']

import interactions

wozniak = interactions.Client(
    token= os.environ['discord_key'])



async def on_ready():
  print("Ready!")

@wozniak.command(name="my_first_command",
                 description="This is the first command I made!")
async def my_first_command(ctx: interactions.CommandContext):
    await ctx.send("Hi there!")

@wozniak.command(name="ping",
                 description="ping!")
async def ping(ctx: interactions.CommandContext):
    await ctx.send("pong!")


@wozniak.command(
    name="ask_woz",
    description="what do you want to code?",
    options=[
        interactions.Option(
            name="input",
            description="what do you want to code?",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def ask_woz(ctx: interactions.CommandContext, input: str):
  output = ""
  
  print("User input: " + input)

  await ctx.send("Working...")
  

  response = openai.Completion.create(
    engine="text-davinci-002",
    prompt= input,
    temperature=0,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )

  output = str(response['choices'][0]['text'])

  print("OpenAI Response: " + output)
  
  await ctx.edit(output)


wozniak.start()

