CREATE TABLE blocks (
    id INT NOT NULL,
    hash VARCHAR(255) NOT NULL,
    expired_date DATE NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE inputs (
    id INT NOT NULL,
    outputID INT NOT NULL,
    txID INT NOT NULL,
    offset INT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE outputs (
    id INT NOT NULL,
    dstAddress VARCHAR(255) NOT NULL,
    value VARCHAR(255) NOT NULL,
    txID INT NOT NULL,
    offset INT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE transactions (
    id INT NOT NULL,
    hash VARCHAR(255) NOT NULL,
    blockID INT NOT NULL,
    PRIMARY KEY (id)
);
