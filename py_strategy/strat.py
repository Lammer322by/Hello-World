from flask import Flask,request,render_template

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

class strategy():
    def __init__(self):
        pass

    def handle(self,greets,request):
        if request.method == 'GET':
            self.handler=GetHandler()
        elif request.method == 'POST':
            self.handler=PostHandler()

        print(greets,request)
        return self.handler.handle(greets,request)


class GetHandler:
    def handle(self,greets,request):
        wout=request.args.get(greets)        
        return wout

class PostHandler:
    def handle(self,greets,request):
        wout=request.form.get(greets)       
        return wout

@app.route('/')
def root():
    return render_template(
        'base.html'
    )

@app.route('/home/cirno_game', methods = ['GET', 'POST'])
def hello_name():
    reaction="Enter toyr word"
    strat=strategy()
    word_in=strat.handle("word", request)
    print(word_in)

    if word_in is None:
        word_in=""
    
    if word_in == 'your word':
        reaction = "Congrats!"
    else:
        reaction = "Please, try again"

    return render_template(
        'base.html',
        word=word_in,
        reaction=reaction
    )

if __name__ == '__main__':
   app.run(debug = True)
   	
