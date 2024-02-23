import sys
from django.test import TestCase

# Create your tests here.
a = "temp_plan_high=0;temp_plan_down=-20;temp_fact_high=-12;temp_fact_down=-23;date_time_subsystem=2024-01-31 19:57:40.040214;date_time_server=2024-01-31 19:57:40.042218;"
print(sys.getsizeof(a))
