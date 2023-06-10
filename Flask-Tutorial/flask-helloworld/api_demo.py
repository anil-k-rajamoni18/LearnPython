import openai
import requests

import os
# openai.organization = "org-NKxjP2HF5UWAdRdCev3CZ0MJ"
# openai.api_key = "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"
# models = openai.Model.list()

# #print(models)

# response = openai.Edit.create(
#   model="text-davinci-edit-001",
#   input="What day of the wek is it?",
#   instruction="Fix the spelling mistakes"
# )

# print(response.json())

print(dir(openai.Edit))