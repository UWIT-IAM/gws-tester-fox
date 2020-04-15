# configuration for gws tester

#HOST = 'iam-ws.u.washington.edu'
#HOST = 'groups.uw.edu'
#HOST = 'eval.groups.uw.edu'
HOST = 'dev.groups.uw.edu'
#HOST = 'gws.sandbox.iam.s.uw.edu'



CERT_FILE = '/home/fox/certs/gws.cac-uw.crt'
KEY_FILE = '/home/fox/certs/gws.cac-uw.key'
# CA_FILE = '/home/fox/certs/uwca.crt'
CA_FILE = '/home/fox/certs/cacerts.cert'
VERIFY_HOST = True

GWS_BASE = 'https://' + HOST + '/group_sws/v3'
GROUP_BASE = 'u_fox_jsontests'

SCHEMA = 'urn:mace:washington.edu:schemas:groups:1.0'

# test group 1 definition

testgroup1 = {
  "id": "u_fox_jsontests_gwstest1",
  "displayName": "Fox's json autotest 地球 with a \\ in it's name.",
  "description": "This is a general purpose group for testing various Group Service functionality.",
  "contact": "fox",
  "authnfactor": "1",
  "classification": "u",
  "dependson": "uw_employee",
  "admins": [
    {
      "type": "dns",
      "id": "gws.cac.washington.edu"
    },
    {
      "type": "uwnetid",
      "id": "fox"
    }
  ],
  "updaters": [
    {
      "type": "eppn",
      "id": "fox.1949@gmail.com"
    }
  ],
  "creators": [
    {
      "type": "group",
      "id": "u_fox_jsontests_gwstest1"
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
  "id": "u_fox_jsontests_gwstest2",
  "displayName": "Fox's json autotest group 2",
  "description": "This is a general purpose group for testing various Group Service functionality.",
  "contact": "fox",
  "authnfactor": "1",
  "classification": "u",
  "admins": [
    {
      "type": "dns",
      "id": "gws.cac.washington.edu"
    },
    {
      "type": "uwnetid",
      "id": "fox"
    }
  ]
}

testgroup3 = {
  "id": "u_fox_jsontests_gwstest2_group3",
  "displayName": "Fox's json autotest group 3",
  "description": "This is a general purpose group for testing various Group Service functionality.",
  "contact": "fox",
  "authnfactor": "1",
  "classification": "u",
  "admins": [
    {
      "type": "dns",
      "id": "gws.cac.washington.edu"
    }
  ]
}

testgroup4 = {
  "id": "u_fox_jsontests_gwstest4",
  "displayName": "Fox's json autotest group 4",
  "description": "This is a general purpose group for testing various Group Service functionality.",
  "contact": "fox",
  "authnfactor": "1",
  "classification": "u",
  "admins": [
    {
      "type": "dns",
      "id": "gws.cac.washington.edu"
    },
    {
      "type": "uwnetid",
      "id": "fox"
    }
  ]
}

testgroup5 = {
  "id": "u_fox_jsontests_gwstest5",
  "displayName": "Fox's json autotest group 5",
  "description": "This is a general purpose group for testing various Group Service functionality.",
  "contact": "fox",
  "authnfactor": "1",
  "classification": "u",
  "admins": [
    {
      "type": "dns",
      "id": "gws.cac.washington.edu"
    },
    {
      "type": "uwnetid",
      "id": "fox"
    }
  ]
}


members1 = [
 {"type": "uwnetid", "id": "fox"},
 {"type": "dns", "id": "gws.cac.washington.edu"},
 {"type": "group", "id": "u_fox"}
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
