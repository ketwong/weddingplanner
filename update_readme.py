import pandas as pd
import re

# Read the current README contents
with open('README.md', 'r') as file:
    contents = file.read()

# Find the start and end of the table in the README
start = contents.index('| Element | Links | Estimated Cost |\n')
end = contents.index('|---|---|---|\n', start)

# Extract the table from the README and convert to a Pandas DataFrame
table = contents[start:end]
df = pd.read_table(pd.compat.StringIO(table), sep='|', index_col=False)

# Add a new row to the DataFrame
new_row = {'Emoji': '🎉', 'Element': 'New Element', 'Links': '[Link](https://example.com/)', 'Estimated Cost': '£1,000 - £10,000+'}
df = df.append(new_row, ignore_index=True)

# Convert the DataFrame back to a Markdown table
table = df.to_markdown(index=False)

# Replace the old table with the updated table in the README
contents = contents[:start] + table + contents[end:]

# Write the updated contents back to the README
with open('README.md', 'w') as file:
    file.write(contents)
