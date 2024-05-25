import json
import pandas as pd
from helpers import mistral




def create_metrics_schema(metrics_text):
    # Split the input string by commas to get individual metrics
    metrics = [metric.strip() for metric in metrics_text.split(',')]
    
    # Initialize the schema dictionary
    schema = {
        "type": "object",
        "properties": {},
        "required": []
    }
    schema["properties"]['Comment'] = {'type': 'str'}
    # Add each metric to the schema
    for metric in metrics:
        schema["properties"][metric] = {"type": "float"}
        schema["required"].append(metric)
    
    
    return schema

def evaluate_chatbot(combined_dialogues, metrics_text):
    results=[]
    metrics_json_schema = create_metrics_schema(metrics_text)

    metrics_text = """Understanding User Queries, Providing Relevant Information, User Interaction and Engagement, 
    Personalization and Context Awareness, Overall Satisfaction"""

    for i in range(1):
        chat=combined_dialogues.iloc[i,1]
        prompt = f"""
        You are a quality assurance specialist evaluating AI assistants. 
        Your goal is to assess the user's level of satisfaction with the chat based on the following metrics:
        {metrics_text}. For each criteria among these criterias {metrics_text} please provide the score between 0 and 5 where 5 is the best score. 
        Here is chat:
        {chat}
        Return json format with the following JSON schema where metric is one of the metrics in the {metrics_text} list: 

        {metrics_json_schema}
        """
        print(prompt)
        response = mistral(prompt, model= 'mistral-large-latest', is_json=True)
        results.append(response)
    
    results_df=pd.DataFrame([eval(i) for i in results])

    return results_df






