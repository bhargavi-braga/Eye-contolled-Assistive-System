import base64
import streamlit as st
from st_clickable_images import clickable_images
import os
import pyttsx3
from playsound import playsound
import news
# for playing note.wav file
##########################

engine = pyttsx3.init()
st.title('Mouse Cursor Control with Eye Ball ')
######################options
lan = st.sidebar.radio("Language",["English","Hindi","Tamil","Malayalam"])

images = []
for file in [os.path.join('img','news_img.jpg'), 
             os.path.join('img','water.png'),
             os.path.join('img','hungry.png'),
             os.path.join('img','loo.png'),
             os.path.join('img','tv.png'),
             os.path.join('img','sleepy.png'),
             os.path.join('img','blanket.png')]:
    with open(file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
        images.append(f"data:image/jpeg;base64,{encoded}")

clicked = clickable_images(
    images,
    titles=[f"Image #{str(i)}" for i in range(len(images))],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "width": "150px","height": "200px"},
)
print(clicked)
st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")
if clicked == 0:
    news_headlines  = news.get_news()
    engine.say(news_headlines)
    engine.runAndWait()  
elif clicked == 1:
    if lan == "English":
        engine.say("I WANT WATER")
        engine.runAndWait()
    elif lan == "Hindi":
        playsound(os.path.join('hindi','hwater.mp3'))
    elif lan == "Tamil":
        playsound(os.path.join('tamil','water.mp3'))
    elif lan == "Malayalam":
        playsound(os.path.join('malayalam','water.mp3')) 
elif clicked == 2:
    if lan == "English":
        engine.say("I'm Hungry")
        engine.runAndWait()
    elif lan == "Hindi":
        playsound(os.path.join('hindi','hfood.mp3'))
    elif lan == "Tamil":
        playsound(os.path.join('tamil','food.mp3'))
    elif lan == "Malayalam":
        playsound(os.path.join('malayalam','food.mp3')) 
elif clicked == 3:
    if lan == "English":
        engine.say("I need to use the loo")
        engine.runAndWait()
    elif lan == "Hindi":
        playsound(os.path.join('hindi','hloo.mp3'))
    elif lan == "Tamil":
        playsound(os.path.join('tamil','loo.mp3'))
    elif lan == "Malayalam":
        playsound(os.path.join('malayalam','loo.mp3'))
elif clicked == 4:
    if lan == "English":
        engine.say("I want to see tv")
        engine.runAndWait()
    elif lan == "Hindi":
        playsound(os.path.join('hindi','htv.mp3'))
    elif lan == "Tamil":
        playsound(os.path.join('tamil','tv.mp3'))
    elif lan == "Malayalam":
        playsound(os.path.join('malayalam','tv.mp3'))
elif clicked == 5:
    if lan == "English":
        engine.say("Switch the bed lights on. I'm sleepy.")
        engine.runAndWait()
    elif lan == "Hindi":
        playsound(os.path.join('hindi','hbed.mp3'))
    elif lan == "Tamil":
        playsound(os.path.join('tamil','sleep.mp3'))
    elif lan == "Malayalam":
        playsound(os.path.join('malayalam','sleep.mp3'))  
elif clicked == 6:
    if lan == "English":
        engine.say("I need a blanket. I'm feeling cold.")
        engine.runAndWait()
    elif lan == "Hindi":
        playsound(os.path.join('hindi','hcold.mp3'))
    elif lan == "Tamil":
        playsound(os.path.join('tamil','cold.mp3'))
    elif lan == "Malayalam":
        playsound(os.path.join('malayalam','cold.mp3'))
else:
    pass