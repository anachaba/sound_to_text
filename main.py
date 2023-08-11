from google.cloud import speech

def transcribe_audio(mp3_file_path):
    client = speech.SpeechClient.from_service_account_file(r'keys/orion-google-key.json')

    with open(mp3_file_path, 'rb') as f:
        mp3_data = f.read()

    audio_file = speech.RecognitionAudio(content=mp3_data)

    configuration = speech.RecognitionConfig(
        sample_rate_hertz=44100,
        enable_automatic_punctuation=True,
        language_code='en-US'
    )

    response = client.recognize(
        config=configuration,
        audio=audio_file
    )

    transcribed_text = ""
    for result in response.results:
        transcribed_text += result.alternatives[0].transcript + " "

    return transcribed_text.strip()

# Call the function with the path to your MP3 file
mp3_file_path = "testa.mp3"
transcription = transcribe_audio(mp3_file_path)


print(transcription)
