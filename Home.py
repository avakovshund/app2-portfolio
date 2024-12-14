import streamlit as st
import pandas

st.set_page_config()

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=900)

with col2:
    st.title("йоу <3")
    content = """
    Hello, I am YOU! I am a chill boy and coder.\n
    I graduated with a bachelor's degree in 2022.
    I have worked already with such companies as Google, OpenAI, Meta, Coca-Cola and Sprite.\n
    So give me money."""
    st.info(content)

text1 = """
Below you can find some of the apps that I have built. Feel free to contact me!
"""
st.write(text1)

col3, col4 = st.columns(2)

data_csv = pandas.read_csv("data.csv", sep="	")

with col3:
    for index, row in data_csv[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Link]({row['url']})")

with col4:
    for index, row in data_csv[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Link]({row['url']})")