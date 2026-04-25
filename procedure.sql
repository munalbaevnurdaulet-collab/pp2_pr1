CREATE OR REPLACE PROCEDURE upsert_contact(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    -- Бұл жерде тек кестенің аты болуы керек: phonebook
    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE first_name = p_name;
    ELSE
        INSERT INTO phonebook(first_name, phone) VALUES(p_name, p_phone);
    END IF;
END; $$;

    -- Өшіру процедурасы
CREATE OR REPLACE PROCEDURE delete_contact(p_identifier TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook WHERE first_name = p_identifier OR phone = p_identifier;
END; $$;