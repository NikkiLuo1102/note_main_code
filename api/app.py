from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import requests

app = Flask(__name__)

API_URL = "http://127.0.0.1:5000/"
COLORS = ['Red', 'Green', 'Blue', 'Yellow', 'Orange']

def send_request(endpoint, params=None):
    try:
        response = requests.get(API_URL + endpoint, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    user_id = request.args.get('user_id')
    if user_id:
        notes = fetch_notes(user_id)
    else:
        notes = []

    if request.method == 'POST':
        action = request.form['action']
        if action == 'add':
            color = request.form['color']
            content = request.form['content']
            add_note(user_id, color, content)
        elif action == 'delete':
            index = int(request.form['index'])
            note_id = notes[index]['note_id']
            delete_note(note_id)
            del notes[index]
        elif action == 'edit':
            index = int(request.form['index'])
            color = request.form['color']
            content = request.form['content']
            update_note(user_id, notes[index]['note_id'], color, content)
        return redirect(url_for('index', user_id=user_id))
    
    return render_template('index.html', colors=COLORS, notes=notes)

def fetch_notes(user_id):
    response = send_request("retrieve_data", params={"user_id": user_id})
    if response:
        return response
    return []

def add_note(user_id, color, content):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {"user_id": user_id, "color": color, "content": content, "time": current_time}
    send_request("create_data", params=data)

def delete_note(note_id):
    send_request("delete_data", params={"note_id": note_id})

def update_note(user_id, note_id, color, content):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {"user_id": user_id, "note_id": note_id, "color": color, "content": content, "time": current_time}
    send_request("update_data", params=data)

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)






