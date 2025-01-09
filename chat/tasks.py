from celery import shared_task
from .models import Test,Position
import json
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import requests
from .utils import get_random_code
@shared_task
def fetch_and_update_all():
    try:
        url='https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'
        response=requests.get(url)
            # Check the response status
        if response.status_code == 200:
            data = response.json()
            for item in data:
                instance,_=Position.objects.get_or_create(name=item["name"])
                instance.image=item["image"]
                instance.price=item["current_price"]
                instance.rank=item["market_cap_rank"]
                instance.market_cap=item["market_cap"]
                instance.save()
        return f"Updated {len(data)} records"
                
    except Exception as e:
        print(f"Error: {str(e)}")
@shared_task
def create_code():
    for instance in Test.objects.all():
        instance.code=get_random_code()
        instance.save()
task_name = 'Fetch API Results Periodically'
PeriodicTask.objects.filter(name=task_name).delete()

schedule, _ = IntervalSchedule.objects.get_or_create(
    every=30,
    period=IntervalSchedule.SECONDS,
)
# Add a periodic task
PeriodicTask.objects.create(
    interval=schedule,
    name=task_name,
    task='chat.tasks.fetch_and_update_all',  # Full path to the task
    args=json.dumps([]),  # Arguments can be passed here if needed
)