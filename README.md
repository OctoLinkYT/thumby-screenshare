# Thumby Screenshare
This program uses serial to stream screen data to the thumby via the same system that the Thumby Code Editor uses.

## How to Use
First, install dependencies:
`pip install pyserial pillow opencv-python`

Plug in and turn on your thumby, and only after that should you run the script.

## I'm Having Problems
- Try connecting to the [Thumby Code Editor](https://code.thumby.us/) with the device running the script.
- If you're on linux, see [this section of the Q&A](https://thumby.us/FAQ/#linux-with-thumby) before anything else.
- Make sure you're using the correct serial port. For me, this was COM3 but it may differ from case to case.
- Did you install & update dependencies? Double check that installed dependencies are updated to the latest version.
- If all else fails, make an issue and I'll try to help.
