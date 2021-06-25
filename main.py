from flask import Flask, render_template

# Create a flask app
app = Flask(__name__, template_folder='templates', static_folder='static')


# Index page (now using the index.html file)
@app.route('/')
def index():
  """
  This is the home page. 
  login option (either as a cafe or as a customer)
  """
  return render_template('index.html')

@app.route('/cafe')
def cafe():
  """
  home page for cafe (automatically cafe dashboard)
  """
  return render_template("cafe.html")

@app.route('/customer')
def customer():
  """
  home page for customer. they should be able to order directly from here
  """
  return render_template("customer.html")
  
if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', debug=True, port=8080)
