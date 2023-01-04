# car-finder
Periodically checks car postings

### Running Locally

1. pip install -r requirements.txt
2. python scraper.py (currently only prints listing locally - very limited)

### Phase 1
- Get this working locally
- Initial ref: https://github.com/meub/craigslist-for-sale-alerts

### Phase 2 
- Run on Docker and deploy
    - Link: https://www.dataquest.io/blog/apartment-finding-slackbot/


WIP: Craigslist For Sale Alerts
-------------------

Craigslist For Sale Alerts is a bot that will scrape Craigslist for real-time for sale postings matching specific criteria. When it finds a listing that it hasn't already seen, it will alert you via Slack and/or Email.

Settings
--------------------

Look in `settings.py` for the list of configuration options. The options are:

 * LISTING_URLS - the harcoded Craigslist searches you want to alert on

Deployment
--------------------

    # copy all files to server
    scp *.py user@domain:/path/to/project/directory
    scp listings.db user@domain:/path/to/project/directory

    # install modules
    pip install -r requirements.txt

    # set permissions
    chmod +x main_loop.py
    chmod +x scraper.py
    chmod +x settings.py
    chmod +x util.py
    chmod +x listings.db

    # start as service
    nohup python main_loop.py &

    # find it again
    ps ax | grep main_loop.py

    # kill it 
    kill -9 process-id



Testing
--------------------

The `remove_listing.py` file is useful for testing your alerts and allows you to easily delete a record from your local database to make sure your alert fires as you expect. Also, it displays the most recent 15 items in your local database for debugging purposes. You must know the Craigslist ID to be able to delete the record.