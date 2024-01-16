import customtkinter
import pyperclip
from faker import Faker


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("450x200")
        self.title("FGen")
        self.iconbitmap('ico.ico')
        self.resizable("False", "False")

        # Generate Button
        self.button = customtkinter.CTkButton(self,
                                              command=self.update_output_number,
                                              text="Generate",
                                              font=('Beantown', 22),
                                              )
        self.button.grid(row=0,column=0,padx=20,pady=20,sticky='ew')

        # Copy Button
        self.copy_button = customtkinter.CTkButton(self,
                                                   command=self.copy_to_clipboard,
                                                   text="Copy",
                                                   font=('Beantown', 16)
                                                   )
        self.copy_button.grid(row=2,column=0,padx=20,pady=20,sticky='e')

        # Output field
        self.output_frame = customtkinter.CTkFrame(self)
        self.output_frame.grid(row=2, column=0, sticky="w", padx=20)
        self.output_number = customtkinter.CTkTextbox(self.output_frame,
                                                      width=200,
                                                      height=30,
                                                      corner_radius=2,
                                                      font=('Beantown', 18),
                                                      )
        self.output_number.grid(row=2, column=0, sticky="w")

        # Radiobuttons
        self.radiobuttons_frame = customtkinter.CTkFrame(self)
        self.radiobuttons_frame.grid(row=1, column=0, sticky="we",padx=5, pady=20)
        self.selected_brand = customtkinter.StringVar(value='Other')
        self.selected_brand.set(CreditCardBrand.VISA)

        self.visa_button = customtkinter.CTkRadioButton(self.radiobuttons_frame,
                                                        text="VISA",
                                                        variable=self.selected_brand,
                                                        value=CreditCardBrand.VISA,
                                                        font=('Beantown', 13),
                                                        width=120,
                                                        radiobutton_height=15,
                                                        radiobutton_width=15,
                                                        border_width_checked=4
                                                        )
        self.visa_button.grid(row=1, column=0, sticky='w')

        self.mastercard_button = customtkinter.CTkRadioButton(self.radiobuttons_frame,
                                                              text="MasterCard",
                                                              variable=self.selected_brand,
                                                              value=CreditCardBrand.MASTERCARD,
                                                              font=('Beantown', 13),
                                                              radiobutton_height=15,
                                                              radiobutton_width=15,
                                                              border_width_checked=4,
                                                              )
        self.mastercard_button.grid(row=1, column=1, sticky='w', padx=20)

        self.amex_button = customtkinter.CTkRadioButton(self.radiobuttons_frame,
                                                        text="AMEX",
                                                        variable=self.selected_brand,
                                                        value=CreditCardBrand.AMEX,
                                                        font=('Beantown', 13),
                                                        radiobutton_height=15,
                                                        radiobutton_width=15,
                                                        border_width_checked=4
                                                        )
        self.amex_button.grid(row=1, column=2, padx=80, sticky='e')

    # functions for buttons and output field
    def update_output_number(self):
        selected_brand = self.selected_brand.get()
        result = self.generate_button(selected_brand)
        self.output_number.delete(1.0, "end")
        self.output_number.insert("end", result)

    def generate_button(self, card_type):
        return fake_credit_card_generator(card_type)

    def copy_to_clipboard(self):
        content = self.output_number.get(1.0, "end-1c")
        pyperclip.copy(content)

# Credit cards and fake card generator
class CreditCardBrand():
    VISA = 'visa'
    MASTERCARD = 'mastercard'
    AMEX = 'amex'

def fake_credit_card_generator(card_type):
    fake = Faker()
    credit_card = fake.credit_card_number(card_type=card_type)
    return credit_card


app = App()
app.grid_columnconfigure(0, weight=1)
app.mainloop()
