from flask import Flask

app = Flask( __name__ )

@app.route('/')
def main():
    return "Hola desde flask"

@app.route('/method/get', methods=['GET'])
def query_method_get():
    return 'Consultando con GET'

@app.route('/method/post', methods=['POST'])
def query_method_post():
    return 'Consultando con POST'

@app.route('/method/put', methods=['PUT'])
def query_method_put():
    return 'Consultando con PUT'

@app.route('/method/delete', methods=['DELETE'])
def query_method_delete():
    return 'Consultando con DELETE'

@app.route('/method/all', methods=['GET','POST','PUT','DELETE'])
def query_method_all():
    return 'Consultando con todos los metodos'

if __name__ == '__main__':
    app.run()

