\c postgres postgres

CREATE DATABASE produciotn;

ALTER DATABASE produciotn OWNER TO postgres;

-- docker exec -i production psql -U postgres < init_db.sql
--database initialization...
