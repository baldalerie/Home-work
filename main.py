#task 1

import json 
from pprint import pprint

purchase_formatted_list = []
purchase_formatted_obj = {}

with open("purchase_logs.txt", "r", encoding = 'utf-8') as f:
   content = f.readlines()

for p in content:  
  new_purchase = json.loads(p)
  key = new_purchase['user_id']
  value = new_purchase['category']
  new_purchase_formatted = {key:value}
  
  purchase_formatted_list.append(new_purchase_formatted)
  purchase_formatted_obj[key]=value

pprint(purchase_formatted_list[:5])
print()
      
#task 2
funnel_formatted = []
with open("funnel.csv", "r", encoding = 'utf-8') as f:
    content = f.readlines()
i= 0 
for p in content:
  p=p.strip().split(',')
  key, source = p 
  if key in list(purchase_formatted_obj.keys()):
    print(key, source, purchase_formatted_obj[key], sep=', ')
    i=i+1
    if i>5:
      break
 
  
 
  
 
