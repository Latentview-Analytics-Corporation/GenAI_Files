# libraries
import openai
import pandas as pd

def askGPT(text):
    """ Define api key """
    openai.api_key = "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"

    # set response parameters
    response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = text,
            temperature = 0.6,
            max_tokens = 300,
        )

    return print(response.choices[0].text)

table = pd.read_csv("D:/GenAI/data/test_NBA.csv")
table = table.iloc[0]
csv_as_str = table.to_csv()

def main():
    """ Run GPT prompt"""
    print('***********')
    prompt = ("Think of yourself as a marketing expert. Based on this data what is the next best product, next best action, positive causality and negative causality?" + csv_as_str)
    askGPT(prompt)

main()

"""
Prompts 
Summarise this table \n
Tell most and least significant feature in this table \n
Tell the top 2 most and least significant features in this table \n
What should be done and should not be done from this table \n
What should be done and should not be done for this data \n
For this customer segment, what is the next best product, next best action, positive causality and negative causality \n
From a marketing perspective, what is the best thing that can be done for this data?


Negative
Frame the positive causality as a sentence that should be done and negative causality as a sentence that should not be done

"""