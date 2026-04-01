# database.py

import mysql.connector
from mysql.connector import Error


class JobTrackerDB:
    def __init__(
        self,
        host="localhost",
        user="root",
        password="root1234",
        database="job_tracker",
    ):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    # -----------------------------
    # Connection helpers
    # -----------------------------
    def connect(self):
        if self.conn is None or not self.conn.is_connected():
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            self.cursor = self.conn.cursor(dictionary=True)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn and self.conn.is_connected():
            self.conn.close()
        self.cursor = None
        self.conn = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.close()

    # -----------------------------
    # Companies
    # -----------------------------
    def get_all_companies(self):
        self.connect()
        query = """
            SELECT company_id, company_name, industry, website,
                   city, state, notes, created_at
            FROM companies
            ORDER BY company_name
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_company_by_id(self, company_id):
        self.connect()
        query = """
            SELECT company_id, company_name, industry, website,
                   city, state, notes, created_at
            FROM companies
            WHERE company_id = %s
        """
        self.cursor.execute(query, (company_id,))
        return self.cursor.fetchone()

    def add_company(self, company_name, industry, website, city, state, notes):
        self.connect()
        query = """
            INSERT INTO companies
                (company_name, industry, website, city, state, notes)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(
            query, (company_name, industry, website, city, state, notes)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def update_company(self, company_id, company_name, industry, website, city, state, notes):
        self.connect()
        query = """
            UPDATE companies
            SET company_name = %s,
                industry = %s,
                website = %s,
                city = %s,
                state = %s,
                notes = %s
            WHERE company_id = %s
        """
        self.cursor.execute(
            query,
            (company_name, industry, website, city, state, notes, company_id),
        )
        self.conn.commit()
        return self.cursor.rowcount

    def delete_company(self, company_id):
        self.connect()
        query = "DELETE FROM companies WHERE company_id = %s"
        self.cursor.execute(query, (company_id,))
        self.conn.commit()
        return self.cursor.rowcount

    # -----------------------------
    # Jobs
    # -----------------------------
    def get_all_jobs(self):
        """
        Returns jobs joined with company name.
        Assumes jobs table has a job_skills TEXT column.
        """
        self.connect()
        query = """
            SELECT
                j.job_id,
                j.company_id,
                j.job_title,
                j.job_description,
                j.salary_min,
                j.salary_max,
                j.job_type,
                j.posting_url,
                j.date_posted,
                j.is_active,
                j.created_at,
                j.job_skills,
                c.company_name
            FROM jobs j
            JOIN companies c ON j.company_id = c.company_id
            ORDER BY j.created_at DESC
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_job_by_id(self, job_id):
        self.connect()
        query = """
            SELECT
                j.job_id,
                j.company_id,
                j.job_title,
                j.job_description,
                j.salary_min,
                j.salary_max,
                j.job_type,
                j.posting_url,
                j.date_posted,
                j.is_active,
                j.created_at,
                j.job_skills,
                c.company_name
            FROM jobs j
            JOIN companies c ON j.company_id = c.company_id
            WHERE j.job_id = %s
        """
        self.cursor.execute(query, (job_id,))
        return self.cursor.fetchone()

    def add_job(
        self,
        company_id,
        job_title,
        job_description,
        salary_min,
        salary_max,
        job_type,
        posting_url,
        date_posted,
        job_skills,
        is_active=1,
    ):
        self.connect()
        query = """
            INSERT INTO jobs
                (company_id, job_title, job_description,
                 salary_min, salary_max, job_type,
                 posting_url, date_posted, is_active, job_skills)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(
            query,
            (
                company_id,
                job_title,
                job_description,
                salary_min,
                salary_max,
                job_type,
                posting_url,
                date_posted,
                is_active,
                job_skills,
            ),
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def update_job(
        self,
        job_id,
        company_id,
        job_title,
        job_description,
        salary_min,
        salary_max,
        job_type,
        posting_url,
        date_posted,
        is_active,
        job_skills,
    ):
        self.connect()
        query = """
            UPDATE jobs
            SET company_id = %s,
                job_title = %s,
                job_description = %s,
                salary_min = %s,
                salary_max = %s,
                job_type = %s,
                posting_url = %s,
                date_posted = %s,
                is_active = %s,
                job_skills = %s
            WHERE job_id = %s
        """
        self.cursor.execute(
            query,
            (
                company_id,
                job_title,
                job_description,
                salary_min,
                salary_max,
                job_type,
                posting_url,
                date_posted,
                is_active,
                job_skills,
                job_id,
            ),
        )
        self.conn.commit()
        return self.cursor.rowcount

    def delete_job(self, job_id):
        self.connect()
        query = "DELETE FROM jobs WHERE job_id = %s"
        self.cursor.execute(query, (job_id,))
        self.conn.commit()
        return self.cursor.rowcount

    def get_jobs_by_salary(self, min_salary):
        self.connect()
        query = """
            SELECT
                j.job_id,
                j.company_id,
                j.job_title,
                j.salary_min,
                j.salary_max,
                j.job_type,
                j.posting_url,
                j.date_posted,
                j.is_active,
                j.job_skills,
                c.company_name
            FROM jobs j
            JOIN companies c ON j.company_id = c.company_id
            WHERE j.salary_min >= %s
            ORDER BY j.salary_min
        """
        self.cursor.execute(query, (min_salary,))
        return self.cursor.fetchall()

    # -----------------------------
    # Applications
    # -----------------------------
    def get_all_applications(self):
        """
        Returns applications joined with job + company.
        """
        self.connect()
        query = """
            SELECT
                a.application_id,
                a.job_id,
                a.application_date,
                a.status,
                a.resume_version,
                a.cover_letter_sent,
                a.response_date,
                a.interview_date,
                a.notes,
                a.created_at,
                j.job_title,
                j.job_skills,
                c.company_name
            FROM applications a
            JOIN jobs j ON a.job_id = j.job_id
            JOIN companies c ON j.company_id = c.company_id
            ORDER BY a.application_date DESC, a.created_at DESC
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_application_by_id(self, application_id):
        self.connect()
        query = """
            SELECT
                a.application_id,
                a.job_id,
                a.application_date,
                a.status,
                a.resume_version,
                a.cover_letter_sent,
                a.response_date,
                a.interview_date,
                a.notes,
                a.created_at,
                j.job_title,
                j.job_skills,
                c.company_name
            FROM applications a
            JOIN jobs j ON a.job_id = j.job_id
            JOIN companies c ON j.company_id = c.company_id
            WHERE a.application_id = %s
        """
        self.cursor.execute(query, (application_id,))
        return self.cursor.fetchone()

    def add_application(
        self,
        job_id,
        application_date,
        status="Applied",
        resume_version=None,
        cover_letter_sent=False,
        response_date=None,
        interview_date=None,
        notes=None,
    ):
        self.connect()
        query = """
            INSERT INTO applications
                (job_id, application_date, status,
                 resume_version, cover_letter_sent,
                 response_date, interview_date, notes)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(
            query,
            (
                job_id,
                application_date,
                status,
                resume_version,
                int(bool(cover_letter_sent)),
                response_date,
                interview_date,
                notes,
            ),
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def update_application(
        self,
        application_id,
        job_id,
        application_date,
        status,
        resume_version,
        cover_letter_sent,
        response_date,
        interview_date,
        notes,
    ):
        self.connect()
        query = """
            UPDATE applications
            SET job_id = %s,
                application_date = %s,
                status = %s,
                resume_version = %s,
                cover_letter_sent = %s,
                response_date = %s,
                interview_date = %s,
                notes = %s
            WHERE application_id = %s
        """
        self.cursor.execute(
            query,
            (
                job_id,
                application_date,
                status,
                resume_version,
                int(bool(cover_letter_sent)),
                response_date,
                interview_date,
                notes,
                application_id,
            ),
        )
        self.conn.commit()
        return self.cursor.rowcount

    def update_application_status(self, application_id, status):
        self.connect()
        query = """
            UPDATE applications
            SET status = %s
            WHERE application_id = %s
        """
        self.cursor.execute(query, (status, application_id))
        self.conn.commit()
        return self.cursor.rowcount

    def delete_application(self, application_id):
        self.connect()
        query = "DELETE FROM applications WHERE application_id = %s"
        self.cursor.execute(query, (application_id,))
        self.conn.commit()
        return self.cursor.rowcount

    # -----------------------------
    # Contacts
    # -----------------------------
    def get_all_contacts(self):
        self.connect()
        query = """
            SELECT
                ct.contact_id,
                ct.company_id,
                ct.first_name,
                ct.last_name,
                ct.email,
                ct.phone,
                ct.job_title,
                ct.linkedin_url,
                ct.notes,
                ct.created_at,
                c.company_name
            FROM contacts ct
            JOIN companies c ON ct.company_id = c.company_id
            ORDER BY c.company_name, ct.last_name, ct.first_name
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_contact_by_id(self, contact_id):
        self.connect()
        query = """
            SELECT
                ct.contact_id,
                ct.company_id,
                ct.first_name,
                ct.last_name,
                ct.email,
                ct.phone,
                ct.job_title,
                ct.linkedin_url,
                ct.notes,
                ct.created_at,
                c.company_name
            FROM contacts ct
            JOIN companies c ON ct.company_id = c.company_id
            WHERE ct.contact_id = %s
        """
        self.cursor.execute(query, (contact_id,))
        return self.cursor.fetchone()

    def add_contact(
        self,
        company_id,
        first_name,
        last_name,
        email,
        phone,
        job_title,
        linkedin_url,
        notes,
    ):
        self.connect()
        query = """
            INSERT INTO contacts
                (company_id, first_name, last_name,
                 email, phone, job_title, linkedin_url, notes)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(
            query,
            (
                company_id,
                first_name,
                last_name,
                email,
                phone,
                job_title,
                linkedin_url,
                notes,
            ),
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def update_contact(
        self,
        contact_id,
        company_id,
        first_name,
        last_name,
        email,
        phone,
        job_title,
        linkedin_url,
        notes,
    ):
        self.connect()
        query = """
            UPDATE contacts
            SET company_id = %s,
                first_name = %s,
                last_name = %s,
                email = %s,
                phone = %s,
                job_title = %s,
                linkedin_url = %s,
                notes = %s
            WHERE contact_id = %s
        """
        self.cursor.execute(
            query,
            (
                company_id,
                first_name,
                last_name,
                email,
                phone,
                job_title,
                linkedin_url,
                notes,
                contact_id,
            ),
        )
        self.conn.commit()
        return self.cursor.rowcount

    def delete_contact(self, contact_id):
        self.connect()
        query = "DELETE FROM contacts WHERE contact_id = %s"
        self.cursor.execute(query, (contact_id,))
        self.conn.commit()
        return self.cursor.rowcount
