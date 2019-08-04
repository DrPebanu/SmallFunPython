import webbrowser, sys, pyperclip

sys.argv

# Check if command line arguments were passed
if len(sys.argv) > 1:
    adress = ' '.join(sys.argv[1:])
else:
    adress = pyperclip.paste()
#/maps/place/' + adress
webbrowser.open('https://www.google.se/maps/place/' + adress)

