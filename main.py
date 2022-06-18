import interactions

wozniak = interactions.Client(
    token=
    "OTg2NTIxMzE1MjIzNjY2Njg4.G_w8qH.f6BGlrqBOs_CveJHcG_AysV1eTtsKNVzQV-nr0")

import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = "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"


@wozniak.command(name="my_first_command",
                 description="This is the first command I made!")
async def my_first_command(ctx: interactions.CommandContext):
    await ctx.send("Hi there!")


@wozniak.command(
    name="code4me",
    description="what do you want to code?",
    options=[
        interactions.Option(
            name="text",
            description="what do you want to code?",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def getCode(ctx: interactions.CommandContext, text: str):

    response = openai.Completion.create(engine="text-davinci-002",
                                        prompt="Write a story based on: " +
                                        text,
                                        temperature=0,
                                        max_tokens=256,
                                        top_p=1.0,
                                        frequency_penalty=0.0,
                                        presence_penalty=0.0)

    outputResponse = str(response['choices'][0]['text'])
    await ctx.send("works")
    await ctx.send(outputResponse)


wozniak.start()
