import pandas

url = "https://www.runnersworld.com/races-places/a20823734/these-are-the-worlds-fastest-marathoners-and-marathon-courses/"

df = pandas.read_html(url)

print(df)
print(len(df))
print(type(df[0]))
