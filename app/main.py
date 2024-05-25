#description = 'a travel assistant that search hotels according to the criteria provided by the user'

import streamlit as st
import pandas as pd 
from evaluator import MistralEvaluator
from chatbot_evaluator import *

def main():
    st.markdown("# 💡 Genies - LLM Quality Analysis ")
    st.markdown("### Project Description:")
    project_description = st.text_input("📝 Please provide a brief description of your LLm Based application:")
    
   # Toggle for user's dialogs
    on = st.toggle("I have user's dialogs")
    if on:
        uploaded_file = st.file_uploader("Upload your dialogs (CSV)", key="file_uploader")

        # If a file is uploaded, read and display its contents
        if uploaded_file is not None:
            # Read the CSV file into a DataFrame
            combined_dialogues = pd.read_csv(uploaded_file, index_col=0)

            # Assuming metrics_text is defined somewhere
            metrics_text = "Some metrics text or configuration"  # Update this as per your requirement

            # Evaluate the chatbot
            results = evaluate_chatbot(combined_dialogues, metrics_text)
            
            # Display the results in Streamlit
            st.markdown("### Evaluation Results")
            st.dataframe(results.head(5))

if __name__ == "__main__":
    main()