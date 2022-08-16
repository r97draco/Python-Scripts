import webbrowser, sys,pyperclip

#sys.argv

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

i=1;


if len(sys.argv) > 2:
    while(i<len(sys.argv)):
          webbrowser.open('https://www.'+ sys.argv[i] +'.com')
          i=i+1
         

    
# webbrowser.open("https://www.tiktok.com")

webbrowser.open(address)
 
