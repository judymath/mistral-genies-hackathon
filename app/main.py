#description = 'a travel assistant that search hotels according to the criteria provided by the user'

import streamlit as st
import pandas as pd 
from evaluator import MistralEvaluator
from chatbot_evaluator import *
import altair as alt


def main():
    st.set_page_config(
        page_title="💡 Genies - LLM Quality Analysis ",
        page_icon="💡",
        layout="wide",
        initial_sidebar_state="expanded")
    alt.themes.enable("dark")

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
            col = st.columns((4.5, 4.5), gap='medium')
            example_idx = 2
            with col[0]:
                st.markdown('#### Example')
                example = '###**Dialogue**###\n\n' + results.iloc[example_idx]['Dialogue'].replace(
                    '\n', '\n\n').replace('Human:', '**Human:**').replace(
                    'Travel Assistant:', '**Travel Assistant:**') + '\n\n###**Comment**###'
                score = results.iloc[example_idx]['Overall Satisfaction']
                comment = results.iloc[example_idx]['Comment']
                example += f'**[{score}/5]** {comment}\n\n'
                st.write(example)
            with col[1]:
                st.markdown('#### Evaluation Scores on the dataset')
                st.metric(label="Overall Satisfaction", value=round(results['Overall Satisfaction'].mean(), 1))
                st.markdown("""---""")
                st.metric(label="Understanding User Queries", value=round(results['Understanding User Queries'].mean(), 1))
                st.metric(label="Providing Relevant Information",
                          value=round(results['Providing Relevant Information'].mean(), 1))
                st.metric(label="User Interaction and Engagement",
                          value=round(results['User Interaction and Engagement'].mean(), 1))
                st.metric(label="Personalization and Context Awareness",
                          value=round(results['Personalization and Context Awareness'].mean(), 1))


if __name__ == "__main__":
    main()