from server.lurea import Lurea, just_show_me_this

app = Lurea("127.0.0.1", 3000, debug=True)

@app.route('/')
def index():
    return just_show_me_this('index.html')

@app.route('/teste')
def teste():
    return "<h1>teste 123</h1>"

@app.route("/tue")
def ele_gosta():
    return "<body style='background-color: Grey'><h1>Tu é, boy?<h1></body>"

if __name__ == "__main__":
    app.run()


