#!/bin/bash
echo "yes" | python3 manage.py flush
python3 hello_world_amz.py create 50