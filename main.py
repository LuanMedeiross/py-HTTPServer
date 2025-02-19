from server.lurea import Lurea

app = Lurea("127.0.0.1", 3000)

@app.route('/')
def main():
    return "<h1>teste</h1>"

@app.route('teste')
def main():
    return "<h1>teste</h1>"

if __name__ == "__main__":
    app.run()


