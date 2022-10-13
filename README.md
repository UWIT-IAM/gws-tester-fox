# Group Web Service tester
These are some Json representation tests we can run when deploying/migrating.

## Settings and groups setup
* Copy settings.tmpl to settings.py and edit that for your local configuration.
* You must create the base group, as identified in your settings.py, and permit your certificate to be a subgroup creator.  Call it "u\_<yournetid>_test".
* You must identify your client and ca certs.
* The membership tests use real ids.

## Testing

* Make a virtual env and install what's in requirements.txt. The latest version of python I've been able to run these tests with is 3.8.2, as some newer version introduced some breaking changes.<br>
`$ pyenv local 3.8.2`<br>
`$ virtualenv -p 3.8.2 env`<br>
`$ . ./env/bin/activate`<br>
``$ pip install `cat requirements.txt` ``<br>
`$ nosetests .`<br>
* The tests should clean up after themselves.

Note that some of the tests rely on ldap membership synchronizing.  That requires the ldap_provisioner running on the target service.

## Style

* Use: pycodestyle --max-line-length=150  *.py test


