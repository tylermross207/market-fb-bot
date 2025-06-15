from apscheduler.schedulers.blocking import BlockingScheduler
from market_summary import get_market_summary
from facebook_poster import post_to_facebook

scheduler = BlockingScheduler()

@scheduler.scheduled_job('cron', hour=9, minute=0)
def scheduled_post():
    message = get_market_summary()
    result = post_to_facebook(message)
    print(result)

if __name__ == "__main__":
    scheduler.start()
