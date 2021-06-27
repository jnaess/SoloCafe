from flask import Flask, render_template, request
from forms import SignUpForm
import numpy as np
import pandas as pd

#mackenzie made me make a change
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
  Displays cafe dashboard (loads today's orders)

  TODO:
  -hidden option for delviered orders
  -transfer orders
  -pop up for more order details

  add link to each column in a table --> https://stackoverflow.com/questions/59438723/flask-make-row-of-dataframe-to-html-clickable
  """
    #queue all orders for the day
    unmade, undelivered, delivered = retrieve_orders()

    #currently delivered orders are not displayed
    return render_template(
        "cafe.html",
        unmade=[unmade.to_html(classes='data', header='true')],
        undelivered=[undelivered.to_html(classes='data', header='true')])

@app.route('/manager')
def manager():
    """
  The dashboard for the cafe manager
  """
    return render_template("manager.html")

@app.route('/user')
def user():
    """
  The dashboard for the cafe manager
  """
    return render_template("user.html")

@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    """
  test manager form
  """

    form = SignUpForm()
    if form.is_submitted():
      result = request.form
      return render_template('user.html', result = result)
    return render_template("signup.html", form=form)

@app.route('/customer')
def customer():
    """
  home page for customer. they should be able to order directly from here
  """
    return render_template("customer.html")

def retrieve_orders():
    """
  Retrieves all orders for the current day. Splits them into a dataframe of unmade, undelivered, and delivered orders

  input: none
  returns: 
    unmade, df
    undelivered, df
    delivered, df
  """
    unmade = pd.DataFrame({
        "name": ["Ms. J", "Ms. Katharine", "Mr. Coolio"],
        "period": [2, 2, 3]
    })

    undelivered = pd.DataFrame({"name": ["Mr. Cc"], "period": [2]})

    delivered = pd.DataFrame({"name": ["Ms. Jj", "Ms. Kk"], "period": [1, 1]})

    return unmade, undelivered, delivered

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', debug=True, port=8080)
