from pathlib import Path
import sqlite3, pandas as pd
base=Path(__file__).resolve().parent
con=sqlite3.connect(base/'investment.sqlite')
con.executescript((base/'schema.sql').read_text())
df=pd.read_csv(base/'data.csv')
df['year']=df.year.astype(int)
df.to_sql('investment',con,if_exists='append',index=False)
assert con.execute('SELECT COUNT(*) FROM investment').fetchone()[0]==len(df)
queries=(base/'analysis_queries.sql').read_text().split(';')
for i,q in enumerate(queries):
    if "SELECT" in q.upper():
        out=pd.read_sql_query(q,con)
        out.to_csv(base/f'query_{i+1}_results.csv',index=False)
        print(f'Query {i+1}: {len(out)} rows')
con.close()
