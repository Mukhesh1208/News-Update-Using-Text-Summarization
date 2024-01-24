import nltk
from textblob import TextBlob
from newspaper import Article
import tkinter as tk
from tkinter import ttk,messagebox
import googletrans
from gtts import gTTS 
from playsound import playsound
import os

#Languages List
languages = googletrans.LANGUAGES
language_list = list(languages.values())

#Summarizing the Text
def summarize():
    summary.delete('1.0','end')
    translate.delete('1.0','end')
    url = utext.get('1.0','end').strip()
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0','end')
    title.insert('1.0',article.title)
  
    publication.delete('1.0','end')
    publication.insert('1.0',article.publish_date)
 
    summary.delete('1.0','end')
    summary.insert('1.0',article.summary)
 
    analysis = TextBlob(article.text)
    sentiment.delete('1.0','end')
    sentiment.insert('1.0',f' Polarity: {analysis.polarity},Sentiment : {"Positive" if analysis.polarity >0 else "negative" if analysis.polarity < 0 else "neutral"}')

    title.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

#Translating Text
def Translate():
    translate.delete('1.0','end')

    try:
        for key, value in languages.items():
            if (value == combo_list.get()):
            
                from_language_key = key
        
        words = TextBlob(summary.get('1.0','end'))
        words = words.translate(from_lang='en', to=from_language_key)
        translate.insert(1.0,words)

    except Exception as e:
        messagebox.showerror("Translator", e)

#Converting Text to Speech
def Speak():

        for key, value in languages.items():
            if (value == combo_list.get()):
                to_language_key = key

        words = translate.get('1.0', 'end')
        # Converting text into a mp3 File
        obj = gTTS(text=words, slow=False, lang=to_language_key)
        obj.save('captured_voice.mp3')

        # Playing the convertedmp3 File
        playsound('D:\\IV-I Mini Project\\captured_voice.mp3')

        # Removing the mp3 File After Playing
        os.remove('D:\\IV-I Mini Project\\captured_voice.mp3')

#GUI

root = tk.Tk()
root.title("News Article Summarization")
root.geometry('1200x600')

tlable = tk.Label(root,text='Title')
tlable.pack()

title = tk.Text(root,height=1,width=140)
title.config(state='disabled',bg='#dddddd')
title.pack()

plable = tk.Label(root,text='Publishing Date')
plable.pack()

publication = tk.Text(root,height=1,width=140)
publication.config(state='disabled',bg='#dddddd')
publication.pack()

slable = tk.Label(root,text='Summary')
slable.pack()

summary = tk.Text(root,height=10,width=140)
summary.config(state='disabled',bg='#dddddd',font=("Times New Roman", 12))
summary.pack()

clable = tk.Label(root,text='Choose Language')
clable.pack()

combo_list = ttk.Combobox(root, width=12, value=language_list)
combo_list.current(94)
combo_list.pack()

xlable = tk.Label(root,text='')
xlable.pack()

translate_btn = tk.Button(root,text="Translate" ,command=Translate,bg='#4db4d6')
translate_btn.pack()

tlable = tk.Label(root,text='Translated Text')
tlable.pack()

translate = tk.Text(root,height=12,width=140)
translate.config(bg='#dddddd',font=("Times New Roman", 12))
translate.pack()

selable = tk.Label(root,text='Sentiment Analysis')
selable.pack()

sentiment = tk.Text(root,height=1,width=140)
sentiment.config(state='disabled',bg='#dddddd')
sentiment.pack()

ulable = tk.Label(root,text='URL')
ulable.pack()

utext = tk.Text(root,height=1,width=140)
utext.pack()

btn = tk.Button(root,text="Summarize" ,command=summarize,bg='#4db4d6')
btn.pack()

ylable = tk.Label(root,text='')
ylable.pack()

speak_output = tk.Button(root, text="Voice_output", command=Speak, bg='#4db4d6')
speak_output.pack()

root.mainloop()
