from flask import Flask, request, jsonify
from datetime import date
from models.diet import Diet
from dto.diet_dto import to_dict
from database import db

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:admin123@127.0.0.1:3306/diet-crud"
)

db.init_app(app)


@app.route("/diet", methods=["POST"])
def create_diet():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    date_time = data.get("date_time", date.today())
    is_within_the_diet = data.get("is_within_the_diet", False)

    if name and description:
        diet_new = Diet(
            name=name,
            description=description,
            date_time=date_time,
            is_within_the_diet=is_within_the_diet,
        )
        db.session.add(diet_new)
        db.session.commit()
        return jsonify({"message": "Dieta cadastrada com sucesso!"})

    return jsonify({"message": "Dados inválidos"}), 400


@app.route("/diet/<int:id_diet>", methods=["GET"])
def read_diet(id_diet):
    diet = Diet.query.get(id_diet)
    if diet:
        return jsonify(to_dict(diet))

    return jsonify({"message": "Dieta não encontrada"}), 404


@app.route("/diet/list", methods=["GET"])
def list_diet():
    diets = Diet.query.all()
    if diets:
        diet_list = [to_dict(diet) for diet in diets]

    output = {
        "diets": diet_list,
        "total_diets": len(diet_list),
    }

    return jsonify(output)


@app.route("/diet/<int:id_diet>", methods=["PUT"])
def update_diet(id_diet):
    data = request.json
    diet_update = Diet.query.get(id_diet)

    if diet_update:
        diet_update.name = data.get("name")
        diet_update.description = data.get("description")
        diet_update.date_time = data.get("date_time", date.today())
        diet_update.is_within_the_diet = data.get("is_within_the_diet", False)

        db.session.commit()

        return jsonify({"message": f"Dieta {id_diet} atualizada com sucesso!"})

    return jsonify({"message": "Dieta não encontrada"}), 404


@app.route("/diet/<int:id_diet>", methods=["DELETE"])
def delete_diet(id_diet):
    diet = Diet.query.get(id_diet)

    if diet:
        db.session.delete(diet)
        db.session.commit()

        return jsonify({"message": f"Dieta {id_diet} deletada com sucesso!"})

    return jsonify({"message": "Dieta não encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)
