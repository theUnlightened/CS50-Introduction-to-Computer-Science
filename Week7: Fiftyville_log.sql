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
FROM flights
WHERE year = '2025'
AND month = '7'
AND day = '29';

SELECT DISTINCT people.name
FROM people
JOIN bakery_security_logs
    ON people.license_plate = bakery_security_logs.license_plate
JOIN bank_accounts
    ON people.id = bank_accounts.person_id
JOIN atm_transactions
    ON bank_accounts.account_number = atm_transactions.account_number
JOIN phone_calls
    ON people.phone_number = phone_calls.caller
WHERE bakery_security_logs.year = 2025
  AND bakery_security_logs.month = 7
  AND bakery_security_logs.day = 28
  AND bakery_security_logs.activity = 'exit'
  AND bakery_security_logs.hour = 10
  AND bakery_security_logs.minute BETWEEN 15 AND 30
  AND atm_transactions.year = 2025
  AND atm_transactions.month = 7
  AND atm_transactions.day = 28
  AND atm_transactions.atm_location = 'Leggett Street'
  AND atm_transactions.transaction_type = 'withdraw'
  AND phone_calls.year = 2025
  AND phone_calls.month = 7
  AND phone_calls.day = 28
  AND phone_calls.duration < 60
  AND people.passport_number IN(
    SELECT passport_number
    FROM passengers
    WHERE flight_id = '36'
  );

SELECT *
FROM airports
WHERE id = '4';

SELECT people.name
FROM people
JOIN phone_calls
    ON people.phone_number = phone_calls.receiver
WHERE phone_calls.caller = (
    SELECT phone_number
    FROM people
    WHERE name = 'Bruce'
)
AND phone_calls.year = 2025
AND phone_calls.month = 7
AND phone_calls.day = 28
AND phone_calls.duration < 60;
