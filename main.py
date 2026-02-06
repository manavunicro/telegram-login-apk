import asyncio
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.clipboard import Clipboard
from telegram_auth import send_otp, verify_otp

class TelegramLogin(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.phone = TextInput(
            hint_text="Enter phone number (+91xxxxxxxxxx)",
            multiline=False
        )

        self.code = TextInput(
            hint_text="Enter OTP",
            multiline=False
        )

        self.status = Label(text="")

        send_btn = Button(text="Send OTP")
        verify_btn = Button(text="Verify & Login")

        send_btn.bind(on_press=self.send_otp_btn)
        verify_btn.bind(on_press=self.verify_btn)

        self.layout.add_widget(self.phone)
        self.layout.add_widget(send_btn)
        self.layout.add_widget(self.code)
        self.layout.add_widget(verify_btn)
        self.layout.add_widget(self.status)

        return self.layout

    def send_otp_btn(self, instance):
        try:
            asyncio.run(send_otp(self.phone.text))
            self.status.text = "OTP sent via Telegram"
        except Exception as e:
            self.status.text = str(e)

    def verify_btn(self, instance):
        try:
            user_id = asyncio.run(
                verify_otp(self.phone.text, self.code.text)
            )
            Clipboard.copy(str(user_id))
            self.status.text = f"Login Success\nTelegram ID:\n{user_id}\n(Copied)"
        except Exception as e:
            self.status.text = str(e)

TelegramLogin().run()
