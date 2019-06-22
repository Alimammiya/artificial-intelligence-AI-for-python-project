import speech_recognition as sr
import os
from playsound import playsound
import datetime
import webbrowser
import random

speech = sr.Recognizer()

greeting_dict = {'hello': 'hello', 'hai': 'hai', 'hi': 'hi', 'hye': 'hye'}
open_launch_dict = {'open': 'open', 'launch': 'launch'}
google_searches_dict = {'what': 'what', 'why': 'why', 'who': 'who', 'which': 'which', 'whose': 'whose', 'where': 'where' }
social_media_dict = {'Facebook': 'https://www.facebook.com', 'Instagram': 'https://www.instagram.com',
                     'YouTube': 'https://www.youtube.com/', 'Twitter': 'https://www.twitter.com',
                     'WhatsApp': 'https://web.whatsapp.com/'}

mp3_thanktou_list = ['mp3/Aisha/thank.mp3', 'mp3/Aisha/thank2.mp3']
mp3_experience_list = ['mp3/Aisha/experience_working.mp3', 'mp3/Aisha/experience_working2.mp3',
                       'mp3/Aisha/experience_working3.mp3']
mp3_listening_problem_list = ['mp3/Aisha/plz_say_again.mp3', 'mp3/Aisha/plz_say_again2.mp3']
mp3_struggling_list = ['mp3/Aisha/struggling.mp3']
mp3_google_search = ['mp3/Aisha/Here_is_result_found.mp3', 'mp3/Aisha/Got_it.mp3']
mp3_greeting_list = ['mp3/Aisha/Yas_sir.mp3', 'mp3/Aisha/Yas_sir2.mp3']
mp3_open_launch_list = ['mp3/Aisha/open.mp3', 'mp3/Aisha/open2.mp3', 'mp3/Aisha/open3.mp3']


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if 0 <= currentH < 12:
        playsound('mp3/Aisha/morning.mp3')

    if 12 <= currentH < 18:
        playsound('mp3/Aisha/afternoon.mp3')

    if currentH >= 18 and currentH != 0:
        playsound('mp3/Aisha/evening.mp3')


greetMe()

error_occurrence = 0


def is_valid_google_search(phrase):
    if google_searches_dict.get(phrase.split(' ')[0]) == phrase.split(' ')[0]:
        return True


def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)


def read_voice_cmd():
    voice_text = ''
    print('Listening...')

    global error_occurrence

    try:
        with sr.Microphone() as source:
            audio = speech.listen(source=source, timeout=10, phrase_time_limit=5)
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:

        if error_occurrence == 0:
            play_sound(mp3_listening_problem_list)
            error_occurrence += 1
        elif error_occurrence == 1:
            play_sound(mp3_struggling_list)
            error_occurrence += 1

    except sr.RequestError:
        print('Network error.')
    except sr.WaitTimeoutError:
        if error_occurrence == 0:
            play_sound(mp3_listening_problem_list)
            error_occurrence += 1
        elif error_occurrence == 1:
            play_sound(mp3_struggling_list)
            error_occurrence += 1

    return voice_text


def is_valid_note(greet_dict, voice_note):
    for key, value in greet_dict.items():

        try:
            if value == voice_note.split(' ')[0]:
                return True

            elif key == voice_note.split(' ')[1]:
                return True

        except IndexError:
            pass

    return False


if __name__ == '__main__':

    while True:

        voice_note = read_voice_cmd()
        print('cmd : {}'.format(voice_note))

        if is_valid_note(greeting_dict, voice_note):
            print('In greeting...')
            play_sound(mp3_greeting_list)
            continue

        elif is_valid_note(open_launch_dict, voice_note):
            print('In open...')
            play_sound(mp3_open_launch_list)
            if (is_valid_note(social_media_dict, voice_note)):

                key = voice_note.split(' ')[1]
                webbrowser.open(social_media_dict.get(key))
            else:
                os.system('explorer C:\\"()"'.format(voice_note.replace('Open', '').replace('launch', '')))
            continue
        elif is_valid_google_search(voice_note):
            print('in google search...')
            play_sound(mp3_google_search)
            webbrowser.open('https://www.google.co.in/search?q={}'.format(voice_note))
            continue
        elif 'thank you' in voice_note:
            play_sound(mp3_thanktou_list)
            continue
        elif 'experience' in voice_note:
            play_sound(mp3_experience_list)
            continue

        elif 'how are you' in voice_note:
            playsound('mp3/Aisha/how_r_u.mp3')
        elif 'fine' in voice_note:
            playsound('mp3/Aisha/ok.mp3')
        elif 'about yourself' in voice_note:
            playsound('mp3/Aisha/about_Yourself.mp3')
        elif 'HOD of IT branch' in voice_note:
            playsound('mp3/Aisha/H.O.D.mp3')
        elif 'favourite cricketer' in voice_note:
            playsound('mp3/Aisha/cricketer.mp3')
        elif 'favourite poem' in voice_note:
            playsound('mp3/Aisha/favourate_poem.mp3')
        elif 'problem' in voice_note:
            playsound('mp3/Aisha/problem_Aisha.mp3')
        elif 'doing' in voice_note:
            playsound('mp3/Aisha/how_are_you_doing.mp3')

        elif 'goodbye' in voice_note or 'by' in voice_note or 'stop' in voice_note:
            playsound('mp3/Aisha/bye.mp3')
            break
        playsound('mp3/Aisha/next.mp3')
