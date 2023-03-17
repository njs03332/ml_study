import os
import random
import re
import math
from argparse import ArgumentParser
from typing import List

import pandas as pd


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-c', '--chapters', nargs='*')

    inputs = os.environ['Comment'].replace('assign roles', '').split()
    args = parser.parse_args(inputs)

    members = [
       "김유리", "주선미", "한단비",
    ]

    df = pd.DataFrame([random.shuffle(members), chapters])

    print(df)

    with open('comment-body.md', 'w') as comment_body:
        df.to_markdown(comment_body, tablefmt='github')

