# webhooker
A Simple Tool that lets you interact with discord webhooks easily [kinda like.. a hook that you use to hold onto things, it 'hooks' into your webhook and lets you do many fun things]! [About 11-17MB]

note that im not responsible for any trolling

# build thingy or smth
this is currently a windows-only tool [but you can change that], but i have provided all the icon files and the original code for the project\
if you're on any os that isnt windows, simply install pyinstaller\
`pip install pyinstaller` [you need python first]\
and then run it using the following command:\
`pyinstaller --onefile --icon=webhooker.ico webhooker.py`
or use build.bat [note that idk if you can do this on linux and macos]\
[i dont have a virtual machine for any of these os's so i cant quickly update or make non-windows versions, sadly :<]\

Available Commands:\
-=setup : Configure the webhook URL.\
-=embed : Start the setup guide to send an embed.\
-=image : Send an image from a URL.\
-=image-file : Send an image from a "select this image" dialog.\
-=edit [message id] [new content] : Edit a message with the specified ID.\
-=settitle [title] : Set the title of the application.\
-=help [asMessage] : Show this help message. If 'asMessage' is provided, the help message will be sent to the Discord channel.\
