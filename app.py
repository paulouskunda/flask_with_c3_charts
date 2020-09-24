# web application entry file

# import the required libraries
from flask import Flask, render_template, send_file

# initialize the flask application
app = Flask(__name__)


# create the home route
@app.route('/')
def home():
    return render_template('index.html')


# create the route to provide the csv file
@app.route('/provideCSV')
def provide_csv():
    # get the path of the file saved in the data folder
    path = send_file("data/data.csv", as_attachment=True)
    return path


# create the entry point
if __name__ == "__main__":
    app.run(port=5000, debug=True)
