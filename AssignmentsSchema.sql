DROP TABLE IF EXISTS assignments CASCADE;
DROP TABLE IF EXISTS courses CASCADE;


CREATE TABLE courses (
    course varchar(20) NOT NULL,
    CONSTRAINT PK_Course PRIMARY KEY (course)
);

CREATE TABLE assignments (
    course varchar(20) NOT NULL,
    assignmentName text NOT NULL,
    due_date date NOT NULL,
    CONSTRAINT PK_Assignment PRIMARY KEY (assignmentName),
    CONSTRAINT FK_course FOREIGN KEY (course) REFERENCES  Courses (course)
);

INSERT INTO courses VALUES('CS1632');
INSERT INTO courses VALUES('CS1555');
INSERT INTO courses VALUES('CS1502');
INSERT INTO courses VALUES('ECON0100');
INSERT INTO courses VALUES('NROSCI0080');
