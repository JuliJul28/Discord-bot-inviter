import webbrowser

id = input('please enter your dicord bot id that you want to invite: ')
def main():
    url = f"https://discord.com/oauth2/authorize?client_id={id}&scope=bot&permissions=0"
    webbrowser.open(url)

if __name__ == '__main__':
    main()
    print('done.\nengoy your bot!')
