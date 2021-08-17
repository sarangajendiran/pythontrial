from flask import Flask, render_template
import get_suites as gs
app = Flask(__name__)
@app.route('/')
def root():
    suite_data, bardata = gs.get_suites('Project DELTA E2E')
    # return str(suite_data)
    return render_template("index2.html", tempdata = suite_data, tempdata1 = bardata)

if __name__ == "__main__":
    app.run(host="PC12256.dialoggroup.internal", port=8080, debug=True)