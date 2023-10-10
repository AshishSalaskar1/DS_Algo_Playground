@app.route('/getAllDiseases')
@cross_origin()
def getALlDiseases():
    return jsonify({"No_of_Disease":len(categories),"Diseases":categories})

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return app.send_static_file('index.html')