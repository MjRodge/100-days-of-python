# day 47 - amazon price tracker

## objectives
- query a specific amazon item url every day at a specific time
- should the price of item fall below a user-specified price target, an email will be sent to alert the user price is below threshold

## steps taken
1. grab a link on amazon for an item to track 
2. confirm the `User-Agent` and `Accept-Language` http headers of my device at [http://myhttpheader.com](http://myhttpheader.com)
3. build `headers` dictionary to send to `requests` module
4. put returned html content into `beautifulsoup`
5. isolated the elements containing the price of the item