"""
 ****************************************************************************
 Filename:          Ispiel.py
 Description:       Interface for Spiel actuator based classes
 Creation Date:     5/02/2016
 Author:            Jake Abernathy

 Do NOT modify or remove this copyright and confidentiality notice!
 Copyright (c) 2001 - $Date: 2015/01/14 $ Seagate Technology, LLC.
 The code contained herein is CONFIDENTIAL to Seagate Technology, LLC.
 Portions are also trade secret. Any use, duplication, derivation, distribution
 or disclosure of this code, for any reason, not expressly authorized is
 prohibited. All other rights are expressly reserved by Seagate Technology, LLC.
 ****************************************************************************
"""

from zope.interface import Interface

class ISpiel(Interface):
    """Interface for Spiel actuator based classes"""


    def perform_request(self, jsonMsg):
        """Notifies Spiel actuator to perform the desired request"""