# Load Javascript objects into postgresql as jsonb
Load a line by line json/javascript object file into postgres using python3 with psycopg2. 

# Usage
python3 python_load_json_postgresql.py ~/myjson.json mytable 

# Warning
I pass each line to node first in case it's a javascript object being turned into json. Edit this if you don't want this.

# Rational
When scraping angular sites you often get giant javascript object blobs. Loading these into postgres as jsonb can be tricky.

The following works, kind of

copy table(data)
from 'table.json' 
csv quote e'\x01' delimiter e'\x02';

But sometimes it would break on certain escape characters. You also get breaks when querying data containing null bytes \u0000

I also tried pgfutter but it never actually loaded the data. pgloader doesn't seem to support json. 

# This avoids the following errors
psycopg2.DataError: unsupported Unicode escape sequence DETAIL: \u0000 cannot be converted to text. CONTEXT: JSON data pqsl


