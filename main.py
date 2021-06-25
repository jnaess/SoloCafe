from flask import Flask, render_template
import numpy as np
import pandas as pd

# Create a flask app
app = Flask(__name__, template_folder='templates', static_folder='static')


# Index page (now using the index.html file)
@app.route('/', methods=("POST", "GET"))
def index():
    """
  This is the home page. 
  login option (either as a cafe or as a customer)
  this is also the page they are taken back to when they logout
  """
    return render_template('index.html')


@app.route('/cafe')
def cafe():
    """
  This is the cafe dashboard
  """

    uncompleted = pd.DataFrame({
        "name": ["Ms. J", "Ms. Katharine", "Mr. Coolio"],
        "period": [2, 2, 3]
    })

    completed = pd.DataFrame({
        "name": ["Ms. Jj", "Ms. Kk", "Mr. Cc"],
        "period": [1, 1, 2]
    })

    #this will be loaded as a query for all
    #orders = order_querry

    return render_template(
        "cafe.html",
        uncompleted=[uncompleted.to_html(classes='data', header='true')],
        completed=[completed.to_html(classes='data', header='true')])


@app.route('/manager')
def manager():
    """
  The dashboard for the cafe manager
  """
    return render_template("manager.html")


@app.route('/customer')
def customer():
    """
  home page for customer. they should be able to order directly from here
  """
    return render_template("customer.html")


if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', debug=True, port=8080)
