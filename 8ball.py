#!/usr/bin/env python3
# 8ball

import random

massages = [
    'It is certain to rain', 'It is decidetly so', 'Yes definitely',
    'Reply hazy try again', 'My reply is no', 'Outlook not so good',
    'Very doubtful'
]

print(massages[random.randint(0, len(massages) - 1)])
