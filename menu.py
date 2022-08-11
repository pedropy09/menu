#cor do texto
#o GREEN é o nome da cor, então colocar desse jeito em inglês
from colorama import Fore, Back, Style 
print(Fore.MAGENTA) 

#começo
print(f'''

digite cmd para ver os comandos
  ________    _____
 /\/\/\/\/\  | "º  \\
<|\/\/\/\/\|_/ /___/
 |____________/
 |_|_|   /_/_/

''')

#loop
loop="positivo"
while loop == "positivo":
        
        #psq
    psq = input("... ")

        #git/meu github, username
    if psq == "git":
        print("meu git: pedropy09")

        #gitlink/meu github, link
    elif psq == "gitlink":
        print("link do meu git: https://github.com/pedropy09")
        
        #telegram
    elif psq == "telegram":
        print(f'''
        
        meu username do telegram: Pedro_py
        link do meu perfil: https://t.me/Pedro_py

        ''')
        
        #cmd/comandos
    elif psq == "cmd":

        print(f'''

        ╭────────────────────────
        ╎┝〢 gitlink
        ╎┝〢 meu github/link
        ╎
        ╎┝〢git
        ╎┝〢meu github/username
        ╎
        ╎┝〢telegram
        ╎┝〢meu telegram
        ╰────────────────────────
        
        ''')