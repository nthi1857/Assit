import speech_recognition as sr  # felismerni a beszédet
import playsound  # hangfájl lejátszásához
from gtts import gTTS  # google text to beszéd
import random
from time import ctime  # kap idő részleteit
import webbrowser  # nyissa meg a böngészőt
import ssl
import certifi
import time
import os  # a létrehozott audio fájlok eltávolításához
import subprocess
from PIL import Image
import pyautogui  # screenshot
import pyttsx3
import urllib.request

class person:
    name = ''

    def setName(self, name):
        self.name = name


class asis:
    name = ''

    def setName(self, name):
        self.name = name


def letezik(terms):
    for term in terms:
        if term in hang_adatok:
            return True


def engine_beszel(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer()  # inicializálja a felismerőt


# hallgassa meg a hangot, és konvertálja szöveggé:
def hanganyag_rogzites(kerdez=""):
    with sr.Microphone() as source:  # mikrofon forrásként
        if kerdez:
            engine_beszel(kerdez)
        audio = r.listen(source, phrase_time_limit=3)  # hallgassa meg a hangot forráson keresztül
        print("Kész hallgatni")
        hang_adatok = ''
        try:
            hang_adatok = r.recognize_google(audio, language="hu-HU")  # audio konvertálása szöveggé
        except sr.UnknownValueError:  # hiba: a felismerő nem érti
            engine_beszel('Nem értem')
        except sr.RequestError:
            engine_beszel('Sajnáljuk, a szolgáltatás nem működik')  # hiba: a felismerő nincs csatlakoztatva
        print(">>", hang_adatok.lower())  # kinyomtatja, amit a felhasználó mondott
        return hang_adatok.lower()

# karakterláncot kap, és készít egy hangfájlt a lejátszáshoz
def engine_beszel(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='hu')  # szöveg-beszéd (hang)
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # mentés mp3 formátumban
    playsound.playsound(audio_file)  # az audio fájl lejátszása
    print(asis_obj.name + ":", audio_string)  # kinyomtatja, amit az alkalmazás mondott
    os.remove(audio_file)  # audio fájl eltávolítása


def valasz(hang_adatok):
    # 1: üdvözlet
    if letezik(['szia', 'hi', 'hello']):
        greetings = ["Szia, segíthetek?" + person_obj.name, "Szia, mi újság?" + person_obj.name,
                     "hallgatlak" + person_obj.name, "miben segíthetek?" + person_obj.name,
                     "Szia" + person_obj.name]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        engine_beszel(greet)

    # 2: név
    if letezik(["mi a neved", "hogy hívlak", "Mondd el a neved"]):
        if person_obj.name:
            engine_beszel("mi a nevemmel")
        else:
            engine_beszel("nem tudom a nevemet. mi a neved")

    if letezik(["a nevem"]):
        person_name = hang_adatok.split("nevem")[-1].strip()
        engine_beszel("oké, emlékszem erre" + person_name)
        person_obj.setName(person_name)  # emlékszik a név személyes tárgyra

    if letezik(["a nevednek kell lennie"]):
        asis_name = hang_adatok.split("lennie")[-1].strip()
        engine_beszel("oké, emlékezni fogok arra, hogy a nevem " + asis_name)
        asis_obj.setName(asis_name)  # emlékszik a névre az asis objektumban

    # 3: üdvözlet
    if letezik(["hogy vagy", "hogy vagy ma"]):
        engine_beszel("Nagyon jól vagyok, köszönöm, hogy megkérdezte " + person_obj.name)

    # 4: idő
    if letezik(["mennyi az idő", "mondd el az időt", "mennyi az idő most"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " óra és " + minutes + " percek"
        engine_beszel(time)

    # 5: keressen a Google-on
    if letezik(["keres"]) and 'youtube' not in hang_adatok:
        keres = hang_adatok.split("keres")[-1]
        url = "https://google.com/search?q=" + keres
        webbrowser.get().open(url)
        engine_beszel("Itt találtam" + keres + "a Google-on")

    # 6: keresés a YouTube-on
    if letezik(["youtube"]):
        keres = hang_adatok.split("youtube")[-1]
        url = "https://www.youtube.com/results?search_query=" + keres
        webbrowser.get().open(url)
        engine_beszel("Itt találtam " + keres + "a Youtube-on")

    # 7: kap tőzsdei árat
    if letezik(["ára"]):
        keres = hang_adatok.split("ára")[-1]
        url = "https://google.com/search?q=" + keres
        webbrowser.get().open(url)
        engine_beszel("Itt találtam " + keres + "a Google-on")

    # 9 időjárás
    if letezik(["időjárás"]):
        keres = hang_adatok.split("időjárás")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_beszel("Ez az, amit megtaláltam a google-on")

    # 10 a kővel, papír vagy olló
    if letezik(["játszhatunk egy játékot", "játszani", "játék", "game"]):
        hang_adatok = hanganyag_rogzites("olyan játékunk van, mint a kővel, papír vagy olló. válasszon a kővel, papír vagy olló közül")
        moves = ["kővel", "papír", "olló"]

        vmove = random.choice(moves)
        jmove = hang_adatok

        engine_beszel("én választok " + vmove)
        engine_beszel("Te választasz " + jmove)
        if jmove == vmove:
            engine_beszel("a meccs döntetlen")
        elif jmove == "kővel" and vmove == "olló":
            engine_beszel("A játékos nyer")
        elif jmove == "kővel" and vmove == "papír":
            engine_beszel("Asszisztens nyer")
        elif jmove == "papír" and vmove == "kővel":
            engine_beszel("A játékos nyer")
        elif jmove == "papír" and vmove == "olló":
            engine_beszel("Asszisztens nyer")
        elif jmove == "olló" and vmove == "papír":
            engine_beszel("A játékos nyer")
        elif jmove == "olló" and vmove == "kővel":
            engine_beszel("Asszisztens nyer")

    # 13 screenshot
    if letezik(["képernyő", "screenshot"]):
        kepernyokepem = pyautogui.screenshot()
        kepernyokepem.save('D:/screen.png')

        # 14 keresni a wikipedia definícióját
    if letezik(["meghatározza"]):
        meghatarozas = hanganyag_rogzites("mi a meghatározása?")
        url = "https://hu.wikipedia.org/wiki/?search=" + meghatarozas
        webbrowser.get().open(url)
        engine_beszel("Itt találtam" + meghatarozas + "a Wikipédiából")

    if letezik(["kilépés", "viszlát", "viszontlátásra"]):
        engine_beszel("viszontlátásra")
        exit()


time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'Assist'
engine = pyttsx3.init()

while (1):
    hang_adatok = hanganyag_rogzites("Felvétel")  # megkapja a hangbemenetet
    print("Kész")
    print("Te:", hang_adatok)
    valasz(hang_adatok)  # válasz
