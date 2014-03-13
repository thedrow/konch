#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

import arbok

context = {
    'randint': random.randint,
    'random': random.random,
    'choice': random.choice,
}

banner = '''
"Probability is not a mere computation of odds on the dice or more complicated
variants; it is the acceptance of the lack of certainty in our knowledge and
the development of methods for dealing with our ignorance."
- Nassim Nickolas Taleb
'''

arbok.config({
    'context': context,
    'banner': banner,
    'shell': arbok.IPythonShell,
})
