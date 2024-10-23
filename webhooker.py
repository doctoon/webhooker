import requests
import json
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

CONFIG_FILE = "config.json"
VERSION = "1.2.3"
BUILD = "stable"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            config = json.load(file)
    else:
        config = {}
        
    # Set default values if they are missing
    if "prefix" not in config:
        config["prefix"] = "-="
    if "webhook_url" not in config:
        config["webhook_url"] = ""

    return config

def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

def set_app_title(title):
    os.system(f"title {title}")

def get_webhook_url():
    config = load_config()
    return config.get("webhook_url")

def send_message(message):
    webhook_url = get_webhook_url()
    if not webhook_url:
        print("Webhook URL is not set. Use -=setup to set the webhook URL.")
        return

    max_length = 2000
    if len(message) > max_length:
        # Split the message into chunks of 2000 characters or less, keeping whole words
        words = message.split()
        chunk = ""
        for word in words:
            if len(chunk) + len(word) + 1 <= max_length:
                chunk += " " + word
            else:
                # Send the current chunk and start a new one
                data = {"content": chunk.strip()}
                response = requests.post(webhook_url, json=data)
                if response.status_code != 204:
                    print(f"Failed to send message chunk: {response.status_code}")
                chunk = word
        if chunk:
            data = {"content": chunk.strip()}
            response = requests.post(webhook_url, json=data)
            if response.status_code != 204:
                print(f"Failed to send message chunk: {response.status_code}")
    else:
        data = {"content": message}
        response = requests.post(webhook_url, json=data)
        if response.status_code != 204:
            print(f"Failed to send message: {response.status_code}")

def send_embed():
    webhook_url = get_webhook_url()
    if not webhook_url:
        print("Webhook URL is not set. Use -=setup to set the webhook URL.")
        return

    title = input("Enter the title (or type 'skip' to skip): ")
    if title.lower() == "skip":
        title = None
    description = input("Enter the description (or type 'skip' to skip): ")
    if description.lower() == "skip":
        description = None
    color = input("Enter the color as a hex value (e.g., 'FF5733') (or type 'skip' to skip): ")
    if color.lower() == "skip":
        color = None
    else:
        color = color.lstrip('#')
        color = int(color, 16)
    embed = {
        "title": title,
        "description": description,
        "color": color
    }
    data = {"embeds": [embed]}
    response = requests.post(webhook_url, json=data)
    if response.status_code != 204:
        print(f"Failed to send embed: {response.status_code}")

def send_image(url):
    webhook_url = get_webhook_url()
    if not webhook_url:
        print("Webhook URL is not set. Use -=setup to set the webhook URL.")
        return

    data = {
        "embeds": [{"image": {"url": url}}]
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code != 204:
        print(f"Failed to send image: {response.status_code}")

def send_file():
    webhook_url = get_webhook_url()
    if not webhook_url:
        print("Webhook URL is not set. Use -=setup to set the webhook URL.")
        return

    Tk().withdraw()
    file_path = askopenfilename(filetypes=[("All files ✨", "*")])
    if file_path:
        with open(file_path, "rb") as file:
            response = requests.post(webhook_url, files={"file": file})
            if response.status_code != 200:
                print(f"Failed to send file: {response.status_code}")
    else:
        print("No file selected.")

def edit_message(message_id, new_content):
    webhook_url = get_webhook_url()
    if not webhook_url:
        print("Webhook URL is not set. Use -=setup to set the webhook URL.")
        return

    data = {"content": new_content}
    response = requests.patch(f"{webhook_url}/messages/{message_id}", json=data)
    if response.status_code != 200:
        print(f"Failed to edit message: {response.status_code}")

def show_help(as_message=False):
    config = load_config()
    help_text = f"""
Available Commands:
{config["prefix"]}setup : Configure the webhook URL.
{config["prefix"]}embed : Start the setup guide to send an embed.
{config["prefix"]}image : Send an image from a URL.
{config["prefix"]}send-file : Send a file from your computer.
{config["prefix"]}edit [message id] [new content] : Edit a message with the specified ID.
{config["prefix"]}settitle [title] : Set the title of the application.
{config["prefix"]}setprefix [prefix] : Set a custom command prefix.
{config["prefix"]}help [asMessage] : Show this help message. If 'asMessage' is provided, the help message will be sent to the Discord channel.
{config["prefix"]}debug [asMessage] : Show the current version and other info, useful for finding bugs i guess. If 'asMessage' is provided, the message will be sent to the Discord channel.
{config["prefix"]}quit, {config["prefix"]}exit, {config["prefix"]}close, {config["prefix"]}end : Close the currently running window.
"""
    if as_message:
        send_message(help_text)
    else:
        print(help_text)

def show_debug(as_message=False):
    config = load_config()
    if as_message:
        debug_text = f"""
You are currently using **Webhooker version {VERSION}** On The **`{BUILD}`** Build.
||⚠️ JSON Output included sensitive webhook info.||
"""
        send_message(debug_text)
    else:
        debug_text = f"""
You are currently using Webhooker version {VERSION} On The '{BUILD}' Build.
Your Config.json:
{json.dumps(config, indent=4)}
"""
        print(debug_text)

def quit_program():
    print("Exiting program.")
    exit()

def setup_webhook_url():
    print("Enter the webhook URL: ", end="")
    url = input().strip()
    config = load_config()
    config["webhook_url"] = url
    save_config(config)
    print(f"Webhook URL has been set.")

def set_prefix(new_prefix):
    config = load_config()
    config["prefix"] = new_prefix
    save_config(config)
    print(f"Command prefix has been set to '{new_prefix}'")

# Command registration and aliases
commands = {}
aliases = {}

def register_command(name, func, alias_list=[]):
    commands[name] = func
    for alias in alias_list:
        aliases[alias] = name

def execute_command(command, args, config):
    if command == "setup":
        setup_webhook_url()
    elif command == "embed":
        send_embed()
    elif command == "image":
        if args:
            send_image(args[0])
        else:
            print("Usage: -=image [url]")
    elif command == "send-file":
        send_file()
    elif command == "edit":
        if len(args) >= 2:
            message_id = args[0]
            new_content = " ".join(args[1:])
            edit_message(message_id, new_content)
        else:
            print("Usage: -=edit [message id] [new content]")
    elif command == "settitle":
        if args:
            set_app_title(" ".join(args))
            print(f"Application title set to: {' '.join(args)}")
        else:
            print("Usage: -=settitle [title]")
    elif command == "help":
        if args and args[0] == "asMessage":
            show_help(as_message=True)
        else:
            show_help()
    elif command == "debug":
        if args and args[0] == "asMessage":
            show_debug(as_message=True)
        else:
            show_debug()
    elif command == "setprefix":
        if args:
            config["prefix"] = args[0]
            save_config(config)
            print(f"Command prefix has been set to '{args[0]}'")
        else:
            print("Usage: -=setprefix [prefix]")
    elif command in ["quit", "exit", "close", "end"]:
        print("Exiting Webhooker...")
        exit(0)
    else:
        send_message(command + " " + " ".join(args))

def main():
    set_app_title(f"Webhooker {VERSION}")
    print(f"Running webhooker version {VERSION} On the {BUILD} build.")
    config = load_config()
    prefix = config["prefix"]

    while True:
        print("Type Your Command/Message: ", end="")
        user_input = input().strip()
        config = load_config()  # Reload config to get updated prefix
        prefix = config["prefix"]
        
        if user_input.startswith(prefix):
            command_with_args = user_input[len(prefix):].strip()
            if command_with_args:
                parts = command_with_args.split(" ")
                command = parts[0]
                args = parts[1:]
                execute_command(command, args, config)
        else:
            send_message(user_input)

if __name__ == "__main__":
    main()
