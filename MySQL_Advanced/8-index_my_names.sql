-- With these attributes:
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
CREATE INDEX idx_name_first
ON names(name(1));
