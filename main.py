from tkinter import Tk, END
from tkinter import ttk
from tkinter import scrolledtext
import re

class BinaryDecoderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Decoder by MD. Bayazid")
        self.root.geometry("1000x600")
        self.root.resizable(False, False)
        self.create_tabs()

    def create_tabs(self):
        self.tab_manager = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(self.tab_manager)
        self.tab2 = ttk.Frame(self.tab_manager)
        self.tab_manager.add(self.tab1, text="Decoder" , )
        self.tab_manager.add(self.tab2, text="Encoder")
        self.tab_manager.pack(padx=10, pady=10)
        self.create_decoder_tab()
        self.create_encoder_tab()

    def create_decoder_tab(self):
        binary_frame = ttk.LabelFrame(self.tab1, text="Binary Code" ,)
        binary_frame.pack(padx=10, pady=10)
        self.binary_input = scrolledtext.ScrolledText(binary_frame, width=800, height=10, wrap="word", font=("./Anonymous_Pro_I.ttf", 15))
        self.binary_input.pack(padx=10, pady=10)

        decode_button = ttk.Button(self.tab1, text="Decode", width=100, command=self.decode)
        decode_button.pack()

        decoded_frame = ttk.LabelFrame(self.tab1, text="Decoded Text")
        decoded_frame.pack(padx=10, pady=10)
        self.decoded_output = scrolledtext.ScrolledText(decoded_frame, width=800, height=15, font=("./Anonymous_Pro_I.ttf", 15), wrap="word")
        self.decoded_output.pack(padx=10, pady=10)

    def create_encoder_tab(self):
        ascii_frame = ttk.LabelFrame(self.tab2, text="ASCII Code")
        ascii_frame.pack(padx=10, pady=10)
        self.ascii_input = scrolledtext.ScrolledText(ascii_frame, width=800, height=10, wrap="word", font=("./Anonymous_Pro_I.ttf", 15))
        self.ascii_input.pack(padx=10, pady=10)

        encode_button = ttk.Button(self.tab2, text="Encode", width=100, command=self.encode)
        encode_button.pack()

        encoded_frame = ttk.LabelFrame(self.tab2, text="Encoded Text")
        encoded_frame.pack(padx=10, pady=10)
        self.encoded_output = scrolledtext.ScrolledText(encoded_frame, width=800, height=15, font=("./Anonymous_Pro_I.ttf", 15), wrap="word")
        self.encoded_output.pack(padx=10, pady=10)

    def encode(self):
        text = self.ascii_input.get(1.0, END).strip()
        if text:
            try:
                
                if re.match(r'^[\x20-\x7E]*$', text):  
                    binary_representation = ' '.join(format(ord(char), '08b') for char in text)
                    self.encoded_output.delete(1.0, END)
                    self.encoded_output.insert(1.0, binary_representation)
                else:
                    self.show_error("Input contains invalid characters. Only printable ASCII characters are allowed.")
            except Exception as e:
                self.show_error(f"Encoding error: {str(e)}")
        else:
            self.show_error("Please enter text to encode!")

    def decode(self):
        binary_text = self.binary_input.get(1.0, END).strip()
        if binary_text:
            try:
              
                if re.match(r'^[01\s]+$', binary_text): 
                    decoded_text = ''.join(chr(int(code, 2)) for code in binary_text.split())
                    self.decoded_output.delete(1.0, END)
                    self.decoded_output.insert(1.0, decoded_text)
                else:
                    self.show_error("Input contains invalid binary code. Only 0s and 1s are allowed.")
            except ValueError:
                self.show_error("Invalid binary code!")
            except Exception as e:
                self.show_error(f"Decoding error: {str(e)}")
        else:
            self.show_error("Please enter binary code to decode!")

    def show_error(self, message):
        self.decoded_output.delete(1.0, END)
        self.decoded_output.insert(1.0, message)


if __name__ == "__main__":
    root = Tk()
    app = BinaryDecoderApp(root)
    root.mainloop()
