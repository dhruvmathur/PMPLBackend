# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import subprocess
import os
from subprocess import Popen, PIPE
from subprocess import check_output

from django.db import models

# Create your models here.
# subprocess.call('./OpenCVTest2 p.jpg', shell=True)

out = check_output(["./OpenCVTest2", "p.jpg"])

class File(models.Model):
  file = models.FileField(default='', null=True, blank=True)
  remark = models.CharField(max_length=20)
  timestamp = models.DateTimeField(auto_now_add=True)
  count = check_output(["./OpenCVTest2", file.name])
