from flask import Flask

app = Flask( __name__ )

@app.route('/')
def main():
    return "Hola desde flask"

@app.route('/method/get', methods=['GET'])
def query_method_get():
    return 'Consultando con GET'

if __name__ == '__main__':
    app.run()

