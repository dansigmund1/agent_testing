from flask import Flask, jsonify, render_template, request
from scripts.check_setup import CheckSetup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/run-checks', methods=['POST'])
def run_script():
    cs = CheckSetup()
    dbs = cs.db_connect()
    wfs = cs.get_workflows()
    return cs.generate_report(dbs, wfs)

if __name__ == '__main__':
    app.run(debug=True)