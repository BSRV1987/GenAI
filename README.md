# GenAI
Sample project to demonstrate GenAI usecases.

This way we can have dataset presented to the model and get insights into it by capturing the response either in a database table or output it to the screen. If we capture the insights into the table it becomes easier to look for trends without having to write another logic. The best part is it can be integrated into an etl pipeline.

# Requirements

libraries:
OpenAI

API token : 
Need to be generated from openAI portal . Have to upgrade the subscription to pay as you go and top up is needed to overcome api usage limit errors

# Further Ideas where this code can be extended To: 

1. Collect logs from etl pipelines or from applications , pass the data set to the model to detect anamolies and publish the same
2. Pass data from the past and prompt model for trends in the future
3. GPT model can also be called to do code reviews via CI/CD pipeline and prompt to suggest modifications

# Output from the code published in the repo

<br>


Store 1:<br>
- Highest weekly sales were on 24/12/2010 with $85,676.09<br>
- Lowest weekly sales were on 06/01/2012 with $1,376.15<br>
- There was a significant increase in sales on 26/11/2010 with $70,158.86 due to a holiday<br>

Store 2:<br>
- Highest weekly sales were on 24/12/2010 with $59,889.32<br>
- Lowest weekly sales were on 06/01/2012 with $4,481.38<br>
- There was a significant increase in sales on 12/02/2010 with $44,682.74 due to a holiday<br>

Store 3:<br>
- Highest weekly sales were on 24/12/2010 with $28,497<br>
