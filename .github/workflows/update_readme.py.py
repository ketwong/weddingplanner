import pandas as pd

# Read the existing README file
with open('README.md', 'r') as file:
    contents = file.read()

# Define the new data
data = [
    ['💄💅', 'Hair and Makeup', '[Bridebook](https://bridebook.co.uk/), [Hitched](https://www.hitched.co.uk/), [WeddingWire](https://www.weddingwire.co.uk/), [The Knot](https://www.theknot.com/marketplace/wedding-beauty-services)', '£200 - £500+'],
    ['🎁💍', 'Wedding Favors', '[Bridebook](https://bridebook.co.uk/), [Hitched](https://www.hitched.co.uk/), [WeddingWire](https://www.weddingwire.co.uk/), [Not on the High Street](https://www.notonthehighstreet.com/weddings/wedding-favours)', '£100 - £500+'],
    ['🏨🛏️', 'Accommodation for Out-of-Town Guests', '[Booking.com](https://www.booking.com/), [Expedia](https://www.expedia.co.uk/), [Hitched](https://www.hitched.co.uk/), [Hotels.com](https://uk.hotels.com/)', '£500 - £2,000+'],
    ['📋💼', 'Wedding Planner or Coordinator', '[Bridebook](https://bridebook.co.uk/), [Hitched](https://www.hitched.co.uk/), [WeddingWire](https://www.weddingwire.co.uk/), [The Knot](https://www.theknot.com/marketplace/wedding-planners)', '£1,000 - £5,000+']
]

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=['Emoji', 'Element', 'Links', 'Estimated Cost'])

# Convert the DataFrame to a markdown table
table = df.to_markdown(index=False)

# Replace the existing table in the README file with the new table
start = contents.index('| Element | Links | Estimated Cost |\n')
end = contents.index('|---|---|---|\n', start)
new_contents = contents[:start] + table + contents[end:]

# Write the updated contents back to the README file
with open('README.md', 'w') as file:
    file.write(new_contents)
