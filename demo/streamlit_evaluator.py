import streamlit as st

def main():
    st.markdown("# 💡 Genies - LLM Quality Analysis ")
    st.markdown("### Choose the Mistral Model to use as LLM Judge:")
    
    models = ["🟢 mistral-small-latest", "🔵 mistral-medium-latest", "🔴 mistral-large-latest"]
    selected_model = st.radio("You can change the Mistral model:", models)
    # todo : give the selected model as parameter to helper function Mistral 
    st.markdown("### Project Description:")
    user_text = st.text_input("📝 Please provide a brief description of your LLm Based application:")
    
    if user_text:
        st.markdown("### 📊 Generated Metrics")
        st.markdown("Based on your description, our evaluator suggests the following metrics. Which ones would you like to use?")
        # todo : replace options by generated metrics
        options = ["✅ Precision", "⚠️ Toxicity", "🤖 Hallucination"]
        
        selected_metrics = []
        for option in options:
            if st.checkbox(option):
                selected_metrics.append(option)
        
        if selected_metrics:
            other_metrics = st.text_input("💡 Would you like to add other metrics?: ")
            if other_metrics:
                selected_metrics.append(other_metrics)
            

if __name__ == "__main__":
    main()