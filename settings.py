# configuration for gws tester

HOST = 'groups.uw.edu'
# HOST = 'dev.groups.uw.edu'
# HOST = 'eval.groups.uw.edu'

CERT_FILE = '/Users/jimt/src/UW/IAM/certs/jim7.cac.washington.edu.crt.uwca'
KEY_FILE = '/Users/jimt/src/UW/IAM/certs/jim7.cac.washington.edu.key.uwca'
CA_FILE = '/Users/jimt/src/UW/IAM/certs/cacerts.cert'
VERIFY_HOST = True

GWS_BASE = 'https://' + HOST + '/group_sws/v3'
GROUP_BASE = 'u_jim7_testbase'

SCHEMA = 'urn:mace:washington.edu:schemas:groups:1.0'

# test group 1 definition

testgroup1 = {
  "id": "u_jim7_testbase_gwstest1",
  "displayName": "json autotest group 1",
  "description": "This is a general purpose group for testing various Group Service functionality.",
  "contact": "jim7",
  "authnfactor": "1",
  "classification": "u",
  "dependson": "uw_employee",
  "admins": [
    {
      "type": "dns",
      "id": "jim7.cac.washington.edu"
    },
    {
      "type": "uwnetid",
      "id": "jim7"
    }
  ],
  "updaters": [
    {
      "type": "eppn",
      "id": "jim.tomlinson@gmail.com"
    }
  ],
  "creators": [
    {
      "type": "group",
      "id": "u_jim7_testbase_gwstest1"
    }
  ],
  "readers": [
    {
      "type": "set",
      "id": "all"
    }
  ]
}

testgroup2 = {
  "id": "u_jim7_testbase_gwstest2",
  "displayName": "json autotest group 2",
  "description": "This is a general purpose group for testing various Group Service functionality.",
  "contact": "jim7",
  "authnfactor": "1",
  "classification": "u",
  "admins": [
    {
      "type": "dns",
      "id": "jim7.cac.washington.edu"
    },
    {
      "type": "uwnetid",
      "id": "jim7"
    }
  ]
}

testgroup3 = {
  "id": "u_jim7_testbase_gwstest2_group3",
  "displayName": "json autotest group 3",
  "description": "This is a general purpose group for testing various Group Service functionality.",
  "contact": "jim7",
  "authnfactor": "1",
  "classification": "u",
  "admins": [
    {
      "type": "dns",
      "id": "jim7.cac.washington.edu"
    }
  ]
}

testgroup4 = {
  "id": "u_jim7_testbase_gwstest4",
  "displayName": "json autotest group 4",
  "description": "This is a general purpose group for testing various Group Service functionality.",
  "contact": "jim7",
  "authnfactor": "1",
  "classification": "u",
  "admins": [
    {
      "type": "dns",
      "id": "jim7.cac.washington.edu"
    },
    {
      "type": "uwnetid",
      "id": "jim7"
    }
  ]
}

testgroup5 = {
  "id": "u_jim7_testbase_gwstest5",
  "displayName": "json autotest group 5",
  "description": "This is a general purpose group for testing various Group Service functionality.",
  "contact": "jim7",
  "authnfactor": "1",
  "classification": "u",
  "admins": [
    {
      "type": "dns",
      "id": "jim7.cac.washington.edu"
    },
    {
      "type": "uwnetid",
      "id": "jim7"
    }
  ]
}


members1 = [
 {"type": "uwnetid", "id": "jim7"},
 {"type": "uwnetid", "id": "markiel"},
 {"type": "uwnetid", "id": "pass"},
 {"type": "uwnetid", "id": "imf"},
 {"type": "uwnetid", "id": "annedt"},
 {"type": "uwnetid", "id": "annt"},
 {"type": "uwnetid", "id": "glenrg"},
 {"type": "dns", "id": "jim7.cac.washington.edu"},
 {"type": "group", "id": "u_jim7"}
]

members2 = [
 {"type": "uwnetid", "id": "joeuser"},
 {"type": "uwnetid", "id": "lisas22g"}
]
members2not = [
 {"type": "uwnetid", "id": "joeuser"},
 {"type": "uwnetid", "id": "0joeuser"},  # see test
 {"type": "uwnetid", "id": "lisas22g"}
]

google_affiliate_1 = {
 "name": "google",
 "status": "active",
 "senders": []
}
google_affiliate_2 = {
 "name": "google",
 "status": "active",
 "senders": ["member"]
}
google_affiliate_3 = {
 "name": "google",
 "status": "active",
 "senders": ["bogus"]
}
google_affiliate_9 = {
 "name": "google",
 "status": "inactive",
 "senders": []
}

email_affiliate_1 = {
 "name": "email",
 "status": "active",
 "senders": []
}
email_affiliate_2 = {
 "name": "email",
 "status": "active",
 "senders": ["dc=all"]
}
email_affiliate_9 = {
 "name": "email",
 "status": "inactive",
 "senders": []
}
