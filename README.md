**README**

# Discord Bot Invitation Generator

This Python script generates a Discord bot invitation link using the provided bot ID. The generated link can be used to invite the bot to your Discord server.

## Installation

No installation is required. You can run the script directly using Python.

## Usage

1. Open the script in a text editor or IDE.
2. Replace the `id` variable value with your Discord bot ID.
3. Save the changes.
4. Run the script using Python.

The script will open your default web browser and navigate to the generated Discord bot invitation link.

## Example

```python
import webbrowser

id = 'your_bot_id_here'
def main():
    url = f"https://discord.com/oauth2/authorize?client_id={id}&scope=bot&permissions=0"
    webbrowser.open(url)

if __name__ == '__main__':
    main()
    print('done.\nengoy your bot!')
```

Replace `'your_bot_id_here'` with your actual Discord bot ID.

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.
