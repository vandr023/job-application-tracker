# app.py

from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import JobTrackerDB

app = Flask(__name__)
db = JobTrackerDB()
db.connect()

# -----------------------------
# Home / Dashboard
# -----------------------------
@app.route("/")
@app.route("/dashboard")
def dashboard():
    companies = db.get_all_companies()
    jobs = db.get_all_jobs()
    applications = db.get_all_applications()
    contacts = db.get_all_contacts()

    total_companies = len(companies)
    total_jobs = len(jobs)
    total_applications = len(applications)
    total_contacts = len(contacts)

    return render_template(
        "dashboard.html",
        total_companies=total_companies,
        total_jobs=total_jobs,
        total_applications=total_applications,
        total_contacts=total_contacts,
    )

# -----------------------------
# Companies (HTML)
# -----------------------------
@app.route("/companies")
def companies():
    companies = db.get_all_companies()
    return render_template("companies.html", companies=companies)


@app.route("/companies/add", methods=["POST"])
def add_company():
    company_name = request.form.get("company_name")
    industry = request.form.get("industry")
    website = request.form.get("website")
    city = request.form.get("city")
    state = request.form.get("state")
    notes = request.form.get("notes")

    db.add_company(company_name, industry, website, city, state, notes)
    return redirect(url_for("companies"))


@app.route("/companies/edit/<int:company_id>")
def edit_company(company_id):
    company = db.get_company_by_id(company_id)
    return render_template("edit_company.html", company=company)


@app.route("/companies/update/<int:company_id>", methods=["POST"])
def update_company(company_id):
    company_name = request.form.get("company_name")
    industry = request.form.get("industry")
    website = request.form.get("website")
    city = request.form.get("city")
    state = request.form.get("state")
    notes = request.form.get("notes")

    db.update_company(company_id, company_name, industry, website, city, state, notes)
    return redirect(url_for("companies"))


@app.route("/companies/delete/<int:company_id>", methods=["POST"])
def delete_company(company_id):
    db.delete_company(company_id)
    return redirect(url_for("companies"))

# -----------------------------
# Jobs (HTML)
# -----------------------------
@app.route("/jobs")
def jobs():
    jobs = db.get_all_jobs()
    companies = db.get_all_companies()
    return render_template("jobs.html", jobs=jobs, companies=companies)


@app.route("/jobs/add", methods=["POST"])
def add_job():
    company_id = request.form.get("company_id")
    job_title = request.form.get("job_title")
    job_description = request.form.get("job_description")
    salary_min = request.form.get("salary_min") or None
    salary_max = request.form.get("salary_max") or None
    job_type = request.form.get("job_type")
    posting_url = request.form.get("posting_url")
    date_posted = request.form.get("date_posted") or None
    job_skills = request.form.get("job_skills") or ""

    db.add_job(
        company_id=company_id,
        job_title=job_title,
        job_description=job_description,
        salary_min=salary_min,
        salary_max=salary_max,
        job_type=job_type,
        posting_url=posting_url,
        date_posted=date_posted,
        job_skills=job_skills,
    )
    return redirect(url_for("jobs"))


@app.route("/jobs/edit/<int:job_id>")
def edit_job(job_id):
    job = db.get_job_by_id(job_id)
    companies = db.get_all_companies()
    return render_template("edit_job.html", job=job, companies=companies)


@app.route("/jobs/update/<int:job_id>", methods=["POST"])
def update_job(job_id):
    company_id = request.form.get("company_id")
    job_title = request.form.get("job_title")
    job_description = request.form.get("job_description")
    salary_min = request.form.get("salary_min") or None
    salary_max = request.form.get("salary_max") or None
    job_type = request.form.get("job_type")
    posting_url = request.form.get("posting_url")
    date_posted = request.form.get("date_posted") or None
    is_active = 1 if request.form.get("is_active", "1") == "1" else 0
    job_skills = request.form.get("job_skills") or ""

    db.update_job(
        job_id=job_id,
        company_id=company_id,
        job_title=job_title,
        job_description=job_description,
        salary_min=salary_min,
        salary_max=salary_max,
        job_type=job_type,
        posting_url=posting_url,
        date_posted=date_posted,
        is_active=is_active,
        job_skills=job_skills,
    )
    return redirect(url_for("jobs"))


@app.route("/jobs/delete/<int:job_id>", methods=["POST"])
def delete_job(job_id):
    db.delete_job(job_id)
    return redirect(url_for("jobs"))

# -----------------------------
# Applications (HTML)
# -----------------------------
@app.route("/applications")
def applications():
    applications = db.get_all_applications()
    jobs = db.get_all_jobs()
    # Status options per rubric
    status_options = ["Applied", "Screening", "Interview", "Offer", "Rejected", "Withdrawn"]
    return render_template(
        "applications.html",
        applications=applications,
        jobs=jobs,
        status_options=status_options,
    )


@app.route("/applications/add", methods=["POST"])
def add_application_html():
    job_id = request.form.get("job_id")
    application_date = request.form.get("application_date")
    status = request.form.get("status") or "Applied"
    resume_version = request.form.get("resume_version")
    cover_letter_sent = bool(request.form.get("cover_letter_sent"))
    response_date = request.form.get("response_date") or None
    interview_date = request.form.get("interview_date") or None
    notes = request.form.get("notes")

    db.add_application(
        job_id=job_id,
        application_date=application_date,
        status=status,
        resume_version=resume_version,
        cover_letter_sent=cover_letter_sent,
        response_date=response_date,
        interview_date=interview_date,
        notes=notes,
    )
    return redirect(url_for("applications"))


@app.route("/applications/edit/<int:application_id>")
def edit_application(application_id):
    application = db.get_application_by_id(application_id)
    jobs = db.get_all_jobs()
    status_options = ["Applied", "Screening", "Interview", "Offer", "Rejected", "Withdrawn"]
    return render_template(
        "edit_application.html",
        application=application,
        jobs=jobs,
        status_options=status_options,
    )


@app.route("/applications/update/<int:application_id>", methods=["POST"])
def update_application_html(application_id):
    job_id = request.form.get("job_id")
    application_date = request.form.get("application_date")
    status = request.form.get("status") or "Applied"
    resume_version = request.form.get("resume_version")
    cover_letter_sent = bool(request.form.get("cover_letter_sent"))
    response_date = request.form.get("response_date") or None
    interview_date = request.form.get("interview_date") or None
    notes = request.form.get("notes")

    db.update_application(
        application_id=application_id,
        job_id=job_id,
        application_date=application_date,
        status=status,
        resume_version=resume_version,
        cover_letter_sent=cover_letter_sent,
        response_date=response_date,
        interview_date=interview_date,
        notes=notes,
    )
    return redirect(url_for("applications"))


@app.route("/applications/delete/<int:application_id>", methods=["POST"])
def delete_application_html(application_id):
    db.delete_application(application_id)
    return redirect(url_for("applications"))

# -----------------------------
# Contacts (HTML)
# -----------------------------
@app.route("/contacts")
def contacts():
    contacts = db.get_all_contacts()
    companies = db.get_all_companies()
    return render_template("contacts.html", contacts=contacts, companies=companies)


@app.route("/contacts/add", methods=["POST"])
def add_contact():
    company_id = request.form.get("company_id")
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    job_title = request.form.get("job_title")
    linkedin_url = request.form.get("linkedin_url")
    notes = request.form.get("notes")

    db.add_contact(
        company_id=company_id,
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        job_title=job_title,
        linkedin_url=linkedin_url,
        notes=notes,
    )
    return redirect(url_for("contacts"))


@app.route("/contacts/edit/<int:contact_id>")
def edit_contact(contact_id):
    contact = db.get_contact_by_id(contact_id)
    companies = db.get_all_companies()
    return render_template("edit_contact.html", contact=contact, companies=companies)


@app.route("/contacts/update/<int:contact_id>", methods=["POST"])
def update_contact(contact_id):
    company_id = request.form.get("company_id")
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    job_title = request.form.get("job_title")
    linkedin_url = request.form.get("linkedin_url")
    notes = request.form.get("notes")

    db.update_contact(
        contact_id=contact_id,
        company_id=company_id,
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        job_title=job_title,
        linkedin_url=linkedin_url,
        notes=notes,
    )
    return redirect(url_for("contacts"))


@app.route("/contacts/delete/<int:contact_id>", methods=["POST"])
def delete_contact(contact_id):
    db.delete_contact(contact_id)
    return redirect(url_for("contacts"))

# -----------------------------
# Jobs API (JSON example)
# -----------------------------
@app.route("/jobs/salary/<int:min_salary>", methods=["GET"])
def get_jobs_by_salary(min_salary):
    jobs = db.get_jobs_by_salary(min_salary)
    return jsonify(jobs)

# -----------------------------
# Job Match (HTML)
# -----------------------------
@app.route("/match", methods=["GET", "POST"])
def match_jobs():
    results = []
    user_skills_raw = ""

    if request.method == "POST":
        user_skills_raw = request.form.get("skills", "")
        user_skills = [
            s.strip().lower() for s in user_skills_raw.split(",") if s.strip()
        ]

        jobs = db.get_all_jobs()

        for job in jobs:
            raw_required = job.get("job_skills") or ""
            required_skills = [
                s.strip().lower() for s in raw_required.split(",") if s.strip()
            ]

            if not required_skills:
                match_percent = 0
                matched = []
                missing = []
            else:
                matched = [s for s in user_skills if s in required_skills]
                missing = [s for s in required_skills if s not in matched]
                match_percent = int((len(matched) / len(required_skills)) * 100)

            results.append(
                {
                    "job_title": job["job_title"],
                    "company_name": job["company_name"],
                    "matched": matched,
                    "missing": missing,
                    "match_percent": match_percent,
                    "required_count": len(required_skills),
                    "matched_count": len(matched),
                }
            )

        results.sort(key=lambda x: x["match_percent"], reverse=True)

    return render_template(
        "job_match.html",
        results=results,
        user_skills=user_skills_raw,
    )

# -----------------------------
# Run the App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)

