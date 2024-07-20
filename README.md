# 🚀 **This project is open source, yayyy!** 🚀 ![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9C%94-brightgreen)<br>
Feel free to expand upon this silly idea :3 <br>
  ![Webhooker Image](webhooker.png)

# Webhooker 🪝
A simple tool that lets you interact with Discord webhooks  easily. [About 11-17MB]<br>
Think of it as a hook that 'hooks' into your webhook and lets you do many fun things!
> Note: I’m not responsible for any trolling.

## Build Instructions 🛠️
Normally, you only get a windows version. however...
You can build Webhooker on any OS with Python and PyInstaller! Follow these steps:
0. **Install Python:**\
Before doing pip and python stuff, you must [download python](https://www.python.org/downloads/).
1. **Install PyInstaller:**\
  `pip install pyinstaller`
2. **Run the build script:**\
   `python build.py`\
   PyInstaller will automatically build the tool for your OS.
3. **Bonus Step | Zip File (Optioanl):**\
  `python release.py`\
  This creates a zip file that you can upload anywhere!

## Available Commands 🖥️
- `-=setup` : Configure the webhook URL.
- `-=embed` : Start the setup guide to send an embed.
- `-=image` : Send an image from a URL.
- `-=send-file` : Send a file from your computer.
- `-=edit [message id] [new content]` : Edit a message with the specified ID.
- `-=settitle [title]` : Set the title of the application.
- `-=help [asMessage]` : Show this help message. If 'asMessage' is provided, the help message will be sent to the Discord channel.
- `-=debug [asMessage]` : Show the current version and other info. If 'asMessage' is provided, the message will be sent to the Discord channel.
- `-=quit`, `-=exit`, `-=close`, `-=end` : Close the currently running window.

## License 📜

This project is open source and available under the [MIT License](LICENSE).
