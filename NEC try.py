import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source2:
    audio2 = r.listen(source2)
    text = r.recognize_google(audio2)
    text = text.lower()

print("You said : " + text)


#print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
#print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])


