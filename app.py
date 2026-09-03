import streamlit as st,requests,pandas as pd
API="http://127.0.0.1:8000"
st.set_page_config(page_title="AI Lead Generation Agent",layout="wide")
st.title("AI Lead Generation Agent")
with st.form("lead"):
    name=st.text_input("Name"); email=st.text_input("Email")
    company=st.text_input("Company"); industry=st.text_input("Industry")
    budget=st.number_input("Budget",min_value=0.0,step=500.0)
    requirement=st.text_area("Customer Requirement")
    engagement=st.slider("Engagement",0,30,10)
    ok=st.form_submit_button("Analyze Lead")
if ok:
    try:
        payload={"name":name,"email":email,"company":company,"industry":industry,"budget":budget,"requirement":requirement,"engagement":engagement}
        r=requests.post(API+"/leads",json=payload,timeout=10); d=r.json()
        st.success(f'{d["category"]} Lead - Score {d["score"]}/100')
        st.text_area("Personalized AI Message",d["ai_message"],height=220)
    except Exception as ex: st.error("Start FastAPI first: "+str(ex))
st.divider(); st.subheader("Saved Leads")
try:
    r=requests.get(API+"/leads",timeout=5)
    if r.ok: st.dataframe(pd.DataFrame(r.json()),use_container_width=True)
except: st.info("API is not running.")
