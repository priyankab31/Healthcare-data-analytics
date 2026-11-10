
-- =====================================================
-- PROJECT: HEALTHCARE DATA ANALYTICS
-- FILE: healthcare_analysis.sql
-- DATABASE: healthcare_db
-- TABLE: patients
-- =====================================================


-- 1. Total Number of Patients

SELECT
    COUNT(*) AS total_patients
FROM patients;


-- 2. Average Patient Age

SELECT
    ROUND(AVG(age), 2) AS average_patient_age
FROM patients;


-- 3. Total Healthcare Treatment Cost

SELECT
    SUM(treatment_cost) AS total_treatment_cost
FROM patients;


-- 4. Department-wise Patient Count

SELECT
    department,
    COUNT(*) AS total_patients
FROM patients
GROUP BY department
ORDER BY total_patients DESC;


-- 5. Inpatient vs Outpatient Analysis

SELECT
    admission_status,
    COUNT(*) AS total_patients,
    ROUND(
        COUNT(*) * 100.0 /
        NULLIF((SELECT COUNT(*) FROM patients), 0),
        2
    ) AS percentage
FROM patients
GROUP BY admission_status;


-- 6. Most Common Diagnosis

SELECT
    diagnosis,
    COUNT(*) AS diagnosis_count
FROM patients
GROUP BY diagnosis
ORDER BY diagnosis_count DESC
LIMIT 5;


-- 7. Monthly Healthcare Expenditure

SELECT
    DATE_TRUNC('month', visit_date)::date AS visit_month,
    SUM(treatment_cost) AS monthly_expenditure
FROM patients
GROUP BY DATE_TRUNC('month', visit_date)
ORDER BY visit_month;


-- 8. Average Treatment Cost by Department

SELECT
    department,
    ROUND(AVG(treatment_cost), 2) AS average_cost
FROM patients
GROUP BY department
ORDER BY average_cost DESC;


-- 9. Age Group Analysis

SELECT
    CASE
        WHEN age <= 18 THEN '0-18'
        WHEN age <= 35 THEN '19-35'
        WHEN age <= 50 THEN '36-50'
        WHEN age <= 65 THEN '51-65'
        ELSE 'Above 65'
    END AS age_group,
    COUNT(*) AS patient_count
FROM patients
GROUP BY age_group
ORDER BY patient_count DESC;


-- 10. Department-wise Total Treatment Cost

SELECT
    department,
    SUM(treatment_cost) AS total_department_cost
FROM patients
GROUP BY department
ORDER BY total_department_cost DESC;


-- =====================================================
-- END OF HEALTHCARE ANALYTICS SQL SCRIPT
-- =====================================================
