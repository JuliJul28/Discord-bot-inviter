Discord Bot Invitation Generator
This Python script generates a Discord bot invitation link using the provided bot ID. The generated link can be used to invite the bot to your Discord server.

Installation
No installation is required. You can run the script directly using Python.

Usage
Open the script in a text editor or IDE.
Replace the id variable value with your Discord bot ID.
Save the changes.
Run the script using Python.
The script will open your default web browser and navigate to the generated Discord bot invitation link.

Code
python
Copy code
import webbrowser

id = input('please enter your discord bot id that you want to invite: ')

def main():
    url = f"https://discord.com/oauth2/authorize?client_id={id}&scope=bot&permissions=0"
    webbrowser.open(url)

if __name__ == '__main__':
    main()
    print('done.\nenjoy your bot!')
Notes
Make sure your bot's client ID is correct.
The permissions parameter is set to 0, which means no special permissions are requested for the bot. You can adjust this if your bot needs specific permissions by changing the permissions value in the URL.
If the web page does not open, ensure your default web browser is properly configured.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

