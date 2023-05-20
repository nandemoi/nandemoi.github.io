from flask import Flask, send_file

app = Flask(__name__)

@app.route('/open_pdf')
def open_pdf():
    return """
    <script>
        window.open('/question', '題目');
    </script>
    """

@app.route('/display_pdf')
def display_pdf():
    return send_file(url_for ('static', filename=f"qs/01q.pdf"), mimetype='application/pdf')

if __name__ == '__main__':
    app.run()
