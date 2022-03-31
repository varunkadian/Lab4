import flask
import pickle
import pandas as pd

with open(f'model/model.pkl','rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])    

def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))

    if flask.request.method == 'POST':

        Weight = flask.request.form['Weight']
        Length1 = flask.request.form['Length1']
        Length2 = flask.request.form['Length2']
        Length3 = flask.request.form['Length3']
        Height = flask.request.form['Height']
        Width = flask.request.form['Width']

        input_variables = pd.DataFrame([[Weight, Length1, Length2, Length3, Height, Width]],columns=['Weight', 'Length1', 'Length2', 'Length3', 'Height', 'Width'],dtype=float)
        prediction = model.predict(input_variables) [0]

        return flask.render_template('main.html',original_input={'Weight':Weight, 'Length1':Length1, 'Length2':Length2, 'Length3':Length3, 'Height':Height, 'Width':Width}, result=prediction,)
    
if __name__ == '__main__':
    app.run(debug=True)