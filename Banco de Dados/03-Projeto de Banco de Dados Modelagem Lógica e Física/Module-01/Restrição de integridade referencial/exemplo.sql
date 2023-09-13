/* Lógico_1: */

CREATE TABLE Funcionario (
    CODIGO INT PRIMARY KEY,
    CPF CHAR,
    Sexo CHAR,
    DT_NASCIMENTO DATE,
    Nome CHAR
);

CREATE TABLE Dependente (
    NR INT,
    Nome CHAR,
    DT_Nascimento DATE,
    fk_Funcionario_CODIGO INT
);
 
ALTER TABLE Dependente ADD CONSTRAINT FK_Dependente_1
    FOREIGN KEY (fk_Funcionario_CODIGO)
    REFERENCES Funcionario (CODIGO)
    ON DELETE CASCADE;