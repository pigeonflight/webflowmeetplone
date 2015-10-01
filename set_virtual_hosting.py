from os import getenv
import transaction
SITE = getenv("SITE_ID")
HOST=getenv('HOST')
print "-----> Plone site %s exists" % SITE
print "-----> Setting virtualhost settings"
app.virtual_hosting.set_map('%s/Plone' % HOST)
transaction.commit()
