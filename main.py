from server.lurea import Lurea

app = Lurea("127.0.0.1", 3000, debug=True)

@app.route('/')
def main():
    return "<h1>index</h1>"

@app.route('/teste')
def main():
    return "<h1>teste 123</h1>"

if __name__ == "__main__":
    app.run()


