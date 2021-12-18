import PySimpleGUI as sg
sg.theme('DarkAmber')   # Add a touch of color

class GUIController:
    
    def __init__(self):
        self.layout = [  [sg.Text('Select sample:')],
            [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('7'), sg.Button('8'), sg.Button('9'),],
            [sg.Button('Toggle repeat')] ]
        self.window = sg.Window('Window Title', self.layout)
        self.repeating = False

    def enable(self, sampler, quit_func):
        self.sampler = sampler
        self.quit = quit_func

    def update(self):
        event, values = self.window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            self.window.close()
            self.quit()
        elif event == "Toggle repeat":
            self.repeating = not self.repeating
        else:
            s = int(event) - 1
            self.sampler.play_sample(self.sampler.samples.get_sample(s))
            if self.repeating:
                self.sampler.mark_loop_pos()