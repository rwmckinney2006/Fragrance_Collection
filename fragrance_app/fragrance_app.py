import streamlit as st
import pandas as pd

st.title("Fragrance Collection")

df = pd.read_csv("fragrances.csv")
df['link_button'] = [
    "https://commodityfragrances.com/products/paper-expressive?srsltid=AfmBOop6ZXbHblcvL2M9z0f2YOuJ4CgEqBwZCdJ4A10bklb82OfwAS8a",
    "https://us.viktor-rolf.com/fragrance/spicebomb-extreme-eau-de-parfum-VKR_034.html",
    "https://www.chanel.com/us/fragrance/p/107350/bleu-de-chanel-eau-de-parfum-spray/?gclsrc=aw.ds&gad_source=1&gad_campaignid=22975835420&gclid=CjwKCAiA_orJBhBNEiwABkdmjBnqApkRseQO2bGBqZAy-He6XHdy4wZfsNVKB4D4L9mKrZmNUN9_ORoCoYQQAvD_BwE",
    "https://us.initioparfums.com/products/side-effect",
    "https://www.yslbeautyus.com/fragrance/mens-fragrances/y/y-eau-de-parfum/727YSL.html?srsltid=AfmBOopKGMBvsVPfD70k3Vpr8gItWN-wBEuSybs8nXIFSSiz1zhBk9M2",
    "https://www.olfactorynyc.com/products/custom-scent-50ml-wizard?variant=7556375871551",
    "https://www.franciskurkdjian.com/us-en/p/grand-soir-eau-de-parfum-RA122521.html?gad_source=4&gad_campaignid=21713493509&gbraid=0AAAAAoc43KHUxe1MLJSzFZQ5AImBWp3nl&gclid=Cj0KCQiAoZDJBhC0ARIsAERP-F97ytWfk7qFmnQkj4OEYrtodgWs5wj4LVY0j0pdyMdqBKUWkeN06LsaAmrCEALw_wcB",
    "https://www.aesop.com/fragrance/fresh/karst-eau-de-parfum/FR22.html",
    "https://www.goldfieldandbanks.com/products/ingenious-ginger?variant=41519740453004&country=AU&currency=AUD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&utm_source=google&utm_medium=cpc&utm_campaign=21554032959&gad_source=1&gad_campaignid=21560548307&gbraid=0AAAAAoZTwBh4fmuAe-5W8RMzx5bPGaeq0&gclid=Cj0KCQiAoZDJBhC0ARIsAERP-F_ybW8rOQIq5XguEYvJPZZRf-WvFMEAAHIStDhPT1VCzBLwlyRltoYaAmz-EALw_wcB",
    "https://www.scentsplit.com/products/imaginary-authors-o-unknown-sample-decants?variant=42839008215240",
    "https://www.mindgamesfragrance.com/products/french-defense?srsltid=AfmBOooIh3OV3HMWRFbGLA0RC5kmaQMaitaN1psYgmpZpWJ89HQiI4Pz&variant=43927351787736",
    "https://nishane.com/product/ani-x/?srsltid=AfmBOorTTJwNDYHqYPWtK2C6TBvbAoKA5ZAuq7gDfbkPOmwXpkpYxWKH"
]

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
        st.link_button("Buy Now", row['link_button'])
    st.divider()
