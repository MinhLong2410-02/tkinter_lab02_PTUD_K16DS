from tkinter import *
import tkinter.filedialog as fd
class TextEditor:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("TextEditor")
        self.window.geometry("700x600")

        self.window.resizable(True, True)
        self.window.minsize(600, 550)
    
        
        self.current_font_family = "Arial"
        self.current_font_size = 12
        self.fontColor ='#000000'
        self.fontBackground= '#FFFFFF'

        self.text_editor = Text(self.window, width=97, height=25,
                                font=(self.current_font_family, self.current_font_size), 
                                selectbackground=self.fontColor,
                                undo=True
        )
        self.text_editor.pack(expand=YES, fill=BOTH)
        
        self.menu_bar = Menu(self.window)
        self.filemenu = Menu(self.menu_bar)
        self.toolmenu = Menu(self.menu_bar)
        
        self.filemenu.add_command(label = 'New', command = self.new_text_file)
        self.filemenu.add_command(label = 'Save', command = self.save_text_file)
        self.filemenu.add_command(label = 'Open', command = self.open_text_file)
        
        
        self.menu_bar.add_cascade(label = 'File', menu = self.filemenu)
        self.menu_bar.add_cascade(label = 'Tool', menu = self.toolmenu)
        self.menu_bar.add_cascade(label = 'About', command = self.about)
        
        self.toolmenu.add_command(label = 'Clear', command = self.clear)
        self.toolmenu.add_command(label = 'Play audio', command = self.audio_play)
        
        
        self.window.config(menu=self.menu_bar)
        
    def new_text_file(self):
        if(fd.askyesno("Message", "Unsaved work will be lost. Continue?")):
            self.text_editor.delete(0, END)  
    
    def save_text_file(self):
        savefile = fd.asksaveasfile(mode = 'w', defaultextension = ".txt")
        text2save = str(self.text_editor.get("1.0", END))
        savefile.write(text2save)
        savefile.close()
    
    def open_text_file(self):
        openfile = fd.askopenfile(mode = 'r', defaultextension = ".txt")
        text = openfile.read()
        self.text_editor.insert(END, text)
        openfile.close()
    
    def clear(self):
        self.text_editor.delete("1.0", END)
    
    def audio_play(self):
        from gtts import gTTS
        from io import BytesIO
        from pydub import AudioSegment
        from pydub.playback import play
        audio = gTTS(text = self.text_editor.get("1.0", END), lang = 'vi', slow = False)
        mp3_fp = BytesIO()
        audio.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        play(AudioSegment.from_file(mp3_fp, format="mp3"))
    
    def about(self):
        self.text_editor.insert(END, "\nNotepad bằng Python với Tkinter\nHọ tên: Trần Minh Long\nMSSV: 20078291\n")
    
    
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = TextEditor()
    app.run()