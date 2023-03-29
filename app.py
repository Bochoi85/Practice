import streamlit as st
view = [100,150,30]
st.write('# Youtube view :smile:')
st.write('## Raw')
view 
st.write('## Bar Chart')
st.bar_chart(view)
import pandas as pd
sview = pd.Series(view)
sview
import streamlit as st
st.markdown('Streamlit is **_really_ cool**.')
st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")
