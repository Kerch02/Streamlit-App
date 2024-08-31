import streamlit as st
import matplotlib.pyplot as plt

st.markdown(
    """
    <style>
    .stApp {
        background-color: #1E2A5E;
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5); 
        border-radius: 5px; 
    }
    h1, h2, h3, h4, h5, h6, p, label, .st-bq {
        color: white;
    }
    .stSelectbox>div>div>div>div:first-child {
        background-color: white !important;
        color: black !important;
    }
    .stSelectbox div[data-baseweb="select"]>div {
        background-color: white !important;
    }
    .stSelectbox div[data-baseweb="select"]>div>div {
        color: black !important;
    }
    .stSelectbox div[data-baseweb="select"]>div>div[aria-selected="true"] {
        background-color: #1E2A5E !important;
        color: white !important;
    }
    .custom-divider {
        border-top: 2px solid white; 
        margin: 10px 0;  
    }
    .circle-img {
        border-radius: 50%;
        width: 100px;
        height: 100px;
        object-fit: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Creating a header with the image and title side by side using Streamlit columns
col1, col2 = st.columns([3, 1])

with col1:
    st.title("👋Hi, I'm Kerch B. Cabo")
with col2:
    st.image('me.jpg', width=100, use_column_width=False)  # Use Streamlit's image method for better handling

st.write("""
Hello! I'm **Kerch B. Cabo**, a 21-year-old student from **Cebu Institute of Technology - University**.
I'm passionate about technology and design, and I'm excited to share my journey with you.
""")

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# Favorite Colors
st.subheader("🎨Favorite Color")
st.write("""
My favorite color is any shades of **Blue**. I find it calming and this inspires my creativity.
""")
st.color_picker('Choose a color you like', '#0000FF')

# About Me
st.header("🧑🏻About Me")

# Age Slider
age = st.slider('My age', 18, 30, 21)  # Default age is 21
st.write(f"My name is **Kerch B. Cabo** and I’m currently {age} years old, studying at **Cebu Institute of Technology - University**. "
         "I'm a BSIT-4 student and have a passion for designing.")

# Hobbies Pie Chart
st.header("🏐My Hobbies")
st.write("Here’s a visual representation of how I spend my leisure time:")

# Data for the pie chart
hobbies = ['Volleyball', 'Valorant', 'Minecraft']
hours_spent = [30, 40, 30]  # Example data

# Custom colors for the pie chart
colors = ['#6EACDA','#03346E','#021526'] 

# Adjusting the size of the pie chart
fig, ax = plt.subplots(figsize=(2, 2))  # 6x6 inches

# Set the background color of the figure
fig.patch.set_facecolor('#1E2A5E')

# Plotting the pie chart with custom colors and custom text properties
ax.pie(hours_spent, labels=hobbies, autopct='%1.1f%%', startangle=90, colors=colors, 
       textprops={'fontsize': 10, 'color': 'white'})  # Customize fontsize and color here
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the pie chart in Streamlit
st.pyplot(fig)

# Education with dropdown
st.header("🎓Education")
education_level = st.selectbox("Select your education level:", ["Elementary", "Secondary", "College"])

if education_level == "Elementary":
    st.write('<p style="color:white;">- Tabunoc Central School</p>', unsafe_allow_html=True)
elif education_level == "Secondary":
    st.write('<p style="color:white;">- Talisay City National High School</p>', unsafe_allow_html=True)
elif education_level == "College":
    st.write('<p style="color:white;">- <b>Cebu Institute of Technology - University</b></p>', unsafe_allow_html=True)
    st.write('<p style="color:white;">  - Bachelor of Science in Information Technology</p>', unsafe_allow_html=True)

# Contact
st.header("✉️Get in Touch")
st.write("Feel free to reach out to me through the form below.")

st.write("Facebook 💙: Kerch Cabo")
st.write("Instagram 🩷: kerchester_")
st.write("Tiktok ❤️: krchcb31")

name = st.text_input("Name")    
message = st.text_area("Message")

if st.button("Send"):
    st.write(f"Thank you, {name}! Your message has been sent.")
