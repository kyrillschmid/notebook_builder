import time
import threading
import sys
from dotenv import load_dotenv
from openai import OpenAI


def blinking_indicator():
    while not stop_threads:
        for i in range(4):
            sys.stdout.write("\r" + "." * i)  # Print dots
            sys.stdout.flush()
            time.sleep(0.5)  # Time interval between blinks


def call_model(prompt, model="gpt-4-0125-preview"):
    load_dotenv()
    client = OpenAI()

    global stop_threads
    stop_threads = False
    thread = threading.Thread(target=blinking_indicator)
    thread.start()

    try:
        # Make the API call
        response = client.chat.completions.create(
            # model="gpt-3.5-turbo-1106",
            # model="gpt-4-0613",
            model=model,
            messages=[{"role": "system", "content": prompt}],
        )
        return response.choices[0].message.content
    finally:
        # Stop the progress bar
        stop_threads = True
        thread.join()
        sys.stdout.write("\r")  # Clear the line
        sys.stdout.flush()
