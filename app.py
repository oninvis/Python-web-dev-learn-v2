from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)

@app.route('/')
def hello_jovian():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name="Jovian")  # Pass `jobs=jobs`

@app.route("/jobs")
def list_jobs():
    jobs = load_jobs_from_db()  # Retrieve jobs for the API route as well
    return jsonify(jobs)  # Return the jobs as JSON

if __name__ == '__main__':
    app.run(debug=True)
