from os import getenv
print "Plone is installed"
URL=getenv('URL')
HOSTNAME = URL.split(".")[0]
import transaction
app.virtual_hosting.set_map('%s/Plone' % HOSTNAME)
transaction.commit()
