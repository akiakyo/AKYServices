from flask import Flask, render_template_string

app = Flask(__name__)
transcripts = {}  # In-memory store

@app.route("/ticket/<ticket_id>")
def show_ticket(ticket_id):
    html = transcripts.get(ticket_id)
    if not html:
        return "Transcript not found", 404
    return render_template_string(html)

def save_transcript(ticket_id, html):
    transcripts[ticket_id] = html
