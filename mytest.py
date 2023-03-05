import streamlit as st
from book import utils

st.header("TOP 50 BOOKS")

a="D:\\ML\\vscode\\Books\\artifacts\\02212023__222424\\data_transformation\\pickle_files\\popular.pkl"
#popular_df=utils.load_object('popular.pkl')
popular_df=utils.load_object(a)


titles=list(popular_df['Book-Title'].values[0:51])
texts=list(popular_df['Book-Author'].values[0:51])
img_srcs=list(popular_df['Image-URL-M'].values[0:51])

# display the cards
col1, col2, col3 = st.columns(3)
for i in range(len(img_srcs)):
    if i % 3 == 0:
        card_col = col1
    elif i % 3 == 1:
        card_col = col2
    else:
        card_col = col3

    with card_col:
        st.image(img_srcs[i], use_column_width=True,)
        st.markdown(f"<h3 style='font-size: 10px;'>{titles[i]}</h3>", unsafe_allow_html=True)
        st.write(texts[i])
