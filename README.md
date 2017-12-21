# Group Web Service 2.2 tester
These are tests I run during development of Groups 2.2, with Json representations.

## Settings and groups setup
* Copy settings.tmpl to settings.py and edit that for your local configuration.
* You must create the base group, as identified in your settings.py, and permit your certificate to be a subgroup creator.  Call it "u\_yourid_test".
* You must identify your client and ca certs.
* The membership tests use real ids.

## Testing

* Make a virtual env and install what's in requirements.txt
* ``$ nosetests .``
* The tests should clean up after themselves.

Note that some of the tests rely on ldap membership synchronizing.  That requires the ldap_provisioner running on the target service.


