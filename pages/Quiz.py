import streamlit as st

st.set_page_config(page_title="BuzzFeed Quiz")

st.title("Dog breed that represent you!")
st.write("Take this quiz to find out which dog breed represents your personality!")
st.write("---")

answers = {}

image_1 = "Images/dog1.jpg"
image_2 = "Images/dog2.jpg"
image_3 = "Images/dog3.jpg"
image_4 = "Images/dog4.jpg"
image_5 = "Images/dog5.jpg"

image_6 = "Images/dog6.jpg"
image_7 = "Images/dog7.jpg"
image_8 = "Images/dog8.jpg"
image_9 = "Images/dog9.jpg"


image_10 = "Images/dog10.jpg"
image_11 = "Images/dog11.jpg"
image_12 = "Images/dog12.jpg"
image_13 = "Images/dog13.jpg"



#Note for the calculation part
# Golden Retriever, Labrador (Social)
# Bulldog, Basset Hound (Chill)
# Border Collie, Poodle (Smart)
# Husky, Australian Shepherd (Adventurer)


# Score 
Social = 0
Chill = 0
Smart = 0
Adventurer = 0


#Quesion 1: Radio Buttons 
st.subheader("Question 1: What is the No.1 trait you look for in a friend?")
st.image(image_1, width=300)
answers['q1'] = st.radio( #NEW
    "Choose one:",
    ("Loyal & Protective", #Social
     "Smart & Easy to teach", #Smart
     "Gentle & Patient with everyone", #Social
     "Independent & Mysterious",#Adventurer
     "Calm & Easygoing"), #Chill
    index=None,
)
st.write("---")

#Question 2: Multiselect
st.subheader("Question 2: Which of these activities you love the most?")
st.image(image_2, width=300)
answers['q2'] = st.multiselect( #NEW
    "Pick your top 3 favorite",
    ["Hiking", #Adventurer
     "Napping", #Chill
     "Learning new things", #Smart
     "Meeting new people", #Social
     "Running"], #Adventurer
    max_selections=3,
)
st.write("---")

#Question 3: Slider
st.subheader("Question 3: On a scale of 1-10, What is your daily energy level?")
st.image(image_3, width=300)
answers['q3'] = st.slider( #NEW
    "1 (Low) to 10 (Unlimited!)",  # 1-3 Chill, 4-7 Social, 7+ Adventurer
    1, 10, 5) 
st.write("---")

#Question 4: Selectbox 
st.subheader("Question 4: What's your problem-solving style?")
st.image(image_4, width=300)
answers['q4'] = st.selectbox( #NEW
    "When you face a challenge, what's your approach?", 
    ("Analyze and strategize.", #smart
     "Act immediately with energy.", #Adventurer
     "Collaborate with friends.", #Social
     "Stay calm and patient."), #Chill
    index=None,
)
st.write("---")

#Question 5: Number Input 
st.subheader("Question 5: What's your ideal group size?")
st.image(image_5, width=300)
answers['q5'] = st.number_input("What's the perfect number of friends for a night out?",  #NEW
                min_value=1, 
                max_value=20, 
                value=5, 
                step=1) #1-3 Chill, 4-8 Social, 9+ adventurer
st.write("---")

#Result calclation
if st.button('And you are.......'):
    st.balloons() #NEW
    if answers['q1'] == "Loyal & Protective":
         Social +=1
    elif answers['q1'] == "Smart & Easy to teach":
        Smart+=1
    elif answers['q1'] == "Gentle & Patient with everyone":
        Social +=1
    elif answers['q1'] ==  "Independent & Mysterious":
        Adventurer +=1
    elif answers['q1'] ==  "Calm & Easygoing":
        Chill+=1
    
    for i in range(len(answers['q2'])):
        if answers['q2'][i] == "Hiking":
            Adventurer +=1
        elif answers['q2'][i] == "Napping":
            Chill+=1
        elif answers['q2'][i] == "Learning new things":
            Smart +=1
        elif answers['q2'][i] ==  "Meeting new people":
            Social +=1
        elif answers['q2'][i] ==  "Running":
            Adventurer+=1

    if answers['q3'] <= 3:
        Chill+=1
    elif answers['q3'] > 3 and answers['q3'] <=7:
        Social+=1
    elif answers['q3'] > 7:
        Adventurer +=1
        
    if answers['q4'] == "Analyze and strategize.":
        Smart +=1
    elif answers['q4'] == "Act immediately with energy.":
        Adventurer+=1
    elif answers['q4'] == "Collaborate with friends.":
        Social+=1
    elif answers['q4'] == "Stay calm and patient.":
        Chill+=1
        
    if answers['q5'] <= 3:
        Chill+=1
    elif answers['q5'] > 3 and answers['q5'] <=8:
        Social+=1
    elif answers['q5'] > 9:
        Adventurer +=1

    score = {
        "Social": Social,  
        "Chill": Chill, 
        "Smart": Smart,
        "Adventurer": Adventurer
        }

    most_score= max(score, key=score.get)
    
    # st.write(score["Social"])
    # st.write(score["Smart"])
    # st.write(score["Chill"])
    # st.write(score["Adventurer"])
    
    if most_score == "Social":
        st.header("You are Golden Retriever & Labrador.")
        st.image(image_6)
        st.image(image_7)
    elif  most_score == "Chill":
        st.header("You are Bulldog and Basset Hound.")
        st.image(image_8)
        st.image(image_9)
    elif most_score == "Smart":
        st.header("You are order Collie and Poodle.")
        st.image(image_10)
        st.image(image_11)
    elif most_score == "Adventurer":
        st.header("You are Husky and Australian Shepherd.")
        st.image(image_12)
        st.image(image_13)
        

        
        
        
        



            