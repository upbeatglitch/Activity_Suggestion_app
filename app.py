import os
import random
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "a_simple_secret_key")

# --- Activity Suggestion Data ---
JOB_SUGGESTIONS = {
    'war': ['great axe only','dual wield war','great sword crit build'],
    'mnk': ['25th degree black belt','staff mnk','def no tank trust','attack with tank trust'],
    'rdm': ['additional effect RDM','RDM fast cast nukes','Oat 2-4 + SC + MB'],
    'thf': ['shark attack with selhteus','triple attack nin','thf/rng'],
    'whm': ['Club DMG for kills','holy mb build','healing whm'],
    'blm': ['Wind nukes only','scythe blm','worms in adoulin'],
    'pld': ['cap exp','dagger AoE','sword shield melee'],
    'drk': ['great axe dark knight','dual wield drk','drk/thf'],
    'rng': ['point blank gun build','to get what you want bow build','melee for tp'],
    'bst': ['AoE','Charm bauild','Nukumi set build'],
    'brd': ['Dharp no gear swaps','as strong as you can be','savage build','Virelai brd'],
    'smn': ['Leviathan SMN','Dark Elemental build','dark element elements'],
    'blu': ['CDC','AoE','homam(dissiverment) style'],
    'pup': ['Stringing Pummel + arcuballista','naked harlequin','dagger pup'],
    'cor': ['savage','gun','adoulin worms'],
    'drg': ['drg/pld sword/shield build','dragoon/warrior max dmg','spear max damage'],
    'sch': ['surgical kills','melee sch','healing sch'],
    'geo': ['AoE with sch magic','melee','buffs only'],
    'nin': ['Detonation(home) ninja','nin/rng','ele wheel ninja'],
    'run': ['savage blade build','great sword','AoE'],
    'sam': ['sam/rng','jinpu','great katana attack build'],
    'dnc': ['-def build','just play for fun','no tank'],
    'gil': ['fishing','digging','nm camping'],
    'nostalgia': ['bcnm 20 wings of fury','pirates chart','chocobo to jeuno'],
    'runs': ['windurst to jeuno','qufim','sandy to hotspring']
}

@app.route('/', methods=['GET', 'POST'])
def index():
    suggestion = None
    if request.method == 'POST':
        # Get input from the HTML form
        job_abbr = request.form.get('job_abbr', '').lower()
        
        # Look up the suggestion
        if job_abbr in JOB_SUGGESTIONS:
            suggestion = random.choice(JOB_SUGGESTIONS[job_abbr])
        else:
            suggestion = "Invalid job abbreviation or category. Try 'war', 'mnk', or 'gil', etc."

    # Render the HTML template, passing the suggestion to be displayed
    return render_template('index.html', suggestion=suggestion)

if __name__ == '__main__':
    # Use a port other than 5000 if running the sim app too
    app.run(debug=True, port=5001)