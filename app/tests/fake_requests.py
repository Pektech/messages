
fake_say_name =  {
  "version": "1.0",
  "session": {
    "dialogState": "STARTED",
    "new": False,
    "sessionId": "amzn1.echo-api.session.0000000-0000-0000-0000-00000000000",
    "application": {
      "applicationId": "fake-application-id"
    },
    "attributes": {},
    "user": {
      "userId": "amzn1.account.AM3B00000000000000000000000"
    }
  },
  "context": {
    "System": {
      "application": {
        "applicationId": "fake-application-id"
      },
      "user": {
        "userId": "amzn1.account.AM3B00000000000000000000000"
      },
      "device": {
        "supportedInterfaces": {
          "AudioPlayer": {}
        }
      }
    },
    "AudioPlayer": {
      "offsetInMilliseconds": 0,
      "playerActivity": "IDLE"
    }
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "string",
    "timestamp": "string",
    "locale": "string",
    "intent": {
      "name": "SayName",
      "slots": {"name":
                    {"name": "name",
                     "confirmationStatus": "NONE"}
        }
      }
    }
}


fake_awake =  {
  "version": "1.0",
  "session": {

    "new": True,
    "sessionId": "amzn1.echo-api.session.0000000-0000-0000-0000-00000000000",
    "application": {
      "applicationId": "fake-application-id"
    },
    "attributes": {},
    "user": {
      "userId": "amzn1.account.AM3B00000000000000000000000"
    }
  },
  "context": {
    "System": {
      "application": {
        "applicationId": "fake-application-id"
      },
      "user": {
        "userId": "amzn1.account.AM3B00000000000000000000000"
      }
    }
  }
,
    "request": {
        "type": "LaunchRequest",
        "requestId": "request5678"
    }
}


fake_say_name_Sam = {
  "version": "1.0",
  "session": {
    "dialogState": "STARTED",
    "new": False,
    "sessionId": "amzn1.echo-api.session.0000000-0000-0000-0000-00000000000",
    "application": {
      "applicationId": "fake-application-id"
    },
    "attributes": {"alexa_id": "999", "my_name": "Sam", "stage": "start"},
    "user": {
      "userId": "amzn1.account.AM3B00000000000000000000000"
    }
  },
  "context": {
    "System": {
      "application": {
        "applicationId": "fake-application-id"
      },
      "user": {
        "userId": "amzn1.account.AM3B00000000000000000000000"
      },
      "device": {
        "supportedInterfaces": {
          "AudioPlayer": {}
        }
      }
    },
    "AudioPlayer": {
      "offsetInMilliseconds": 0,
      "playerActivity": "IDLE"
    }
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "string",
    "timestamp": "string",
    "locale": "string",
    "intent": {
      "name": "SayName",
      "slots": {"name":
                    {"name": "name",
                     "value" : "Sam",
                     "confirmationStatus": "NONE"}
        }
      }
    }
}

fake_check_msg_Sam = {
  "version": "1.0",
  "session": {
    "dialogState": "STARTED",
    "new": False,
    "sessionId": "amzn1.echo-api.session.0000000-0000-0000-0000-00000000000",
    "application": {
      "applicationId": "fake-application-id"
    },
    "attributes": {"alexa_id": "999", "my_name": "Sam", "stage": "start"},
    "user": {
      "userId": "amzn1.account.AM3B00000000000000000000000"
    }
  },
  "context": {
    "System": {
      "application": {
        "applicationId": "fake-application-id"
      },
      "user": {
        "userId": "amzn1.account.AM3B00000000000000000000000"
      },
      "device": {
        "supportedInterfaces": {
          "AudioPlayer": {}
        }
      }
    },
    "AudioPlayer": {
      "offsetInMilliseconds": 0,
      "playerActivity": "IDLE"
    }
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "string",
    "timestamp": "string",
    "locale": "string",
"dialogState": "STARTED",
    "intent": {
      "name": "CheckMessages",

      "confirmationStatus": "NONE"}
        }
      }



fake_check_msg_Bobby = {
  "version": "1.0",
  "session": {
    "dialogState": "STARTED",
    "new": False,
    "sessionId": "amzn1.echo-api.session.0000000-0000-0000-0000-00000000000",
    "application": {
      "applicationId": "fake-application-id"
    },
    "attributes": {"alexa_id": "999", "my_name": "Bobby", "stage": "start"},
    "user": {
      "userId": "amzn1.account.AM3B00000000000000000000000"
    }
  },
  "context": {
    "System": {
      "application": {
        "applicationId": "fake-application-id"
      },
      "user": {
        "userId": "amzn1.account.AM3B00000000000000000000000"
      },
      "device": {
        "supportedInterfaces": {
          "AudioPlayer": {}
        }
      }
    },
    "AudioPlayer": {
      "offsetInMilliseconds": 0,
      "playerActivity": "IDLE"
    }
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "string",
    "timestamp": "string",
    "locale": "string",
    "intent": {
      "name": "CheckMessages",
      "slots": {"name":
                    {"name": "name",
                     "value" : "Bobby",
                     "confirmationStatus": "NONE"}
        }
      }
    }
}

test = {
  "version": "1.0",
  "session": {
    "dialogState": "STARTED",
    "new": False,
    "sessionId": "amzn1.echo-api.session.0000000-0000-0000-0000-00000000000",
    "application": {
      "applicationId": "fake-application-id"
    },
    "attributes": {"alexa_id": "999", "my_name": "Sam", "stage": "start"},
    "user": {
      "userId": "amzn1.account.AM3B00000000000000000000000"
    }
  },
  "context": {
    "System": {
      "application": {
        "applicationId": "fake-application-id"
      },
      "user": {
        "userId": "amzn1.account.AM3B00000000000000000000000"
      },
      "device": {
        "supportedInterfaces": {
          "AudioPlayer": {}
        }
      }
    },
    "AudioPlayer": {
      "offsetInMilliseconds": 0,
      "playerActivity": "IDLE"
    }
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "string",
    "timestamp": "string",
    "locale": "string",
    "intent": {
      "name": "CheckMessages",
      "slots": {"name":
                    {"name": "name",
                     "value" : "Sam",
                     "confirmationStatus": "NONE"}
        }
      }
    }
}

fake_next_msg = {
  "version": "1.0",
  "session": {
    "dialogState": "STARTED",
    "new": False,
    "sessionId": "amzn1.echo-api.session.0000000-0000-0000-0000-00000000000",
    "application": {
      "applicationId": "fake-application-id"
    },
    "attributes": {"alexa_id": "999", "my_name": "Sam", "stage": "start",
        "msg_num": 0,
                "my_msg_list": [
    {
        "deleted_flag": False,
        "fam_sent": 5,
        "fam_to": 1,
        "id": 4,
        "message": "Going to salt a ghost"
    },
    {
        "deleted_flag": False,
        "fam_sent": 2,
        "fam_to": 1,
        "id": 3,
        "message": "Need more apple pie"
    }]
},
    "user": {
      "userId": "amzn1.account.AM3B00000000000000000000000"
    }
  },
  "context": {
    "System": {
      "application": {
        "applicationId": "fake-application-id"
      },
      "user": {
        "userId": "amzn1.account.AM3B00000000000000000000000"
      },
      "device": {
        "supportedInterfaces": {
          "AudioPlayer": {}
        }
      }
    },
    "AudioPlayer": {
      "offsetInMilliseconds": 0,
      "playerActivity": "IDLE"
    }
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "string",
    "timestamp": "string",
    "locale": "string",
    "intent": {
      "name": "NextMsg",

        }
      }
    }


fake_leave_msg = {
  "version": "1.0",
  "session": {
    "dialogState": "STARTED",
    "new": False,
    "sessionId": "amzn1.echo-api.session.0000000-0000-0000-0000-00000000000",
    "application": {
      "applicationId": "fake-application-id"
    },
    "attributes": {"alexa_id": "999", "my_name": "Sam", "stage": "start",
        "msg_num": 0,
                "my_msg_list": [
    {
        "deleted_flag": False,
        "fam_sent": 5,
        "fam_to": 1,
        "id": 4,
        "message": "Going to salt a ghost"
    },
    {
        "deleted_flag": False,
        "fam_sent": 2,
        "fam_to": 1,
        "id": 3,
        "message": "Need more apple pie"
    }]
},
    "user": {
      "userId": "amzn1.account.AM3B00000000000000000000000"
    }
  },
  "context": {
    "System": {
      "application": {
        "applicationId": "fake-application-id"
      },
      "user": {
        "userId": "amzn1.account.AM3B00000000000000000000000"
      },
      "device": {
        "supportedInterfaces": {
          "AudioPlayer": {}
        }
      }
    },
    "AudioPlayer": {
      "offsetInMilliseconds": 0,
      "playerActivity": "IDLE"
    }
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "string",
    "timestamp": "string",
    "locale": "string",
    "intent": {
      "name": "LeaveMessage",
        "confirmationStatus": "NONE",
                            "slots": {
                                "msg": {
                                    "name": "msg",
                                  "value" : "zombies coming home",
                                    "confirmationStatus": "NONE"
                                },
                                "to_name": {
                                    "name": "to_name",
                                    "value": "dean",
                                    "confirmationStatus": "NONE"
                                }
                            }
                        },
                        "dialogState": "STARTED"

        }
      }
