DROP TABLE IF EXISTS investment;
CREATE TABLE investment (firm TEXT NOT NULL, year INTEGER NOT NULL, invest REAL NOT NULL, value REAL NOT NULL, capital REAL NOT NULL, PRIMARY KEY(firm,year));
