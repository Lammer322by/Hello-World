from flask import Flask,request,render_template

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

class strategy():
    def __init__(self,request):
        if self.request.method == 'GET':
            self.handler=GetHandler(request)
        elif self.request.method == 'POST':
            self.handler=PostHandler(request)

    
    def Handle(self,greets):
        self.handler.handle(greets,self.request)

class GetHandler:
    def handle(self,greets,request):
        return request.form.get(greets)        
        
class PostHandler:
    def handle(self,greets,request):
        return request.form.get(greets)       
      
@app.route('/')
def root():
    return render_template(
        'index.html'
    )

@app.route('/home/cirno_game', methods = ['GET', 'POST'])
def hello_name():
    strat=strategy(request)
    word_in=strat.handrle(request)
    
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
