-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT *
FROM crime_scene_reports
WHERE year = '2025'
AND month = '7'
AND day = '28'
AND street = 'Humphrey Street';

SELECT *
FROM interviews
WHERE year = '2025'
AND month = '7'
AND transcript LIKE '%bakery%';

SELECT *
FROM bakery_security_logs
WHERE year = '2025'
AND month = '7'
AND day = '28'
AND hour = '10'
AND minute BETWEEN 15 AND 30
AND activity = 'exit';


SELECT person_id
FROM bank_accounts
JOIN atm_transactions ON bank_accounts.accounts_number = atm_transactions.account_number
WHERE atm_transactions.year = '2025'
AND atm_transactions.month = '7'
AND atm_transactions.day = '28'
AND atm_transactions.atm_location = 'Leggett Street';

SELECT *
FROM phone_calls
WHERE year = '2025'
AND month = '7'
AND day = '28'
AND duration <= 60;

