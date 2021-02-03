from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")

@app.route("/", methods=["GET", "POST"])
def home():
    if(request.method == "GET"):
        return render_template("index.html")
    else:
        if(request.form["n1"] != "" and request.form["n2"] != ""):
            n1 = request.form["n1"]
            n2 = request.form["n2"]

            if (request.form["option"] == "soma"):
                soma = int(n1) + int(n2)
                return {
                    "Resultado": str(soma)
                    }
            elif (request.form["option"] == "subtracao"):
                subtracao = int(n1) - int(n2)
                return {
                    "Resultado": str(subtracao)
                    }
            elif (request.form["option"] == "multiplicacao"):
                multipicacao = int(n1) * int(n2)
                return {
                    "Resultado": str(multipicacao)
                    }
            elif (request.form["option"] == "divisao"):
                divisao = int(n1) / int(n2)
                return {
                    "Resultado": str(divisao)
                    }
        else:
            return "Informe um valor válido!"


@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")

app.run(port=5001, debug=True)




# https://zoom.us/rec/play/i5hiRHP_M8SPAGpsWvZVUDlvrQ3dmNTpJ_q8Jo7UMXmcyEsMRveTQ9FxLQfYsPqpVHpSOjsN-5Dt6ZRd.8CkHfyjuq6x10gm9
# C&kQF9W9