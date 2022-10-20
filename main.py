#Created dimxd :)
import PySimpleGUI as sg
from os import startfile


def main():
    sg.theme('DarkAmber')

    #create window
    layout =  [ [sg.Text('Your text: '), sg.InputText(do_not_clear=False)],
                [sg.Button('Save'), sg.Button('OpenFile'), sg.Button('ClearFile'), sg.Button('Exit')], ]

    window = sg.Window('dWrite', layout)



    while True:
        event, values = window.read()
        # text_input = values['-text-']

        #exit
        if event in (sg.WIN_CLOSED, 'Exit'):
            print('exit')
            break


        file = open('text.txt', 'a', encoding='utf-8')

        #clear file (text.txt)
        if event in 'ClearFile':
            with open('text.txt', 'w') as f:
                print('File cleared')
                pass

            

        #press button (open file text.txt)
        if event in 'OpenFile':
            print('open file')
            # system(r'text.txt')
            startfile('text.txt')
            file.close()

        #saved file
        if event in 'Save':

            #if input clear
            if values[0] == '':
                pass

            else:
                print('Text saved')
                file.write(f'{values[0]}\n')  
                file.close()

                    
        
    window.close()


if __name__ == '__main__':
    main()

        