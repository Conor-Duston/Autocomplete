
from flask import Flask, request, jsonify

#My import function
from results_parser import most_searched_completions

app = Flask(__name__)

@app.route('/s', methods=['GET'])
def get_query():
    search = request.args.get('search')
    
    results = most_searched_completions(search)

    return jsonify( {'d' : str(results), 'q' : search})

if __name__ == '__main__':
    app.run(debug=True)