DROP TABLE cursos;

CREATE TABLE cursos (
    id number NOT NULL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    preco REAL
);

INSERT INTO cursos VALUES (1,"Python pra quem não sabe nada", 100.0);
INSERT INTO cursos VALUES (2,"Java de guerrilha", 200.0);
INSERT INTO cursos VALUES (3,"Terapia Javascript ", 300.0);