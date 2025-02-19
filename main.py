from server.lurea import Lurea

app = Lurea("127.0.0.1", 3000)

@app.route(path='/')
def main():
    return "<h1>teste</h1>"

app.run()


