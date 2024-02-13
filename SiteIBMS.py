from flask import Flask

app = Flask(__name__)
#route -> TesteCameraIBMS.com/Camera
#função -> o que deve ser exibido naquela página

@app.route("/")
def homepage():
    return "Esse é o primeiro Teste"

#colocar o site no ar
if __name__== "__main__":
    app.run(debug=True)

#servidor do heroku