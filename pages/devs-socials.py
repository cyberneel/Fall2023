import streamlit as st

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.link_button("Neelesh Chevuri", "https://instagram.com/cyber_neel")
    
with col2:
    st.link_button("Yugarya Goyal", "https://facebook.com/yugarya.goyal")

with col3:
    st.link_button("Sameer Agarwal", "https://instagram.com/sam.eer.agarwal")

with col4:
    st.link_button("Murtaza Haque", "https://www.facebook.com/profile.php?id=100093926327175")

