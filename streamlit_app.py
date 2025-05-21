import streamlit as st
import json

# Load clause rulebook
with open("clause_rules.json") as f:
    rules = json.load(f)

st.title("Synesis Clause Risk Analyzer")
st.write("Upload a contract or enter a clause below:")

clause_text = st.text_area("Enter Clause Text")

if clause_text:
    st.subheader("🧠 Clause Analysis")
    if "indemnity" in clause_text.lower():
        result = rules["Indemnity"]
    elif "confidential" in clause_text.lower():
        result = rules["Confidentiality"]
    else:
        result = {"risk_level": "Low", "rule": "No specific risk detected.", "suggestion": "Clause appears standard."}
    
    st.write(f"**Risk Level:** {result['risk_level']}")
    st.write(f"**Rule Check:** {result['rule']}")
    st.write(f"**Suggested Fix:** {result['suggestion']}")
