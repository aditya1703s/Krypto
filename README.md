Introduction:

This is a bitcoin price alerting system. It alerts the user via mail as soon as the price crosses the desired value whether the user is being bullish or bearish for the coin. The API used for the task is coingecko which provides free API to get crypto details.

Approach used:

1. Import necessary libraries(pycoingecko, pandas, requests etc.)
2. Get value of current price from coingecko API
3. Set the desired value where we want to get alert
4. Used smtp to send mails.

Usage:
1. Run the .py file provided.
2. Enter sender's email address, password, receiver's mail id and password.
3. Choose weather you need to be bullish or bearish on coin.
4. Enter the target price.
5. You will get an alert on mail as soon as soon as target price is achieve.
