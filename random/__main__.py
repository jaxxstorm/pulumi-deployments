"""A Python Pulumi program"""

import pulumi
import pulumi_random as random


string = random.RandomString("string", length=13)
