import speech_recognition as sr
import pyautogui as pya

running = False

def enableDisable():
    running = not running

def recognize_speech_from_mic(recognizer, microphone):
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response
r = sr.Recognizer()
m = sr.Microphone()
words = recognize_speech_from_mic(r, m)

while words["transcription"] != "stop":
<<<<<<< HEAD
    words = recognize_speech_from_mic(r, m)
    print("User said: {}".format(words["transcription"]))
    if words["transcription"] == "click":
        pya.click()

    pya.typewrite(words["transcription"])
=======
    if running:
        words = recognize_speech_from_mic(r, m)
        print("User said: {}".format(words["transcription"]))
        pya.typewrite(words["transcription"])
>>>>>>> 065705aa2409d52d50d8dc149416d2ebffeb3417
   