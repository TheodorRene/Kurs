



# Bevegelser
- h,j,k,l ← ↓ ↑ →
- w(words), b(backwards words), e(end of words)
- the lazy fox jumped over the quick brown dog
- 0(Start), $(End of line)

# Operatorer med bevegelse
- d - Delete
- c - Change (Slett og gå inn i Insert mode)
- y - Yank(Copy)

# Ekstra bevegelser sammen med operatorer
- i - Inside
- a - Around
- t - unTil

# Ellers kjekt
- f - Find - gå til karakter i linja
- u - Undo
- Ctrl-r - Redo
- p - Paste
- / - Search
- o - insert mode under linjen du er på
- O - insert mode under linjen du er på
- % - hopp mellom ([{"
- r - Replace one character

# "handlingsbevegelser"
- d w "delete word "
- d a w "delete around/after word"
- d i w "delete inside word"
- d i ( "delete inside parentheses"
- d d "delete line"
- D "delete rest of line"

# Oppgaver (10/15 min)
* Lag en ny fil som heter f.eks "main.py"
* Og prøv å skriv fizzbuzz i Vim
* Skriv en enkel fizzbuzz funksjon som tar inn et tall og returnerer en streng
	- hvis tallet er delelig med 3 returnerer Fizz
	- hvis tallet er delelig med 5 returner Buzz
	- hvis tallet er delelig med begge returner FizzBuzz
	- Ellers returnerer tallet som en streng

* Så litt refakturering
* oversett alle variablene til norsk.(fizzbuzz på norsk, må være fissbuss)
	- Hint "Change In Word"
* Hvis du gjorde operasjoner i en if-setning, prøv å flytt det ut i en variabel
	- hint "Change unTil Colon"
	- hint "Change In Parenthes"
* Til slutt vil jeg at endre så det ikke er 3 og 5, men 7 og 8 
	- Bruk "r" så slipper du å hoppe inn i insert mode for en så enkel endring
* Skru på relativenumber ":set relativenumber" og kopier hele funksjonen i en operasjon, kanskje paste den
	- Hint: kvantifisering av operasjon. "Yank Antall Retning"

