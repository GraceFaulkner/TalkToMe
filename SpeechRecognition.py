# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:50:46 2020

@author: eia18jao
"""

import glob
import speech_recognition as sr
import shutil


def recognition():
    n = 1
    for file in glob.glob('HackMed*.wav'):
            r = sr.Recognizer()
            file_name = sr.AudioFile(file)
            with file_name as source:
                audio = r.record(source)
                print(r.recognize_google(audio))
            shutil.move(rf"U:\HackMed\Recordings\{file}",f"U:\HackMed\Read\Read({n}).wav")
            n+=1

recognition()