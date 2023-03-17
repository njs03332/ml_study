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
    parser.add_argument('-s', '--seed', type=int, default=None)

    inputs = os.environ['Comment'].replace('assign roles', '').split()
    args = parser.parse_args(inputs)

    if args.seed is not None:
        random.seed(args.seed)

    members = [
       "김유리", "주선미", "한단비",
    ]
    
    if args.chapters is None:
        chapters = [1, 2, 3]
    else:
        chapters = args.chapters

    random.shuffle(members)
    df = pd.DataFrame([members, chapters], index=['member', 'chapter'])

    print(df)

    with open('comment-body.md', 'w') as comment_body:
        df.to_markdown(comment_body, tablefmt='github')

