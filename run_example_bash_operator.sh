#!/bin/bash

# run your first task instance
airflow tasks test example_bash_operator runme_0 2015-01-01

# run a backfill over 2 days
airflow backfill create --dag-id example_bash_operator \
    --from-date 2015-01-01 \
    --to-date 2015-01-02