# -*- coding: utf-8 -*-
"""regularisation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1evsor-xx4ewduPx3iel2Cx16j_4JIGjv
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

""" regularization"""
def L1_Loss(model, factor=0.0005):
  l1 = nn.L1Loss(size_average=False)
  reg_loss = 0
  for param in model.parameters():

    zero_vector=torch.zeros_like(param)
    reg_loss += l1(param,zero_vector)

  return factor * reg_loss