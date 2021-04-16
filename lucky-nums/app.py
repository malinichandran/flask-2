from flask import Flask, request, jsonify, render_template
from models import db, connect_db, GetLuckyNum
# from forms import LuckyNumForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///luckynums_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)
db.create_all()

@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")

@app.route("/api/get-lucky-num", methods=["POST"])
def get_lucky_num():
        # form = LuckyNumForm()
        
        # if form.validate_on_submit():

        #     name = form.name.data
        #     email = form.email.data
        #     birth_year = form.birth_year.data
        #     color = form.color.data
            name = request.json['name']
            email = request.json['email']
            birth_year = request.json['birth_year']
            color = request.json['color']
            errors = {
                        "color": [
                        "Invalid value, must be one of: red, green, orange, blue."
                        ],
                        "name": [
                        "This field is required."
                        ],
                        "birth_year":[
                        "Enter a year between 1900 and 2000."
                        ]
                    }
            if name == " " or email == " ":
                return errors.name

            if color == " " or  color != "red" or "blue"or"green"or"orange":
                return errors.color
            
            if birth_year == " " or birth_year <= 1900 or birth_year >=2000:
                return errors.birth_year
            
            else:
                response = {
                            "num": {
                                "fact": "67 is the number of throws in Judo.",
                                "num": 67
                            },
                            "year": {
                                "fact": "1950 is the year that nothing remarkable happened.",
                                "year": "1950"
                            }
                            }

            # luckynum = GetLuckyNum(name=name,
            #                     email=email,
            #                     birth_year=birth_year,
            #                     color=color)
            # db.session.add(luckynum)
            # db.session.commit()
            # response_json = jsonify(luckynum=luckynum.serialize())
            return (response,201)


            