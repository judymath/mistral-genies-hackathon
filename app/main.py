#description = 'a travel assistant that search hotels according to the criteria provided by the user'

import streamlit as st
from evaluator import MistralEvaluator

def main():
    st.markdown("# 💡 Genies - LLM Quality Analysis ")
    st.markdown("### Project Description:")
    project_description = st.text_input("📝 Please provide a brief description of your LLm Based application:")
    
    if project_description:
        mistral_evaluator = MistralEvaluator(project_description)
        st.markdown("### 📊 Generated Metrics")
        st.markdown("Based on your description, our evaluator suggests the following metrics. Which ones would you like to use?")
        # todo : replace options by generated metrics
        options = mistral_evaluator.generate_metrics()
        
        selected_metrics = []
        for option in options:
            if st.checkbox(option):
                selected_metrics.append(option)
        

if __name__ == "__main__":
    main()