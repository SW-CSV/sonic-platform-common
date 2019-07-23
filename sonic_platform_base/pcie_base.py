#!/usr/bin/env python
#
# pcie_base.py
#
# Abstract base class for implementing platform-specific
#  PCIE functionality for SONiC
#

try:
    import abc
except ImportError as e:
    raise ImportError (str(e) + " - required module not found")

class PcieBase(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def get_pcie_speed(self,device):
        
      
        return 0
    
    