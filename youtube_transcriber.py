import streamlit as st
import youtube_dl

# Define ydl_opts if needed
ydl_opts = {}

@st.cache
def transcribe_from_link(link, categories: bool):
    _id = link.strip()

    def get_vid(_id):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(_id)

def main():
    # Custom CSS for RTL layout
    rtl_style = """
        <style>            
            body {
                direction: rtl;
                text-align: left;
                font-family: "Arial", sans-serif;
            }
            .stApp {
                background-image: url('https://up6.cc/2024/02/170887253131271.jpg'); /* Add your image URL */
                background-attachment: fixed;
                background-size: cover;
                background-position: center;
                direction: rtl;
                text-align: center;
            }
        </style>
    """

    st.markdown(rtl_style, unsafe_allow_html=True)
    
    img2 = "https://up6.cc/2024/02/170887061117042.png"
    st.image(img2)
    
    
    link = 'https://www.youtube.com/watch?v=-zF3a5BVEvc&feature=youtu.be'

    if link:
        
        st.video(link)

    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            img = "https://up6.cc/2024/02/170887225454832.jpg"
            st.image(img, caption="عدد السيارارت ", use_column_width=True)
        with right_column:
            img1 = "https://up6.cc/2024/02/170887225456083.jpg"
            st.image(img1, caption="عدد الأشخاص", use_column_width=False)

if __name__ == "__main__":
    main()
