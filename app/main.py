import streamlit as st
from evaluator import MistralEvaluator

def main():
    st.markdown("# Genies - LLM Quality Analysis ")
    st.markdown("### 📝 Project Description:")
    project_description = st.text_input(" Please provide a brief description of your LLm Based application:")
    
    if project_description:
        mistral_evaluator = MistralEvaluator(project_description)
        # Toggle for user's dialogs
        on = st.toggle("📂 I have my own tests")
        if on:
            uploaded_file = st.file_uploader("📤 Upload your dataset(CSV)", key="file_uploader")
        else:
            st.markdown("### 📈 Metrics")
            # todo : replace options by generated metrics
            # generated_metrics = mistral_evaluator.generate_metrics()
            predefined_metrics = [
                "Grammatical Accuracy",
                "Toxicity",
                "Hallucination",  
                "Coherence", 
                "Personalization",
                "Sensitive Information", 
            ]
            
            selected_metrics = st.multiselect("Select metrics:", predefined_metrics)
            # Allow user to add custom metrics
            custom_metric = st.text_input("You can add a custom metric:")
            if custom_metric and custom_metric not in selected_metrics:
                selected_metrics.append(custom_metric)
            
            # Allow user to specify the number of generated tests
            num_tests = st.number_input("Specify the number of generated user inputs:", min_value=1, max_value=100, value=3)
            
            if st.button("✔️ Confirm Selection"):
                if selected_metrics:
                    st.markdown("### 📊 Generated Dataset")
                    st.markdown("Based on the selected metrics, here are some examples of generated user inputs")
                    generated_questions = mistral_evaluator.generate_questions(selected_metrics, num_tests)
                    st.markdown(f"{generated_questions}")

if __name__ == "__main__":
    main()