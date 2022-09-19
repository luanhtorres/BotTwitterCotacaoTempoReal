import tweepy
import time
import requests
import json


# BOT CRIADO PARA CONSULTAR UMA OUTRA API (COTAÇÃO DO DOLAR) EM TEMPO REAL E PUBLICAR NO TWITTER A CADA X TEMPO.

api = tweepy.Client(
    consumer_key='suaKEYaqui',
    consumer_secret='suaKEYaqui',
    access_token='suaKEYaqui',
    access_token_secret='suaKEYaqui'
)


running = True
seconds = 1
end = 0
while(running):
    seconds -=1
    if(seconds <= end):
        try:
            req = requests.get ('https://economia.awesomeapi.com.br/all/USD-BRL')
            cotacao = req.json()
            cotacao_print = ("#### Cotação do Dolar ####" + "\n" + "Moeda:"  + cotacao["USD"]["name"] + "\n" + "Data: " + cotacao["USD"]["create_date"] + "\n" + "Valor atual: R$" + cotacao["USD"]["bid"] + "\n" + "Maior Valor: R$" + cotacao["USD"]["high"] + "\n" + "Menor Valor: R$" + cotacao["USD"]["low"])

            tweet = api.create_tweet(text=cotacao_print)
            print(tweet)
            time.sleep(5)
                
        except Exception as error:
            print("Erro:", error)