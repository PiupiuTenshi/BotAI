import pvporcupine
import time
from pvrecorder import PvRecorder
import speech_recognition as sr
import pyttsx3
import ollama
import webbrowser
import os
import winsound
from datetime import datetime
from langdetect import detect
from AppOpener import open as openApp
import multiprocessing
from gif_player import show_gif
import sys

# Setting 
#! Notes: fill your api key, ai_model = gemma2:2b (default), name_en (null)
# https://console.picovoice.ai/ link to access API key free
ACCESS_KEY = "" 
AI_MODEL = "gemma2:2b"
NAME_EN = "Mahiru" 

# Setting voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice_en_id = None
voice_vn_id = None

for v in voices:
    langs = str(v.languages).lower()
    name = v.name.lower()
    if voice_en_id is None and 'en' in langs:
        voice_en_id = v.id
    if voice_vn_id is None and ('vi' in langs or 'vietnam' in name):
        voice_vn_id = v.id

def BotSpeak(text, lang="vi"):
    print(f"Bot ({lang}): {text}")
    try:
        engine.stop()
        if lang == "en" and voice_en_id:
            engine.setProperty('voice', voice_en_id)
        elif voice_vn_id:
            engine.setProperty('voice', voice_vn_id)
        engine.say(text)
        engine.runAndWait()
    except:
        pass 
    
def ResourcePath(relative_path):
    try:
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".") 
    return os.path.join(base_path, relative_path)

# File model if u want to individual assistant 
# https://console.picovoice.ai/ find wake words
# NAME_MODEL = ResourcePath("Ma-hee-roo_en_windows_v4_0_0.ppn") 

def ChatToOllama(prompt, lang="vi"):
    system_instruction = (
        "You are a helpful assistant named Mahiru. "
        "Reply in the same language as the user (English or Vietnamese). "
        "Keep answers short, concise, and friendly."
    )
    try:
        response = ollama.chat(model=AI_MODEL, messages=[
            {'role': 'system', 'content': system_instruction},
            {'role': 'user', 'content': prompt},
        ])
        return response['message']['content']
    except:
        return "Xin lỗi, tôi bị mất kết nối với não bộ."

def ProcessCode(text):
    text = text.lower()
    try:
        lang_code = detect(text)
    except:
        lang_code = 'vi'

    cmd_youtube = ["mở youtube", "open youtube"]
    cmd_exit = ["tắt máy", "thoát", "exit", "shutdown", "ngủ đi", "bye"]
    cmd_time = ["time", "mấy giờ", "what time"]
    cmd_open_app = ["mở ứng dụng", "open app", "khởi động", "mở phần mềm"]
    cmd_leetcode = ["mở leetcode", "open leetcode"]
    cmd_mail = ["open mail", "open email", "mở email", "mở mail"]
    cmd_gemini = ["open gemini", "open gemini", "mở gemini", "mở gemini"]
    
    if any(word in text for word in cmd_youtube):
        msg = "Đang mở YouTube" if lang_code == 'vi' else "Opening YouTube"
        BotSpeak(msg, lang_code)
        webbrowser.open("https://youtube.com")
        
    elif any(word in text for word in cmd_leetcode):
        msg = "Đang mở Leetcode" if lang_code == 'vi' else "Opening Leetcode"
        BotSpeak(msg, lang_code)
        webbrowser.open("https://leetcode.com")
        
    elif any(word in text for word in cmd_mail):
        msg = "Đang mở Mail" if lang_code == 'vi' else "Opening Mail"
        BotSpeak(msg, lang_code)
        webbrowser.open("https://mail.google.com/mail")
    
    elif any(word in text for word in cmd_gemini):
        msg = "Đang mở gemini" if lang_code == 'vi' else "Opening gemini"
        BotSpeak(msg, lang_code)
        webbrowser.open("https://gemini.google.com/app?hl=vi")

    elif any(word in text for word in cmd_time):
        now = datetime.now().strftime("%H:%M")
        msg = f"Bây giờ là {now}" if lang_code == 'vi' else f"It is {now}"
        BotSpeak(msg, lang_code)
        
    elif any(word in text for word in cmd_open_app):
        nameApp = text
        for keyword in cmd_open_app:
            nameApp = nameApp.replace(keyword, "").strip()
        
        if nameApp == "":
            BotSpeak("Bạn chưa nói tên ứng dụng", lang_code)
        else:
            msg = f"Đang tìm và mở {nameApp}..." if lang_code == 'vi' else f"Opening {nameApp}..."
            BotSpeak(msg, lang_code)
            try:
                openApp(nameApp, match_closest=True, throw_error=True)
            except:
                BotSpeak("Tôi không tìm thấy ứng dụng này trên máy bạn", lang_code)

    elif any(word in text for word in cmd_exit):
        msg = "Tạm biệt chủ nhân" if lang_code == 'vi' else "Goodbye master"
        BotSpeak(msg, lang_code)
        os._exit(0)

    else:
        response = ChatToOllama(text, lang_code)
        BotSpeak(response, lang_code)

def HearCommandWhenWakeUp():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(">> Đang nghe...")
        try:
            audio = r.listen(source, timeout=4, phrase_time_limit=8)
            text = r.recognize_google(audio, language="vi-VN")
            return text
        except:
            return None

def RunProgram():
    try:
        # if u use default voice like: google, hey Siri... 
        # replace attribute keywords with attribute keyword_paths=[TEN_FILE_MODEL]
        porcupine = pvporcupine.create(access_key=ACCESS_KEY, keywords=['ok google'])
        recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
    except Exception as e:
        print(f"Lỗi khởi tạo Porcupine (Kiểm tra Key): {e}")
        return

    print(f"Bot '{NAME_EN}' đã sẵn sàng. Hãy nói '{NAME_EN}' để gọi tôi dậy.")
    # when u hear system started, your run that program oke
    BotSpeak("System started","en")
    recorder.start()

    try:
        while True:
            pcm = recorder.read()
            result = porcupine.process(pcm)

            if result >= 0:
                print(f"\n>> Đã nghe thấy gọi tên!")
                winsound.Beep(800, 200) 
                
                # add a GIF to make it appear on the right side of the screen.
                gif_path = ResourcePath("mahiru_siri.gif")
                p = multiprocessing.Process(target=show_gif, args=(gif_path, 4000))
                p.start()
                
                recorder.stop()
                time.sleep(0.5)
                command = HearCommandWhenWakeUp()
                if command:
                    print(f"User: {command}")
                    ProcessCode(command)
                else:
                    BotSpeak("Tôi không nghe rõ", "vi")
                
                print(f"\nBot đang ngủ... Gọi '{NAME_EN}' để đánh thức.")
                time.sleep(0.5)
                recorder.start() 
                
    except KeyboardInterrupt:
        recorder.stop()
    finally:
        porcupine.delete()
        recorder.delete()

if __name__ == "__main__":
    multiprocessing.freeze_support()
    RunProgram()
