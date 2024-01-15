# Video Word Counter

A small utility that will download a YouTube video, count words in it and display some useful stats.

Many thoughtful people might be receiving advice to speak faster, but that is not as important as the clarity of your thinking. Using this tool, you can figure out how fast you speak and compare yourself to people whom you admire -- my guess is that you are already speaking as fast or faster then some of them.

Nothing works as well as raw numbers to change your beliefs 🙂 (at least for some subset of the population). May this app set you free 🙏.

Inspired by [a conversation on Twitter](https://x.com/radekosmulski/status/1746354989772284126?s=20).

# Installation

```
pip install -r requirements.txt
sudo apt install ffmpeg
pip install pipx
pipx ensurepath
pipx install insanely-fast-whisper --force --pip-args="--ignore-requires-python"
```

At the moment of creation of this repo, `insanely-fast-whisper` doesn't support Python 3.12. If you run into any trouble with the installation process, please take a look at [its repository](https://github.com/Vaibhavs10/insanely-fast-whisper).

# How to

After you've installed everything, from terminal run: `python count.py <video_url>`, for instance `python count.py https://www.youtube.com/watch?v=Unzc731iCUY`.

This should give you the words spoken per minute statistic you can use as a reference point
