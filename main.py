import streamlit as st
from dotenv import load_dotenv
from ImageDownloader import *

################## DOWNLOAD THE IMAGE OF THE DAY ###########################################

load_dotenv()

api_key = os.getenv("NASA_API")

response = get_data(api_key)
datum = get_date(response)
url = get_url(response)
download_image(url, datum)
explanation = get_explaination(response)


#################################### FRONT END ###########################################

st.set_page_config(page_title="NASA IMAGE OF THE DAY", layout="centered")

st.title("NASA IMAGE OF THE DAY")
st.subheader("FEAST YOUR EYES")

image_path = os.getenv("IMAGE_PATH")
image = st.image(image_path)

st.write(explanation)