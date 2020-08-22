from lxml import html
import requests
from random import choice
from hash_map import AlgoHashTable
from email_generator_project import email_list


page = requests.get('https://www.brainyquote.com/topics/wisdom-quotes')
tree = html.fromstring(page.content)
quotes = tree.xpath('//a[@title="view quote"]/text()')


def gen_hash(size):
  hash_table = AlgoHashTable(size)
  hash_table.set_val("g4m3rm1k3@hotmail.com", {'If you can keep your head when all about you are losing thiers and blaming it on you'})
  e_list = email_list(size-1)
  with open('emails.txt', 'w+') as f:
    for email in e_list:
      f.write(email + ":" + choice(quotes)+"\n")

  with open('emails.txt', 'r') as f:
    for line in f.readlines():
      key, val = line.strip().split(":")
      hash_table.set_val(key, val)
  
  return hash_table


# from hash_table_project import gen_hash

# hash_table = gen_hash(256)
# # print(hash_table)
# print(hash_table.get_val("g4m3rm1k3@hotmail.com"))