# Assit - virtual assistant project in python
This application is used to assist users to use features such as search, weather, time viewing,... with voice assistance. This application only using the Hungarian language. To be able to run the program, you need to install the following software and modules:
- Python 2.7+
- Python Modules:
  - SpeechRecognition
    - pip install SpeechRecognition
  - playsound
    - pip install playsound
  - gTTS
    - pip install gTTS
  - Pillow
    - pip install Pillow
  - PyAutoGUI
    - pip install PyAutoGUI
  - pyttsx3
    - pip install pyttsx3
  - PyAudio
    - pip install PyAudio

Main features and usage:
1. Greetings
2. Ask the assistant's name and make the assistant remember your name
3. Ask Time: Say "mennyi az idő" or "mondd el az időt" or "mennyi az idő most.
4. Search Google or Youtube:
  - Say "keres" + thing you want to search, google result will open on your default browser.
  - Say "youtube" + thing you want to search, youtube result will open on your default browser.
5. Get stock price: Say "ára" + stock price you want to see
6. Weather: Say "időjárás", the result will open on your default browser.
7. Play game stone, paper or scissors: Just say "játszhatunk egy játékot" or "játszani"or "játék" or "game" to play.
8. Screenshot: Say "képernyő" or "screenshot", file will save at "D:/screen.png"
9. Search for Wikipedia definition: Say "meghatározza", the assistant will ask, after that say what thing you want to define. The result will open on your default browser.
10. To stop using, Say "kilépés" or "viszlát" or "viszontlátásra".
