import streamlit as st
from connect import load_fragrances

st.title("Fragrance Collection")

df = load_fragrances()

for i, row in df.iterrows():
    st.subheader(f"{row['name']} ({row['concentration']}) by {row['brand']}")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"Notes: {row['notes']}")
        st.write(f"Size: {row['size_ml']} ml")
        st.write(f"Price: ${row['retail_price']}")
        st.write(f"Season: {row['season']}")
    
    with col2:
        st.image(row['image_path'], width=200)
    
    st.markdown("---")