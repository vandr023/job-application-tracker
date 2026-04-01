CREATE DATABASE  IF NOT EXISTS `job_tracker` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `job_tracker`;
-- MySQL dump 10.13  Distrib 8.0.45, for macos15 (arm64)
--
-- Host: localhost    Database: job_tracker
-- ------------------------------------------------------
-- Server version	9.6.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '1dcf7ef6-27e7-11f1-b2b7-74abfef8e07a:1-114';

--
-- Table structure for table `application_summary`
--

DROP TABLE IF EXISTS `application_summary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `application_summary` (
  `summary_id` int NOT NULL AUTO_INCREMENT,
  `company_name` varchar(100) DEFAULT NULL,
  `total_jobs` int DEFAULT NULL,
  `total_applications` int DEFAULT NULL,
  `avg_salary` decimal(10,2) DEFAULT NULL,
  `last_updated` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`summary_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `application_summary`
--

LOCK TABLES `application_summary` WRITE;
/*!40000 ALTER TABLE `application_summary` DISABLE KEYS */;
INSERT INTO `application_summary` VALUES (1,'Tech Solutions Inc',4,1,65000.00,'2026-03-27 02:38:13'),(2,'Data Analytics Corp',4,1,61250.00,'2026-03-27 02:38:13'),(3,'Cloud Systems LLC',3,1,78333.33,'2026-03-27 02:38:13'),(4,'Digital Innovations',4,2,60500.00,'2026-03-27 02:38:13'),(5,'Smart Tech Group',2,1,90000.00,'2026-03-27 02:38:13'),(6,'Test Company',0,0,NULL,'2026-03-27 02:38:13'),(7,'New Tech Corp',1,0,120000.00,'2026-03-27 02:38:13');
/*!40000 ALTER TABLE `application_summary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `applications`
--

DROP TABLE IF EXISTS `applications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `applications` (
  `application_id` int NOT NULL AUTO_INCREMENT,
  `job_id` int NOT NULL,
  `application_date` date NOT NULL,
  `status` varchar(30) DEFAULT 'Applied',
  `resume_version` varchar(50) DEFAULT NULL,
  `cover_letter_sent` tinyint(1) DEFAULT '0',
  `response_date` date DEFAULT NULL,
  `interview_date` datetime DEFAULT NULL,
  `notes` text,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`application_id`),
  KEY `job_id` (`job_id`),
  KEY `idx_app_status` (`status`),
  CONSTRAINT `applications_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`job_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `applications`
--

LOCK TABLES `applications` WRITE;
/*!40000 ALTER TABLE `applications` DISABLE KEYS */;
INSERT INTO `applications` VALUES (1,1,'2025-01-16','Rejected','v2.1',1,NULL,NULL,NULL,'2026-03-25 03:56:36'),(2,3,'2025-01-13','Screening','v2.1',1,NULL,NULL,NULL,'2026-03-25 03:56:36'),(3,4,'2025-01-09','Interview Completed','v2.0',0,NULL,NULL,NULL,'2026-03-25 03:56:36'),(4,5,'2025-01-15','Applied','v2.1',1,NULL,NULL,NULL,'2026-03-25 03:56:36'),(5,7,'2025-01-12','Phone Screen','v2.1',1,NULL,NULL,NULL,'2026-03-25 03:56:36'),(6,6,'2026-03-25','Applied','v3.0',1,NULL,NULL,NULL,'2026-03-25 16:33:46'),(7,8,'2026-03-28','Applied',NULL,0,NULL,NULL,NULL,'2026-03-29 00:33:59'),(8,11,'2026-03-28','Applied',NULL,0,NULL,NULL,NULL,'2026-03-29 00:34:45'),(9,11,'2026-03-28','Applied',NULL,0,NULL,NULL,NULL,'2026-03-29 00:36:40'),(10,14,'2026-03-28','Applied',NULL,0,NULL,NULL,NULL,'2026-03-29 00:37:02'),(11,15,'2026-03-28','Applied',NULL,0,NULL,NULL,NULL,'2026-03-29 00:40:15');
/*!40000 ALTER TABLE `applications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `companies`
--

DROP TABLE IF EXISTS `companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `companies` (
  `company_id` int NOT NULL AUTO_INCREMENT,
  `company_name` varchar(100) NOT NULL,
  `industry` varchar(50) DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `notes` text,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`company_id`),
  KEY `idx_company_industry` (`industry`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companies`
--

LOCK TABLES `companies` WRITE;
/*!40000 ALTER TABLE `companies` DISABLE KEYS */;
INSERT INTO `companies` VALUES (1,'Tech Solutions Inc','Technology','www.techsolutions.com','Miami','Florida',NULL,'2026-03-25 03:52:54'),(2,'Data Analytics Corp','Data Science','www.dataanalytics.com','Austin','Texas',NULL,'2026-03-25 03:52:54'),(3,'Cloud Systems LLC','Cloud Computing','www.cloudsystems.com','Seattle','Washington',NULL,'2026-03-25 03:52:54'),(4,'Digital Innovations','Software','www.digitalinnovations.com','San Francisca','California','Applied to Senior Developer position on 2026-03-25','2026-03-25 03:52:54'),(5,'Smart Tech Group','AI/ML','www.smarttech.com','Boston','Massachusetts',NULL,'2026-03-25 03:52:54'),(7,'New Tech Corp','Technology',NULL,'Denver','Colorado',NULL,'2026-03-25 16:05:18');
/*!40000 ALTER TABLE `companies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacts`
--

DROP TABLE IF EXISTS `contacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contacts` (
  `contact_id` int NOT NULL AUTO_INCREMENT,
  `company_id` int NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `job_title` varchar(100) DEFAULT NULL,
  `linkedin_url` varchar(200) DEFAULT NULL,
  `notes` text,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`contact_id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `contacts_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `companies` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts`
--

LOCK TABLES `contacts` WRITE;
/*!40000 ALTER TABLE `contacts` DISABLE KEYS */;
INSERT INTO `contacts` VALUES (1,1,'Sarah','Johnson','sjohnson@techsolutions.com',NULL,'HR Manager',NULL,NULL,'2026-03-25 03:58:16'),(2,2,'Michael','Chen','mchen@dataanalytics.com',NULL,'Technical Recruiter',NULL,NULL,'2026-03-25 03:58:16'),(3,3,'Emily','Williams','ewilliams@cloudsystems.com',NULL,'Hiring Manager',NULL,NULL,'2026-03-25 03:58:16'),(4,4,'David','Brown',NULL,NULL,'Senior Developer',NULL,NULL,'2026-03-25 03:58:16'),(5,5,'Lisa','Garcia','lgarcia@smarttech.com',NULL,'Talent Acquisition',NULL,NULL,'2026-03-25 03:58:16'),(6,7,'Jennifer','Martinez','jmartinez@newtechcorp.com',NULL,'CTO',NULL,NULL,'2026-03-25 16:22:01'),(7,4,'Robert','Kim','rkim@digitalinnovations.com',NULL,'Engineering Manager',NULL,NULL,'2026-03-25 16:34:37');
/*!40000 ALTER TABLE `contacts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs`
--

DROP TABLE IF EXISTS `jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobs` (
  `job_id` int NOT NULL AUTO_INCREMENT,
  `company_id` int NOT NULL,
  `job_title` varchar(100) NOT NULL,
  `job_description` text,
  `salary_min` decimal(10,2) DEFAULT NULL,
  `salary_max` decimal(10,2) DEFAULT NULL,
  `job_type` varchar(20) DEFAULT NULL,
  `posting_url` varchar(500) DEFAULT NULL,
  `date_posted` date DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `job_skills` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`job_id`),
  KEY `idx_job_title` (`job_title`),
  KEY `idx_company_type` (`company_id`,`job_type`),
  CONSTRAINT `jobs_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `companies` (`company_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs`
--

LOCK TABLES `jobs` WRITE;
/*!40000 ALTER TABLE `jobs` DISABLE KEYS */;
INSERT INTO `jobs` VALUES (1,1,'Software Developer','Seeking a Software Developer with experience in Python, SQL, Flask, Git, and REST API development. Responsibilities include building backend services and collaborating with cross-functional teams.',70000.00,90000.00,'Full-time',NULL,'2025-01-15',1,'2026-03-25 03:54:09','Python, Java, SQL, Git, REST APIs, HTML, CSS, JavaScript'),(2,1,'Database Administrator','Looking for a Database Administrator skilled in SQL, MySQL, database optimization, backups, indexing, and performance tuning. Experience with stored procedures and security best practices preferred.',75000.00,95000.00,'Full-time',NULL,'2025-01-10',1,'2026-03-25 03:54:09','SQL, MySQL, PostgreSQL, Backups, Indexing, Query Optimization, Security'),(3,2,'Data Analyst','Data Analyst role requiring SQL, Tableau, Excel, and Python. Responsibilities include building dashboards, analyzing datasets, and generating business insights.',65000.00,85000.00,'Full-time',NULL,'2025-01-12',1,'2026-03-25 03:54:09','SQL, Excel, Python, Tableau, Power BI, Data Cleaning, Data Visualization'),(4,3,'Cloud Engineer','Cloud Engineer needed with experience in AWS, Python, Linux, Docker, CI/CD pipelines, and cloud infrastructure automation.',80000.00,100000.00,'Full-time',NULL,'2025-01-08',1,'2026-03-25 03:54:09','AWS, Azure, Linux, Python, Docker, Kubernetes, Networking, CI/CD'),(5,4,'Junior Developer','Entry-level developer position requiring basic knowledge of Python, HTML, CSS, JavaScript, and Git. Will assist in building web applications and debugging code.',55000.00,70000.00,'Full-time',NULL,'2025-01-14',1,'2026-03-25 03:54:09','Python, JavaScript, HTML, CSS, Git, SQL, Debugging'),(6,4,'Senior Developer','Senior Developer with strong experience in Python, SQL, Flask, Docker, AWS, and system architecture. Will lead development teams and design scalable applications.',95000.00,120000.00,'Full-time',NULL,'2025-01-14',1,'2026-03-25 03:54:09','Python, Java, SQL, AWS, Docker, Kubernetes, Microservices, CI/CD'),(7,5,'ML Engineer','Machine Learning Engineer skilled in Python, TensorFlow, SQL, data preprocessing, model training, and deployment. Experience with cloud ML services preferred.',90000.00,115000.00,'Full-time',NULL,'2025-01-11',1,'2026-03-25 03:54:09','Python, TensorFlow, PyTorch, Pandas, NumPy, SQL, Machine Learning, Model Deployment'),(8,1,'QA Engineer','QA Engineer responsible for testing web applications, writing test cases, performing regression testing, and using tools such as Selenium, Python, and SQL.',60000.00,80000.00,'Full-time',NULL,'2025-01-05',1,'2026-03-25 04:23:03','Testing, QA Automation, Selenium, Python, Debugging, CI/CD, Test Cases'),(9,2,'Business Analyst','Business Analyst skilled in requirements gathering, SQL, process mapping, and stakeholder communication. Experience with Agile methodologies preferred.',65000.00,85000.00,'Full-time',NULL,'2025-01-06',1,'2026-03-25 04:23:03','SQL, Excel, Requirements Gathering, Data Analysis, Power BI, Communication'),(10,2,'Data Scientist','Data Scientist role requiring Python, SQL, machine learning, data modeling, and experience with libraries such as Pandas, NumPy, and Scikit-learn.',85000.00,110000.00,'Full-time',NULL,'2025-01-07',1,'2026-03-25 04:23:03','Python, SQL, Machine Learning, Pandas, NumPy, Statistics, Data Modeling'),(11,3,'DevOps Engineer','DevOps Engineer experienced with AWS, Docker, CI/CD pipelines, Linux, automation scripting, and infrastructure as code tools such as Terraform.',80000.00,105000.00,'Full-time',NULL,'2025-01-08',1,'2026-03-25 04:23:03','AWS, Docker, Kubernetes, Linux, CI/CD, Terraform, Python, Monitoring'),(12,3,'Security Analyst','Security Analyst responsible for monitoring security alerts, analyzing vulnerabilities, performing risk assessments, and using tools such as SIEM, IDS/IPS, and Python.',75000.00,95000.00,'Full-time',NULL,'2025-01-09',1,'2026-03-25 04:23:03','Networking, Firewalls, SIEM, Linux, Threat Detection, Incident Response, Security Tools'),(13,4,'UI/UX Designer','UI/UX Designer skilled in Figma, Adobe XD, wireframing, prototyping, user research, and creating intuitive user interfaces for web and mobile applications.',60000.00,80000.00,'Full-time',NULL,'2025-01-10',1,'2026-03-25 04:23:03','Figma, Wireframing, Prototyping, User Research, UI Design, UX Design, HTML, CSS'),(14,5,'Product Manager','Product Manager responsible for roadmap planning, feature prioritization, Agile ceremonies, user story creation, and cross-functional communication.',90000.00,120000.00,'Full-time',NULL,'2025-01-11',1,'2026-03-25 04:23:03','Roadmapping, Agile, Communication, Market Research, Requirements, Leadership'),(15,1,'Technical Writer','Technical Writer skilled in documentation, technical communication, editing, and creating user guides, API documentation, and knowledge base articles.',55000.00,75000.00,'Contract',NULL,'2025-01-12',1,'2026-03-25 04:23:03','Technical Writing, Documentation, Editing, Research, Communication, Markdown'),(16,2,'Intern - Data','Data Intern position requiring basic knowledge of SQL, Excel, Python, and data cleaning. Will assist analysts with reporting and data preparation.',30000.00,40000.00,'Internship',NULL,'2025-01-13',1,'2026-03-25 04:23:03','SQL, Excel, Python, Data Cleaning, Data Visualization'),(17,4,'Intern - Development','Development Intern role requiring basic programming skills in Python, HTML, CSS, and JavaScript. Will assist developers with debugging and small features.',32000.00,42000.00,'Internship',NULL,'2025-01-14',1,'2026-03-25 04:23:03','Python, JavaScript, HTML, CSS, Git, Debugging'),(18,7,'Software Architect','Software Architect responsible for designing system architecture, leading development teams, and working with Python, SQL, cloud technologies, and microservices.',120000.00,150000.00,'Full-time',NULL,NULL,1,'2026-03-25 16:14:01','Python, Java, System Design, Microservices, AWS, Docker, Kubernetes, SQL');
/*!40000 ALTER TABLE `jobs` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-04-01  0:59:45
