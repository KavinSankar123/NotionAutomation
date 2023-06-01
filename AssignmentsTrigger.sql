DROP TRIGGER IF EXISTS checkAssignments ON assignments CASCADE;
DROP FUNCTION IF EXISTS checkDuplicateAssignments() CASCADE;

CREATE OR REPLACE FUNCTION checkDuplicateAssignments()
    RETURNS TRIGGER AS
$$
    DECLARE doesAssignmentExist boolean;
BEGIN
    SELECT EXISTS(SELECT 1 FROM assignments WHERE assignmentName = NEW.assignmentName) INTO doesAssignmentExist;
    IF doesAssignmentExist THEN
        RETURN NULL;
    ELSE
       RETURN NEW;
    END IF;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE TRIGGER checkAssignments
    BEFORE INSERT
    ON assignments
    FOR EACH ROW
EXECUTE FUNCTION checkDuplicateAssignments();
