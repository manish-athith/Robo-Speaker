import pyttsx3  # Importing the text-to-speech conversion library

def robo_speaker():
    print("Welcome to Chitti Robo Speaker 2.0. Created by Manish Choudhary")

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Setting the speech speed
    engine.setProperty('volume', 1.0)  # Setting the volume level (1.0 is maximum)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Change index for male/female voice
    
  # Welcome speech
    welcome_text = "Welcome to Chitti Robo Speaker 2.0. Created by Manish Choudhary. I am ready to speak for you."
    engine.say(welcome_text)
    engine.runAndWait()
    

    while True:
        text = input("Enter what you want to speak (type 'exit' to stop): ")
        
        if text.lower() == 'exit':
            print("Exiting Chitti Robo Speaker 2.0... Goodbye!")
            engine.say("Exiting Chitti Robo Speaker 2.0... Goodbye!")
            engine.runAndWait()
            break  # Stop the loop when 'exit' is entered

        engine.say(text)  # Convert text to speech
        engine.runAndWait()  # Wait until the speech is finished before continuing

if __name__ == "__main__":
    robo_speaker()  # Call the function to start the speaker
