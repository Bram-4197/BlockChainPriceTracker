

from flask import Flask
from cryptoPrice import start

  
  
app = Flask(__name__)
  
# Route for seeing a data
@app.route('/data')
def get_time():
  
    # Returning an api for showing in  reactjs
    return (
        
        start()
    )
  
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)

