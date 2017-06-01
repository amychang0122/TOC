from transitions.extensions import GraphMachine
import telegram


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def go_user(self, update):
        if(update.message!=None):
            text = update.message.text
        else:
            text = "none";
        return text.lower() == '/start'

    def go_english(self, update):
        if(update.message!=None):
            text = update.message.text
        else:
            text = "none";
        return text == 'English'

    def go_french(self, update):
        if(update.message!=None):
            text = update.message.text
        else:
            text = "none";
        return text == 'Français'

    def go_chinese(self, update):
        if(update.message!=None):
            text = update.message.text
        else:
            text = "none";
        return text == '中文'

    def go_play1(self, update):
        if(update.message!=None):
            text = update.message.text
        else:
            text = "none";
        return text.lower() == '1'

    def go_play2(self, update):
        if(update.message!=None):
            text = update.message.text
        else:
            text = "none";
        return text.lower() == '2'

    def go_play3(self, update):
        if(update.message!=None):
            text = update.message.text
        else:
            text = "none";
        return text.lower() == '3'

    def go_play4(self, update):
        if(update.message!=None):
            text = update.message.text
        else:
            text = "none";
        return text.lower() == '4'

    def go_play5(self, update):
        if(update.message!=None):
            text = update.message.text
        else:
            text = "none";
        return text.lower() == '5'

    def go_cancel(self, update):
        if(update.message!=None):
            text = update.message.text
        else:
            text = "none";
        return text == 'Cancel'

    def go_basic(self, update):
        if(update.message!=None):
            text = update.message.text
        else:
            text = "none";
        return text == 'Yes'

    def go_finish(self, update):
        if(update.message!=None):
            text = update.message.text
        else:
            text = "none";
        return text == 'Finish'

    def on_enter_start(self, update):
        custom_keyboard = [['start']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Press 'start' to start!", reply_markup=reply_markup)

    def on_enter_user(self, update):
        custom_keyboard = [['中文','English'],['Français','Haha(useless)']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Choose the language you want\n", reply_markup=reply_markup)

    def on_enter_cancel(self, update):
        custom_keyboard = [['Yes']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Do you want to restart?\n", reply_markup=reply_markup)

    def on_enter_english(self, update):
        custom_keyboard = [['1','2','3'],['4','5','Cancel']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Which English song do you want?\n" + \
        "1. Rock N Roll\n2. Let Her Go\n3. Sugar\n4. Blank Space\n5. Uptown Funk", reply_markup=reply_markup)

    def on_enter_french(self, update):
        custom_keyboard = [['1','2','3'],['4','5','Cancel']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Vous voulez quel chanson?\n" + \
        "1. Caractère\n2. Les filles d'aujourd'hui\n3. Ça Ira\n4. J'attendais\n5. Je ne sais pas", reply_markup=reply_markup)

    def on_enter_chinese(self, update):
        custom_keyboard = [['1','2','3'],['4','5','Cancel']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="請選擇想要的歌曲：\n" + \
        "1. 也可以\n2. 步步\n3. 情歌\n4. 憨人\n5. 下個轉彎是你嗎", reply_markup=reply_markup)

    def on_enter_c1_play(self, update):
        filename = "1.也可以.mp3"
        file1 = open(filename, 'rb')
        update.message.reply_text("選取音樂中...")
        update.message.reply_audio(audio=file1)
        file1.close()
        custom_keyboard = [['Finish']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Finish?\n", reply_markup=reply_markup)

    def on_enter_c2_play(self, update):
        filename = "2.步步.mp3"
        file1 = open(filename, 'rb')
        update.message.reply_text("選取音樂中...")
        update.message.reply_audio(audio=file1)
        file1.close()
        custom_keyboard = [['Finish']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Finish?\n", reply_markup=reply_markup)

    def on_enter_c3_play(self, update):
        filename = "3.情歌.mp3"
        file1 = open(filename, 'rb')
        update.message.reply_text("選取音樂中...")
        update.message.reply_audio(audio=file1)
        file1.close()
        custom_keyboard = [['Finish']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Finish?\n", reply_markup=reply_markup)

    def on_enter_c4_play(self, update):
        filename = "4.憨人.mp3"
        file1 = open(filename, 'rb')
        update.message.reply_text("選取音樂中...")
        update.message.reply_audio(audio=file1)
        file1.close()
        custom_keyboard = [['Finish']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Finish?\n", reply_markup=reply_markup)

    def on_enter_c5_play(self, update):
        filename = "5.下個轉彎是你嗎.mp3"
        file1 = open(filename, 'rb')
        update.message.reply_text("選取音樂中...")
        update.message.reply_audio(audio=file1)
        file1.close()
        custom_keyboard = [['Finish']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Finish?\n", reply_markup=reply_markup)

    def on_enter_e1_play(self, update):
        filename = "1.Rock N Roll.mp3"
        file1 = open(filename, 'rb')
        update.message.reply_text("loading...")
        update.message.reply_audio(audio=file1)
        file1.close()
        custom_keyboard = [['Finish']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Finish?\n", reply_markup=reply_markup)

    def on_enter_e2_play(self, update):
        filename = "2.Let Her Go.mp3"
        file1 = open(filename, 'rb')
        update.message.reply_text("loading...")
        update.message.reply_audio(audio=file1)
        file1.close()
        custom_keyboard = [['Finish']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Finish?\n", reply_markup=reply_markup)

    def on_enter_e3_play(self, update):
        filename = "3.Sugar.mp3"
        file1 = open(filename, 'rb')
        update.message.reply_text("loading...")
        update.message.reply_audio(audio=file1)
        file1.close()
        custom_keyboard = [['Finish']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Finish?\n", reply_markup=reply_markup)

    def on_enter_e4_play(self, update):
        filename = "4.Blank Space.mp3"
        file1 = open(filename, 'rb')
        update.message.reply_text("loading...")
        update.message.reply_audio(audio=file1)
        file1.close()
        custom_keyboard = [['Finish']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Finish?\n", reply_markup=reply_markup)

    def on_enter_e5_play(self, update):
        filename = "5.Uptown Funk.mp3"
        file1 = open(filename, 'rb')
        update.message.reply_text("loading...")
        update.message.reply_audio(audio=file1)
        file1.close()
        custom_keyboard = [['Finish']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Finish?\n", reply_markup=reply_markup)

    def on_enter_f1_play(self, update):
        filename = "1.Caractère.mp3"
        file1 = open(filename, 'rb')
        update.message.reply_text("Chercher le chanson...")
        update.message.reply_audio(audio=file1)
        file1.close()
        custom_keyboard = [['Finish']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Finish?\n", reply_markup=reply_markup)

    def on_enter_f2_play(self, update):
        filename = "2.Les filles d'aujourd'hui.mp3"
        file1 = open(filename, 'rb')
        update.message.reply_text("Chercher le chanson...")
        update.message.reply_audio(audio=file1)
        file1.close()
        custom_keyboard = [['Finish']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Finish?\n", reply_markup=reply_markup)

    def on_enter_f3_play(self, update):
        filename = "3.Ça Ira.mp3"
        file1 = open(filename, 'rb')
        update.message.reply_text("Chercher le chanson...")
        update.message.reply_audio(audio=file1)
        file1.close()
        custom_keyboard = [['Finish']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Finish?\n", reply_markup=reply_markup)

    def on_enter_f4_play(self, update):
        filename = "4.J'attendais.mp3"
        file1 = open(filename, 'rb')
        update.message.reply_text("Chercher le chanson...")
        update.message.reply_audio(audio=file1)
        file1.close()
        custom_keyboard = [['Finish']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Finish?\n", reply_markup=reply_markup)

    def on_enter_f5_play(self, update):
        filename = "5.Je ne sais pas.mp3"
        file1 = open(filename, 'rb')
        update.message.reply_text("Chercher le chanson...")
        update.message.reply_audio(audio=file1)
        file1.close()
        custom_keyboard = [['Finish']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        update.message.reply_text(text="Finish?\n", reply_markup=reply_markup)

    def on_exit_state2(self, update):
        print('Leaving state2')
