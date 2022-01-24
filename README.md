# pub-popularity
Uses google popular times data to list pubs (or any venue) by popularity. 

## What is Popular Times 
https://support.google.com/business/answer/6263531?hl=en

*Popular times are based on average popularity over the last few months. Popularity for any given hour is shown relative to the typical peak popularity for the business for the week.*

## Example Data Set In "data.csv"

Data Retreived on 2022-01-24

- Values under each heading are sum totals of popularity each hour each day. 
- Total header is sum of whole week. 
- Ordered in Descending Total 
- Places retreived with search term: "pub"

## How To Run 

- Open 'popularity.py' 
- Add Google API KEY https://developers.google.com/maps/documentation/ios-sdk/get-api-key

- Run In Terminal 
```bash 
python3 -i [PATH TO popularity.py]
```
- Run in REPL 
```python
run()
```
