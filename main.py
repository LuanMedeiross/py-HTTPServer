from server.daddy import Daddy, gimme_that_damn_page

app = Daddy()

@app.right_here('/')
def index():
    return gimme_that_damn_page('index.html')

@app.right_here('/teste')
def teste():
    return "<h1>teste 123</h1>"

@app.right_here("/tue")
def ele_gosta():
    return "<body style='background-color: Grey'><h1>Tu é, boy?<h1></body>"

if __name__ == "__main__":
    app.run_bitch_run(debug = True)


