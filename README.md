# pub-popularity
Uses google popular times data to list pubs (or any venue) by popularity. 

## What is 'Popular Times'
https://support.google.com/business/answer/6263531?hl=en

*Popular times are based on average popularity over the last few months. Popularity for any given hour is shown relative to the typical peak popularity for the business for the week.*

## Prerequisites

- Python3 
- Populartimes Python Library https://github.com/m-wrzr/populartimes install with:
```bash 
pip3 install --upgrade git+https://github.com/m-wrzr/populartimes
```

## How To Run 

- Open 'popularity.py' 
- Add Google API KEY https://developers.google.com/maps/documentation/ios-sdk/get-api-key
- Ensure a 'data.csv' file in the same directory as 'popularity.py'

- Run In Terminal 
```bash 
python3 -i [PATH TO popularity.py]
```
- Run in REPL 
```python
run()
```
