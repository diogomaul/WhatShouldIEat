from flask import Flask, request, redirect, url_for, Response, render_template
import random
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        action = request.form['actions']
        return redirect(action)
    else:
        return '''
            <form method="post" action="">
                <label for="actions">What would you like to do today?</label>
                <select id="actions" name="actions">
                    <option value="/getSuggestion">Get a suggestion</option>
                    <option value="/addItem">Add an item</option>
                    <option value="/removeItem">Remove an item</option>
                    <option value="/listItems">List items</option>
                </select>
                <input type="submit" value="Submit">
            </form>
        '''
            
@app.route('/getSuggestion', methods=['GET','POST'])
def getSuggestion():

    now = datetime.datetime.now()
    hour = now.hour

    if hour > 18:
        snacks = ['Banana and Granola', 'Nuts', 'Mini Carrots and Hummus', 'Popcorn', 'cookies', 'any fruit']
        suggestion = random.choice(snacks)
        return 'You should eat ' + suggestion
    else:
        return '''
            <form method="post" action="/dinner">
                <H1>It\'s past 6 pm, time for dinner!</H1>
                <br>
                <label>Do you feel like cooking?</label>
                <input type="radio" name="option" value="y">Yes
                <input type="radio" name="option" value="n">No
                <input type="submit" value="Submit">
            </form>
        '''

@app.route('/dinner', methods=['GET','POST'])
def dinner():
    dinner = ['Crepioca', 'Tuna Wrap', 'Hamburguer Flights']
    takeOut = ['Domino\'s', 'Papi Shawarma', 'Burguer Priest', 'Mandarim 2 Go']

    option = request.form['option']

    if option == 'y':
        suggestion = random.choice(dinner)
        return ('You should cook ' + suggestion + ' for dinner!')
    else:
        suggestion = (random.choice(takeOut))
        return ('You should order ' + suggestion + ' for dinner!')

@app.route('/addItem', methods=['GET','POST'])
def addItem():
    if request.method == 'POST':
        action = request.form['actions']
        return redirect(action)
    else:
        return '''
            <form method="post" action="">
                <label for="actions">What would you like to add?</label>
                <select id="actions" name="actions">
                    <option value="/addSnack">Snack</option>
                    <option value="/addDinner">Dinner</option>
                    <option value="/addTakeOut">Take Out</option>
                </select>
                <input type="submit" value="Submit">
            </form>
        '''
    
@app.route('/removeItem', methods=['GET','POST'])
def removeItem():
    if request.method == 'POST':
        action = request.form['actions']
        return redirect(action)
    else:
        return '''
            <form method="post" action="">
                <label for="actions">What would you like to remove?</label>
                <select id="actions" name="actions">
                    <option value="/removeSnack">Snack</option>
                    <option value="/removeDinner">Dinner</option>
                    <option value="/removeTakeOut">Take Out</option>
                </select>
                <input type="submit" value="Submit">
            </form>
        '''

@app.route('/listItems', methods=['GET','POST'])
def listItems():
    if request.method == 'POST':
        action = request.form['actions']
        return redirect(action)
    else:
        return '''
            <form method="post" action="">
                <label for="actions">Which list do you want to see?</label>
                <select id="actions" name="actions">
                    <option value="/snacksList">Snacks</option>
                    <option value="/dinnerList">Dinner</option>
                    <option value="/takeOutList">Take Out</option>
                </select>
                <input type="submit" value="Submit">
            </form>
        '''

@app.route('/snacksList', methods=['GET'])
def snacksList():
    snacks = ['Banana and Granola', 'Nuts', 'Mini Carrots and Hummus', 'Popcorn', 'Cookies', 'Any Fruit']
    snack_table = '<table><thead><tr><th></th></tr></thead><tbody>'
    for snack in snacks:
        snack_table += f'<tr><td>{snack}</td></tr>'
    snack_table += '</tbody></table>'
    return f'<body><h1>Snacks</h1>{snack_table}</body>'

@app.route('/dinnerList', methods=['GET'])
def dinnerList():
    dinner = ['Crepioca', 'Tuna Wrap', 'Hamburguer Flights']
    dinner_table = '<table><thead><tr><th></th></tr></thead><tbody>'
    for dish in dinner:
        dinner_table += f'<tr><td>{dish}</td></tr>'
    dinner_table += '</tbody></table>'
    return f'<body><h1>Dinner</h1>{dinner_table}</body>'


@app.route('/takeOutList', methods=['GET'])
def takeOutList():
    takeOut = ['Domino\'s', 'Papi Shawarma', 'Burguer Priest', 'Mandarim 2 Go']
    takeOut_table = '<table><thead><tr><th></th></tr></thead><tbody>'
    for restaurant in takeOut:
        takeOut_table += f'<tr><td>{restaurant}</td></tr>'
    takeOut_table += '</tbody></table>'
    return f'<body><h1>Take Out</h1>{takeOut_table}</body>'


if __name__ == '__main__':
    app.run()