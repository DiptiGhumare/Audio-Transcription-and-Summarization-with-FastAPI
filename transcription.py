from transformers import pipeline

def transcribe_audio(file_path: str):
    # Initialize ASR pipeline
    whisper = pipeline('automatic-speech-recognition', model='openai/whisper-large-v3')
    
    # Load audio file
    with open(file_path, 'rb') as audio_file:
        result = whisper(audio_file.read())
    
    # Extract transcription
    transcription = result['text']
    
    # Placeholder timestamps (modify as per requirements)
    words = transcription.split()
    timestamps = [{"word": word, "start_time": i, "end_time": i + 1} for i, word in enumerate(words)]
    
    return transcription, timestamps
