from flask import Flask
import random

app = Flask(__name__)

facts_list = ["Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor",
            "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası akıllı telefonlarına bağımlı olduğunu düşünüyor",
            "Sosyal ağların olumlu ve olumsuz yanları var ve bu platformları kullanırken her ikisinin de farkında olmalıyız",
            "Teknoloji bağımlılığı çalışması, modern bilimsel araştırmanın en alakalı alanlarından biridir"]
            
@app.route("/")
def hello_world():
    return f'<h1>selamın aleyküm</h1><a href ="/rastgelebilgi">Rastgele bilgi için tıklayın</a>\n<a href ="/toss_up">Yazı tura için tıklayın</a>'

@app.route("/rastgelebilgi")
def inform_me():
    return f'<h1>{random.choice(facts_list)}, Daha fazlası için sayfayı yenileyin.</h1>'


@app.route("/toss_up")
def toss():
    tossit = ("yazı", "tura",)
    result = random.choice(tossit)
    return f"<h1>{result}</h1>"

app.run(debug=False)

