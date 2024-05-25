#description = 'a travel assistant that search hotels according to the criteria provided by the user'

import streamlit as st
from evaluator import MistralEvaluator

def main():
    st.markdown("# 💡 Genies - LLM Quality Analysis ")
    st.markdown("### Project Description:")
    project_description = st.text_input("Please provide a brief description of your LLm Based application:")
    
    
    if project_description:
        mistral_evaluator = MistralEvaluator(project_description)
        st.markdown("### 📋 Metrics")
        # todo : replace options by generated metrics
        #generated_metrics = mistral_evaluator.generate_metrics()
        generated_metrics = ["Coherence",
                              "Readability",
                              "Toxicity",
                              "Hallucination", 
                              "Providing Relevant Information", 
                              "User Interaction and Engagement", 
                              "Personalization and Context Awareness",
                              "Empathy", 
                              ]
        
        selected_metrics = st.multiselect("Select metrics:", generated_metrics)
                
        if st.button("Confirm Selection"):
            if selected_metrics :
                st.markdown("### 📊 Generated dataset")
                st.markdown("Based on the selected metrics, here are some examples of generated tests")
                generated_questions = mistral_evaluator.generate_questions(selected_metrics)
                st.markdown(f"{generated_questions}")
        

if __name__ == "__main__":
    main()