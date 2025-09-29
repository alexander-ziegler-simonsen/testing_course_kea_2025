-- SQLite-compatible schema and data for 'converter' database

-- Drop the table if it exists
DROP TABLE IF EXISTS grades;

-- Create the table
CREATE TABLE grades (
    nGradeID INTEGER PRIMARY KEY AUTOINCREMENT,
    cDenmark TEXT NOT NULL,
    cUSA TEXT NOT NULL
);

-- Insert data
INSERT INTO grades (cDenmark, cUSA) VALUES
    ('12', 'A+'),
    ('10', 'A'),
    ('7', 'B'),
    ('4', 'C'),
    ('02', 'D'),
    ('00', 'F'),
    ('-3', 'F');
