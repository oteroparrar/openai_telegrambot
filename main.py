import openai
import telebot

openai.api_key = "TU OPEN AI TOKEN"
bot = telebot.TeleBot("TU TELEGRAM TOKEN")

@bot.message_handler(commands =  ["start", "help"])
def enviar (message):
    bot.reply_to (message, "Que bola asere,  pregunta lo que quieras")
    


@bot.message_handler(commands=[""])

@bot.message_handler(func=lambda message:True)
def Descargar(message):
        
    question= message.text
    mess = message.chat.id
    model_engine = "text-davinci-003"
    prompt = question
    # Generate a response
    completion = openai.Completion.create(
    engine=model_engine,
    prompt=question,
    max_tokens=500,
    n=1,
    stop=None,
    temperature=0.5,
        )
    
    response = completion.choices[0].text
    return bot.send_message(mess, response)

bot.infinity_polling()
