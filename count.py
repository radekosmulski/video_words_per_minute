import os
import re
import argparse
import time
import subprocess
import json
from pytube import YouTube

# Record the start time
start_time = time.time()

# Create the downloads directory if it doesn't exist
if not os.path.exists('downloads'):
    os.makedirs('downloads')

parser = argparse.ArgumentParser(description='Download audio from YouTube video and output statistics.')
parser.add_argument('video_url', type=str, help='The URL of the YouTube video.')
args = parser.parse_args()

args = parser.parse_args()
yt = YouTube(args.video_url)
video_duration_in_minutes = yt.length / 60

# stream = sorted(yt.streams.filter(only_audio=True), key=lambda s: s.abr, reverse=True)[0]
stream = sorted(yt.streams.filter(progressive=True), key=lambda s: s.resolution)[0]

print('Downloading the file for {}...'.format(yt.title))

# Clean the title so it can be used as a filename
title = re.sub('[^a-zA-Z0-9 \n\.]', '', yt.title).replace(' ', '_')

stream.download(output_path='downloads', filename=title + '.webm')

filename = 'downloads/' + title + '.webm'

print('Running transcription using insanely-fast-whisper...')
subprocess.run(['insanely-fast-whisper', '--file-name', filename])

with open('output.json', 'r') as f:
    output = json.load(f)

num_words_spoken = len(output['text'].split())

print('Number of words spoken: {}'.format(num_words_spoken))
print('Video duration: {:.2f} minutes'.format(video_duration_in_minutes))
print('Words per minute: {:.2f}'.format(num_words_spoken / video_duration_in_minutes))

total_runtime = (time.time() - start_time) / 60
print('Ran in: {:.2f} minutes'.format(total_runtime))

